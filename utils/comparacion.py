"""Modulo de comparacion Datos1 vs Datos2.

Tabla 1 = CONSULTA, Tabla 2 = BUSQUEDA: cada valor de D1 se busca en D2.
Soporta mismo tipo o cruzado (estructuras distintas): la comparacion se hace
por UN campo elegido de cada tabla (indice de columna), no por posicion.

Tipos de coincidencia:
- exacta: valores normalizados identicos (4551 = 4551)
- parcial: la consulta aparece como token o subcadena en la busqueda
  (4551 = 998-4551), o comparten un token (tokens separados por
  guiones, barras, espacios, etc.). Los tokens puramente numericos se
  comparan sin ceros a la izquierda (004551 = 4551).

Formato de las tres listas de resultados (estilo comparativo, UNA sola
fila por registro y las claves juntas al centro):
    Origen | columnas D1 (clave al final) | clave D2 | resto de columnas D2
- tableWidget_coincidencias: SOLO coincidencias exactas (columna Tipo)
- tableWidget_parciales: SOLO coincidencias parciales (columna Tipo)
- tableWidget_faltantes: filas de Datos1 sin ninguna coincidencia
  (columna Origen "DATOS 1" y columnas D2 vacias, sin contraparte).
"""

import re

from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

COLOR_D1 = QColor(200, 230, 255)  # celeste suave
COLOR_D2 = QColor(255, 243, 200)  # crema suave
COLOR_CLAVE = QColor(255, 255, 255)

_FUENTE_CLAVE: QFont | None = None


def _fuente_clave() -> QFont:
    """Fuente en negrita para las columnas de clave (se crea en el primer uso)."""
    global _FUENTE_CLAVE
    if _FUENTE_CLAVE is None:
        fuente = QFont()
        fuente.setBold(True)
        _FUENTE_CLAVE = fuente
    return _FUENTE_CLAVE


def normalizar(valor: object, case_sensitive: bool = False, strip: bool = True) -> str:
    texto = "" if valor is None else str(valor)
    if strip:
        texto = texto.strip()
        # Colapsar espacios internos multiples: "a  b" -> "a b"
        texto = " ".join(texto.split())
    if not case_sensitive:
        texto = texto.casefold()
    return texto


def leer_qtable(tabla: QTableWidget) -> tuple[list[str], list[list[str]]]:
    """Lee cabecera + filas de un QTableWidget como listas de str."""
    n_filas = tabla.rowCount()
    n_cols = tabla.columnCount()
    cabecera: list[str] = []
    for j in range(n_cols):
        item = tabla.horizontalHeaderItem(j)
        texto = item.text() if item is not None else ""
        cabecera.append(texto if texto else f"Campo{j + 1}")
    filas: list[list[str]] = []
    for i in range(n_filas):
        fila: list[str] = []
        for j in range(n_cols):
            item = tabla.item(i, j)
            fila.append(item.text() if item is not None else "")
        filas.append(fila)
    return cabecera, filas


def _sin_ceros(token: str) -> str:
    """Forma canonica de tokens numericos: '004551' -> '4551'."""
    if token.isdigit():
        recortado = token.lstrip("0")
        return recortado if recortado else "0"
    return token


def tokens_de(normalizado: str) -> list[str]:
    """Divide en tokens alfanumericos unicode ('998-4551' -> ['998', '4551'])."""
    return re.findall(r"[^\W_]+", normalizado, flags=re.UNICODE)


def _igual_token(a: str, b: str) -> bool:
    if a == b:
        return True
    if a.isdigit() and b.isdigit():
        return _sin_ceros(a) == _sin_ceros(b)
    return False


def tipo_coincidencia(
    consulta: str,
    busqueda: str,
    parcial: bool = True,
    min_longitud_parcial: int = 3,
) -> str | None:
    """Clasifica el match entre valores YA normalizados.

    Devuelve 'exacta', 'parcial' o None (sin coincidencia).
    """
    if consulta == "" or busqueda == "":
        return "exacta" if consulta == busqueda else None
    if consulta == busqueda:
        return "exacta"
    if not parcial:
        return None
    tok_q = tokens_de(consulta)
    tok_s = tokens_de(busqueda)
    for a in tok_q:
        for b in tok_s:
            if _igual_token(a, b):
                return "parcial"
    if len(consulta) >= min_longitud_parcial and consulta in busqueda:
        return "parcial"
    if len(busqueda) >= min_longitud_parcial and busqueda in consulta:
        return "parcial"
    return None


def comparar_con_detalle(
    filas1: list[list[str]],
    idx1: int,
    filas2: list[list[str]],
    idx2: int,
    case_sensitive: bool = False,
    strip: bool = True,
    omitir_vacios: bool = True,
    parcial: bool = True,
    min_longitud_parcial: int = 3,
) -> list[tuple[int, int, str]]:
    """Compara D1 (consulta) contra D2 (busqueda). Devuelve (i1, i2, tipo).

    - Soporta duplicados: 1 consulta puede parear con N busquedas.
    - Omite claves vacias para no matchear celdas en blanco.
    - Indice invertido: exacta O(1) + tokens O(1); solo el fallback por
      subcadena recorre D2 (evita el O(N*M) completo cuando ya hubo match
      por token/exacta para esa consulta).
    """
    # Precalcular busqueda (D2): norma, tokens y formas numericas canonicas.
    normas2: list[str] = []
    tokens2: list[set[str]] = []
    mapa_exacta: dict[str, list[int]] = {}
    indice_token: dict[str, list[int]] = {}
    for i2, fila2 in enumerate(filas2):
        norma = normalizar(fila2[idx2] if idx2 < len(fila2) else "", case_sensitive, strip)
        normas2.append(norma)
        if omitir_vacios and norma == "":
            tokens2.append(set())
            continue
        mapa_exacta.setdefault(norma, []).append(i2)
        toks = {_sin_ceros(t) for t in tokens_de(norma)}
        tokens2.append(toks)
        for t in toks:
            indice_token.setdefault(t, []).append(i2)

    resultado: list[tuple[int, int, str]] = []
    for i1, fila1 in enumerate(filas1):
        if idx1 >= len(fila1):
            continue
        consulta = normalizar(fila1[idx1], case_sensitive, strip)
        if omitir_vacios and consulta == "":
            continue
        vistos: set[int] = set()

        # 1) Exactas por indice
        for i2 in mapa_exacta.get(consulta, []):
            vistos.add(i2)
            resultado.append((i1, i2, "exacta"))

        if parcial:
            # 2) Tokens por indice invertido (cubre 4551 = 998-4551)
            for t in {_sin_ceros(x) for x in tokens_de(consulta)}:
                for i2 in indice_token.get(t, []):
                    if i2 not in vistos:
                        vistos.add(i2)
                        resultado.append((i1, i2, "parcial"))
            # 3) Subcadena solo sobre no vistos (cubre pegados sin separador)
            if len(consulta) >= min_longitud_parcial:
                for i2, norma2 in enumerate(normas2):
                    if i2 in vistos or norma2 == "":
                        continue
                    if consulta in norma2 or (
                        len(norma2) >= min_longitud_parcial and norma2 in consulta
                    ):
                        vistos.add(i2)
                        resultado.append((i1, i2, "parcial"))
    return resultado


def comparar_por_campos(
    filas1: list[list[str]],
    idx1: int,
    filas2: list[list[str]],
    idx2: int,
    case_sensitive: bool = False,
    strip: bool = True,
    omitir_vacios: bool = True,
    parcial: bool = True,
    min_longitud_parcial: int = 3,
) -> list[tuple[int, int]]:
    """Devuelve pares (i1, i2) donde hay coincidencia exacta o parcial.

    - Soporta duplicados: 1 fila de D1 puede parear con N filas de D2.
    - Omite claves vacias para no matchear celdas en blanco.
    - D1 = consulta, D2 = busqueda.
    """
    return [
        (i1, i2)
        for i1, i2, _ in comparar_con_detalle(
            filas1,
            idx1,
            filas2,
            idx2,
            case_sensitive,
            strip,
            omitir_vacios,
            parcial,
            min_longitud_parcial,
        )
    ]


def _columnas_comparativas(
    cab1: list[str], cab2: list[str], idx1: int, idx2: int
) -> list[tuple[str, int]]:
    """Orden de columnas comparativo: ('primero',-1), D1 con clave al final,
    clave D2 y luego el resto de D2 (claves juntas al centro)."""
    columnas: list[tuple[str, int]] = [("primero", -1)]
    columnas.extend(("d1", k) for k in range(len(cab1)) if k != idx1)
    if 0 <= idx1 < len(cab1):
        columnas.append(("d1", idx1))
    if 0 <= idx2 < len(cab2):
        columnas.append(("d2", idx2))
    columnas.extend(("d2", k) for k in range(len(cab2)) if k != idx2)
    return columnas


def cabecera_comparativa(
    cab1: list[str],
    cab2: list[str],
    idx1: int = 0,
    idx2: int = 0,
    etiqueta_primero: str = "Tipo",
) -> list[str]:
    """Cabecera comparativa: ['Tipo'/'Origen', 'D1:x', ..., 'D1:clave',
    'D2:clave', 'D2:y', ...]."""
    etiquetas = [etiqueta_primero]
    for lado, k in _columnas_comparativas(cab1, cab2, idx1, idx2)[1:]:
        prefijo = "D1" if lado == "d1" else "D2"
        cab = cab1 if lado == "d1" else cab2
        etiquetas.append(f"{prefijo}:{cab[k]}")
    return etiquetas


def _pintar_fila_comparativa(
    destino: QTableWidget,
    r: int,
    columnas: list[tuple[str, int]],
    cab1: list[str],
    cab2: list[str],
    fila_d1: list[str],
    fila_d2: list[str],
    idx1: int,
    idx2: int,
    primero: str,
    color_primero: QColor,
    tooltip_primero: str,
    i1: int | None = None,
    i2: int | None = None,
    tipo: str = "",
) -> None:
    """Pinta una fila: valor inicial, columnas D1 (clave al centro) y D2 al lado."""
    fuente_clave = _fuente_clave()
    sufijo = f" · {tipo}" if tipo else ""
    for c, (lado, k) in enumerate(columnas):
        if lado == "primero":
            item = QTableWidgetItem(primero)
            item.setBackground(color_primero)
            item.setToolTip(tooltip_primero)
            destino.setItem(r, c, item)
            continue
        if lado == "d1":
            valor = fila_d1[k] if k < len(fila_d1) else ""
            etiqueta = f"D1:{cab1[k]}"
            origen = f"D1 fila {i1 + 1}" if i1 is not None else "D1"
            fondo = COLOR_D1
            es_clave = k == idx1
        else:
            valor = fila_d2[k] if k < len(fila_d2) else ""
            etiqueta = f"D2:{cab2[k]}"
            origen = f"D2 fila {i2 + 1}" if i2 is not None else "D2"
            fondo = COLOR_D2
            es_clave = k == idx2
        item = QTableWidgetItem(valor)
        item.setBackground(COLOR_CLAVE if es_clave else fondo)
        if es_clave:
            item.setFont(fuente_clave)
        item.setToolTip(f"{origen} · {etiqueta}{sufijo}")
        destino.setItem(r, c, item)


def indices_no_coincidentes(
    n1: int,
    n2: int,
    detalle: list[tuple[int, int]] | list[tuple[int, int, str]],
) -> tuple[list[int], list[int]]:
    """Devuelve (i1_sin_match, i2_sin_match) en orden original de cada tabla."""
    vistos1 = {p[0] for p in detalle}
    vistos2 = {p[1] for p in detalle}
    return (
        [i for i in range(n1) if i not in vistos1],
        [i for i in range(n2) if i not in vistos2],
    )


def mostrar_faltantes(
    destino: QTableWidget,
    cab1: list[str],
    filas1: list[list[str]],
    cab2: list[str],
    filas2: list[list[str]],
    detalle: list[tuple[int, int]] | list[tuple[int, int, str]],
    idx1: int = 0,
    idx2: int = 0,
) -> list[int]:
    """Pinta en destino las filas de D1 (consulta) sin coincidencia.

    Formato comparativo (una fila por registro): Origen | D1 con la clave
    al final | clave D2 | resto de D2 (columnas D2 vacias, sin contraparte).
    Devuelve [i1_faltantes] para tooltips/mensajes.
    """
    falt1, _ = indices_no_coincidentes(len(filas1), len(filas2), detalle)
    destino.clear()
    destino.setRowCount(0)
    destino.setColumnCount(0)
    if not falt1:
        return falt1
    columnas = _columnas_comparativas(cab1, cab2, idx1, idx2)
    destino.setColumnCount(len(columnas))
    destino.setHorizontalHeaderLabels(
        cabecera_comparativa(cab1, cab2, idx1, idx2, etiqueta_primero="Origen")
    )
    destino.setRowCount(len(falt1))

    for r, i1 in enumerate(falt1):
        fila = filas1[i1] if 0 <= i1 < len(filas1) else []
        _pintar_fila_comparativa(
            destino,
            r,
            columnas,
            cab1,
            cab2,
            fila,
            [],
            idx1,
            idx2,
            primero="DATOS 1",
            color_primero=COLOR_D1,
            tooltip_primero=f"D1 fila {i1 + 1} sin coincidencia en D2",
            i1=i1,
            tipo="sin coincidencia",
        )

    destino.resizeColumnsToContents()
    return falt1


def mostrar_coincidencias(
    destino: QTableWidget,
    cab1: list[str],
    filas1: list[list[str]],
    cab2: list[str],
    filas2: list[list[str]],
    pares: list[tuple[int, int]] | list[tuple[int, int, str]],
    idx1: int = 0,
    idx2: int = 0,
) -> None:
    """Pinta cada par en UNA sola fila (estilo comparativo, claves al centro).

    Columnas: Tipo | D1 (clave al final) | clave D2 | resto de D2.
    Acepta pares (i1, i2) o triples (i1, i2, tipo).
    """
    destino.clear()
    destino.setRowCount(0)
    destino.setColumnCount(0)
    if not pares:
        return
    columnas = _columnas_comparativas(cab1, cab2, idx1, idx2)
    destino.setColumnCount(len(columnas))
    destino.setHorizontalHeaderLabels(cabecera_comparativa(cab1, cab2, idx1, idx2))
    destino.setRowCount(len(pares))

    for r, par in enumerate(pares):
        i1, i2 = par[0], par[1]
        tipo = par[2] if len(par) > 2 else ""
        fila_d1 = filas1[i1] if 0 <= i1 < len(filas1) else []
        fila_d2 = filas2[i2] if 0 <= i2 < len(filas2) else []
        nota = f"Coincidencia {tipo} · " if tipo else "Coincidencia · "
        _pintar_fila_comparativa(
            destino,
            r,
            columnas,
            cab1,
            cab2,
            fila_d1,
            fila_d2,
            idx1,
            idx2,
            primero=tipo or "coincidencia",
            color_primero=COLOR_CLAVE,
            tooltip_primero=(
                f"{nota}D1 fila {i1 + 1} ↔ D2 fila {i2 + 1}"
            ),
            i1=i1,
            i2=i2,
            tipo=tipo,
        )

    destino.resizeColumnsToContents()


def mostrar_parciales(
    destino: QTableWidget,
    cab1: list[str],
    filas1: list[list[str]],
    cab2: list[str],
    filas2: list[list[str]],
    pares: list[tuple[int, int]] | list[tuple[int, int, str]],
    idx1: int = 0,
    idx2: int = 0,
) -> None:
    """Pinta en destino solo los pares con coincidencia parcial.

    Mismo formato comparativo que mostrar_coincidencias (una fila con D1 y
    su coincidencia D2 al lado).
    """
    mostrar_coincidencias(destino, cab1, filas1, cab2, filas2, pares, idx1, idx2)
