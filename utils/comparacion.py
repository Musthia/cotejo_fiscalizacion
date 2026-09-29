"""Modulo de comparacion Datos1 vs Datos2.

Soporta mismo tipo o cruzado (estructuras distintas): la comparacion se hace
por UN campo elegido de cada tabla (indice de columna), no por posicion.

Resultado en tableWidget_coincidencias con filas pareadas:
- fila par (0, 2, 4...): fila completa de Datos1 + etiqueta "DATOS 1"
- fila impar (1, 3, 5...): su coincidencia de Datos2 + etiqueta "DATOS 2"
"""

from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

COLOR_D1 = QColor(200, 230, 255)  # celeste suave
COLOR_D2 = QColor(255, 243, 200)  # crema suave
COLOR_CLAVE = QColor(255, 255, 255)


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


def comparar_por_campos(
    filas1: list[list[str]],
    idx1: int,
    filas2: list[list[str]],
    idx2: int,
    case_sensitive: bool = False,
    strip: bool = True,
    omitir_vacios: bool = True,
) -> list[tuple[int, int]]:
    """Devuelve pares (i1, i2) donde la clave normalizada coincide.

    - Soporta duplicados: 1 fila de D1 puede parear con N filas de D2.
    - Omite claves vacias para no matchear celdas en blanco.
    """
    mapa2: dict[str, list[int]] = {}
    for i2, fila2 in enumerate(filas2):
        if idx2 >= len(fila2):
            continue
        clave = normalizar(fila2[idx2], case_sensitive, strip)
        if omitir_vacios and clave == "":
            continue
        mapa2.setdefault(clave, []).append(i2)

    pares: list[tuple[int, int]] = []
    for i1, fila1 in enumerate(filas1):
        if idx1 >= len(fila1):
            continue
        clave = normalizar(fila1[idx1], case_sensitive, strip)
        if omitir_vacios and clave == "":
            continue
        for i2 in mapa2.get(clave, []):
            pares.append((i1, i2))
    return pares


def cabecera_unificada(cab1: list[str], cab2: list[str]) -> list[str]:
    """Une cabeceras de distinta estructura: ['Origen', 'D1:x / D2:y', ...]."""
    n = max(len(cab1), len(cab2))
    unificada = ["Origen"]
    for k in range(n):
        partes: list[str] = []
        if k < len(cab1):
            partes.append(f"D1:{cab1[k]}")
        if k < len(cab2):
            partes.append(f"D2:{cab2[k]}")
        unificada.append(" / ".join(partes))
    return unificada


def mostrar_coincidencias(
    destino: QTableWidget,
    cab1: list[str],
    filas1: list[list[str]],
    cab2: list[str],
    filas2: list[list[str]],
    pares: list[tuple[int, int]],
    idx1: int = 0,
    idx2: int = 0,
) -> None:
    """Pinta pares en destino: fila D1 completa y debajo su coincidencia D2."""
    destino.clear()
    destino.setRowCount(0)
    destino.setColumnCount(0)
    if not pares:
        return
    cab = cabecera_unificada(cab1, cab2)
    n_datos = len(cab) - 1
    destino.setColumnCount(len(cab))
    destino.setHorizontalHeaderLabels(cab)
    destino.setRowCount(len(pares) * 2)

    fuente_clave = QFont()
    fuente_clave.setBold(True)

    for n, (i1, i2) in enumerate(pares):
        fila_d1 = filas1[i1] if 0 <= i1 < len(filas1) else []
        fila_d2 = filas2[i2] if 0 <= i2 < len(filas2) else []
        r_par, r_impar = n * 2, n * 2 + 1

        item_origen1 = QTableWidgetItem("DATOS 1")
        item_origen1.setBackground(COLOR_D1)
        destino.setItem(r_par, 0, item_origen1)
        for c in range(n_datos):
            valor = fila_d1[c] if c < len(fila_d1) else ""
            item = QTableWidgetItem(valor)
            item.setBackground(COLOR_D1)
            item.setToolTip(f"D1 fila {i1 + 1} · {cab[c + 1]}")
            if c == idx1:
                item.setFont(fuente_clave)
                item.setBackground(COLOR_CLAVE)
            destino.setItem(r_par, c + 1, item)

        item_origen2 = QTableWidgetItem("DATOS 2")
        item_origen2.setBackground(COLOR_D2)
        destino.setItem(r_impar, 0, item_origen2)
        for c in range(n_datos):
            valor = fila_d2[c] if c < len(fila_d2) else ""
            item = QTableWidgetItem(valor)
            item.setBackground(COLOR_D2)
            item.setToolTip(f"D2 fila {i2 + 1} · {cab[c + 1]}")
            if c == idx2:
                item.setFont(fuente_clave)
                item.setBackground(COLOR_CLAVE)
            destino.setItem(r_impar, c + 1, item)

    destino.resizeColumnsToContents()
