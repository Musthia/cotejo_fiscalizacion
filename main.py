"""Punto de entrada de la aplicacion."""

import sys

from PySide6.QtWidgets import QApplication

from views.ventana_principal import VentanaPrincipal


def main() -> int:
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
