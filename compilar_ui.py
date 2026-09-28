"""Compila los .ui de la carpeta ui/ a Python con pyside6-uic.

Regla:
- Fuente de verdad (editable): ui/*.ui  -> se edita en Qt Designer
- Generado (NO EDITAR): ui/*_ui.py

Uso:
    venv\\Scripts\\python.exe compilar_ui.py
    venv\\Scripts\\python.exe compilar_ui.py --force
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UI_DIR = BASE_DIR / "ui"
UIC_EXE = BASE_DIR / "venv" / "Scripts" / "pyside6-uic.exe"

# (origen .ui, destino .py generado)
UIS = [
    (UI_DIR / "ventana_principal.ui", UI_DIR / "ventana_principal_ui.py"),
]


def necesita_compilar(origen: Path, destino: Path, force: bool = False) -> bool:
    if force:
        return True
    if not destino.exists():
        return True
    return origen.stat().st_mtime > destino.stat().st_mtime


def compilar(origen: Path, destino: Path) -> None:
    cmd = [str(UIC_EXE), str(origen), "-o", str(destino)]
    print(f"Compilando {origen.name} -> {destino.name}")
    subprocess.run(cmd, check=True)


def main() -> int:
    force = "--force" in sys.argv
    if not UIC_EXE.exists():
        print(f"No se encontro {UIC_EXE}. Activa el venv.")
        return 1
    for origen, destino in UIS:
        if not origen.exists():
            print(f"Falta plantilla: {origen}")
            return 1
        if necesita_compilar(origen, destino, force):
            compilar(origen, destino)
        else:
            print(f"Sin cambios: {origen.name} (usa --force para recompilar)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
