"""Exportacion de tablas de resultados a varios formatos.

Tablas:
- tableWidget_coincidencias -> pushButton_export_coinc
- tableWidget_faltantes -> pushButton_export_falt

Formatos a eleccion del usuario (filtro del dialogo Guardar):
- Excel (*.xlsx), CSV (*.csv, ';'), Texto (*.txt, TAB), SQLite (*.db)
"""

import csv
import re
import sqlite3
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidget, QWidget

from utils.comparacion import leer_qtable

BASE_DIR = Path(__file__).resolve().parent.parent
EXPORT_DIR = BASE_DIR / "recursos" / "exportados"

FILTRO_EXPORT = (
    "Excel (*.xlsx);;CSV (*.csv);;Texto tabulado (*.txt);;SQLite (*.db)"
)

EXT_POR_FILTRO = {
    "Excel": ".xlsx",
    "CSV": ".csv",
    "Texto": ".txt",
    "SQLite": ".db",
}


def _formato_desde(filtro: str, ruta: Path) -> str:
    for clave in ("Excel", "CSV", "Texto", "SQLite"):
        if clave in filtro:
            return clave
    sufijo = ruta.suffix.lower()
    if sufijo == ".xlsx":
        return "Excel"
    if sufijo == ".csv":
        return "CSV"
    if sufijo == ".txt":
        return "Texto"
    if sufijo in (".db", ".sqlite", ".sqlite3"):
        return "SQLite"
    return "CSV"


def _con_extension(ruta: Path, formato: str) -> Path:
    if ruta.suffix:
        return ruta
    return ruta.with_suffix(EXT_POR_FILTRO[formato])


def _escribir_csv(ruta: Path, cabecera: list[str], filas: list[list[str]]) -> None:
    with ruta.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(cabecera)
        for fila in filas:
            w.writerow([(c if c is not None else "") for c in fila])


def _escribir_txt(ruta: Path, cabecera: list[str], filas: list[list[str]]) -> None:
    with ruta.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(cabecera)
        for fila in filas:
            w.writerow([(c if c is not None else "") for c in fila])


def _escribir_excel(ruta: Path, cabecera: list[str], filas: list[list[str]]) -> None:
    try:
        import openpyxl
    except ImportError as exc:
        raise RuntimeError(
            "Para exportar a Excel instala: venv\\Scripts\\pip.exe install openpyxl"
        ) from exc
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "datos"
    ws.append(cabecera)
    for fila in filas:
        ws.append(list(fila))
    wb.save(ruta)
    wb.close()


def _ident(nombre: str, alternativo: str) -> str:
    limpio = re.sub(r"\W+", "_", nombre, flags=re.UNICODE).strip("_")
    if not limpio:
        limpio = alternativo
    if limpio[0].isdigit():
        limpio = f"t_{limpio}"
    return limpio[:60]


def _escribir_sqlite(
    ruta: Path, cabecera: list[str], filas: list[list[str]], tabla: str = "datos"
) -> None:
    nombre_tabla = _ident(tabla, "datos")
    columnas: list[str] = []
    vistas: set[str] = set()
    for j, h in enumerate(cabecera):
        base = _ident(h, f"c{j + 1}")
        nombre = base
        k = 2
        while nombre.lower() in vistas:
            nombre = f"{base}_{k}"
            k += 1
        vistas.add(nombre.lower())
        columnas.append(nombre)
    con = sqlite3.connect(str(ruta))
    try:
        con.execute(f'DROP TABLE IF EXISTS "{nombre_tabla}"')
        defs = ", ".join(f'"{c}" TEXT' for c in columnas)
        con.execute(f'CREATE TABLE "{nombre_tabla}" ({defs})')
        marcas = ", ".join("?" for _ in columnas)
        cols = ", ".join(f'"{c}"' for c in columnas)
        normalizadas = [
            [(v if v is not None else "") for v in (fila + [""] * len(columnas))[: len(columnas)]]
            for fila in filas
        ]
        con.executemany(
            f'INSERT INTO "{nombre_tabla}" ({cols}) VALUES ({marcas})', normalizadas
        )
        con.commit()
    finally:
        con.close()


def exportar_tabla(
    parent: QWidget | None,
    tabla: QTableWidget,
    titulo: str,
    nombre_sugerido: str,
) -> Path | None:
    """Guarda el contenido de un QTableWidget en el formato que elija el usuario."""
    cabecera, filas = leer_qtable(tabla)
    if not cabecera or not filas:
        QMessageBox.warning(parent, "Exportar", f"{titulo}: no hay filas para exportar.")
        return None
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    ruta_str, filtro = QFileDialog.getSaveFileName(
        parent,
        f"Exportar {titulo}",
        str(EXPORT_DIR / nombre_sugerido),
        FILTRO_EXPORT,
    )
    if not ruta_str:
        return None
    formato = _formato_desde(filtro, Path(ruta_str))
    destino = _con_extension(Path(ruta_str), formato)
    try:
        if formato == "Excel":
            _escribir_excel(destino, cabecera, filas)
        elif formato == "CSV":
            _escribir_csv(destino, cabecera, filas)
        elif formato == "Texto":
            _escribir_txt(destino, cabecera, filas)
        else:
            _escribir_sqlite(destino, cabecera, filas, nombre_sugerido)
    except Exception as exc:  # noqa: BLE001 - se muestra al usuario
        QMessageBox.warning(parent, "Exportar", f"{type(exc).__name__}: {exc}")
        return None
    QMessageBox.information(
        parent, "Exportar", f"{titulo}: {len(filas)} filas en {destino.name}"
    )
    return destino
