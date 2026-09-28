"""Clase principal de la aplicacion.

Usa como plantilla de edicion: ui/ventana_principal.ui
Compilado generado (NO EDITAR): ui/ventana_principal_ui.py
"""

from PySide6.QtWidgets import QMainWindow

from ui.ventana_principal_ui import Ui_MainWindow


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana principal del cotejo de fiscalizacion."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
