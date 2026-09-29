"""Clase principal de la aplicacion.

Usa como plantilla de edicion: ui/ventana_principal.ui
Compilado generado (NO EDITAR): ui/ventana_principal_ui.py
"""

from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui.ventana_principal_ui import Ui_MainWindow
from utils.carga_datos import cargar_en_tabla
from utils.comparacion import (
    comparar_por_campos,
    leer_qtable,
    mostrar_coincidencias,
)
from views.dialogo_campos import DialogoCampos


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana principal del cotejo de fiscalizacion."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._conectar_carga_datos()
        self._conectar_comparacion()
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

    def _conectar_comparacion(self):
        self.pushButton_comparar.clicked.connect(self._comparar)

    def _comparar(self):
        cab1, filas1 = leer_qtable(self.tableWidget_datos1)
        cab2, filas2 = leer_qtable(self.tableWidget_datos2)
        if not filas1 or not filas2:
            QMessageBox.warning(
                self,
                "Comparar",
                "Carga datos en ambas tablas antes de comparar.",
            )
            return
        elegido = DialogoCampos.elegir(
            self,
            cab1,
            cab2,
            len(filas1),
            len(filas2),
            str(getattr(self, "archivo_datos1", "Datos 1") or "Datos 1"),
            str(getattr(self, "archivo_datos2", "Datos 2") or "Datos 2"),
        )
        if elegido is None:
            return
        idx1, idx2, opts = elegido
        pares = comparar_por_campos(
            filas1,
            idx1,
            filas2,
            idx2,
            case_sensitive=opts.get("case_sensitive", False),
            strip=opts.get("strip", True),
        )
        mostrar_coincidencias(
            self.tableWidget_coincidencias,
            cab1,
            filas1,
            cab2,
            filas2,
            pares,
            idx1,
            idx2,
        )
        self.tableWidget_coincidencias.setToolTip(
            f"{len(pares)} coincidencias: {cab1[idx1]} <-> {cab2[idx2]}"
        )
        QMessageBox.information(
            self,
            "Comparar",
            f"{len(pares)} coincidencias.\n"
            f"D1[{cab1[idx1]}] <-> D2[{cab2[idx2]}]\n"
            "Cargadas en Coincidencias (fila D1 y debajo su par D2).",
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
