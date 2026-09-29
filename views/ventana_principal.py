"""Clase principal de la aplicacion.

Usa como plantilla de edicion: ui/ventana_principal.ui
Compilado generado (NO EDITAR): ui/ventana_principal_ui.py
"""

from PySide6.QtWidgets import QMainWindow

from ui.ventana_principal_ui import Ui_MainWindow
from utils.carga_datos import cargar_en_tabla


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana principal del cotejo de fiscalizacion."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._conectar_carga_datos()
        self.archivo_datos1 = None
        self.archivo_datos2 = None

    # --- Carga Datos 1 / Datos 2 (6 botones por tabla) ---
    def _conectar_carga_datos(self):
        # Datos 1 -> tableWidget_datos1, carpetas recursos/datos_1/...
        self.pushButton_datos_excel.clicked.connect(
            lambda: self._cargar(1, "excel")
        )
        self.pushButton_datos_csv.clicked.connect(lambda: self._cargar(1, "csv"))
        self.pushButton_datos_txt.clicked.connect(lambda: self._cargar(1, "txt"))
        self.pushButton_datos_db.clicked.connect(lambda: self._cargar(1, "db"))
        self.pushButton_datos_acces.clicked.connect(
            lambda: self._cargar(1, "access")
        )
        self.pushButton_nomb_archiv.clicked.connect(
            lambda: self._cargar(1, "archivo")
        )
        # Datos 2 -> tableWidget_datos2, carpetas recursos/datos_2/...
        self.pushButton_datos_excel_2.clicked.connect(
            lambda: self._cargar(2, "excel")
        )
        self.pushButton_datos_csv_2.clicked.connect(lambda: self._cargar(2, "csv"))
        self.pushButton_datos_txt_2.clicked.connect(lambda: self._cargar(2, "txt"))
        self.pushButton_datos_db_2.clicked.connect(lambda: self._cargar(2, "db"))
        self.pushButton_datos_acces_2.clicked.connect(
            lambda: self._cargar(2, "access")
        )
        self.pushButton_nomb_archiv_2.clicked.connect(
            lambda: self._cargar(2, "archivo")
        )

    def _cargar(self, tabla_num: int, tipo: str):
        tabla = self.tableWidget_datos1 if tabla_num == 1 else self.tableWidget_datos2
        ruta = cargar_en_tabla(self, tabla, tabla_num, tipo)
        if ruta is None:
            return
        if tabla_num == 1:
            self.archivo_datos1 = ruta
            # El boton de nombre muestra el ultimo archivo cargado
            self.pushButton_nomb_archiv.setText(ruta.name[:20])
            self.pushButton_nomb_archiv.setToolTip(str(ruta))
        else:
            self.archivo_datos2 = ruta
            self.pushButton_nomb_archiv_2.setText(ruta.name[:20])
            self.pushButton_nomb_archiv_2.setToolTip(str(ruta))
