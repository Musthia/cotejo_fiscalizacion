"""Nueva ventana: eleccion del campo de cada tabla a comparar.

Permite comparar mismo tipo o cruzado porque cada tabla aporta su propio
indice de columna (las estructuras pueden variar).
"""

from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class DialogoCampos(QDialog):
    def __init__(
        self,
        parent: QWidget | None = None,
        cab1: list[str] | None = None,
        cab2: list[str] | None = None,
        n1: int = 0,
        n2: int = 0,
        nombre1: str = "Datos 1",
        nombre2: str = "Datos 2",
    ):
        super().__init__(parent)
        self.setWindowTitle("Comparar: elegir campo de cada tabla")
        self.setMinimumWidth(420)

        cab1 = cab1 or []
        cab2 = cab2 or []

        layout = QVBoxLayout(self)
        layout.addWidget(
            QLabel(
                f"Tabla 1 ({nombre1}): {n1} filas, {len(cab1)} columnas. "
                f"Tabla 2 ({nombre2}): {n2} filas, {len(cab2)} columnas."
            )
        )
        form = QFormLayout()
        self.combo1 = QComboBox(self)
        for j, nombre in enumerate(cab1):
            self.combo1.addItem(f"{j + 1}. {nombre}", j)
        self.combo2 = QComboBox(self)
        for j, nombre in enumerate(cab2):
            self.combo2.addItem(f"{j + 1}. {nombre}", j)
        form.addRow("Campo de Datos 1:", self.combo1)
        form.addRow("Campo de Datos 2:", self.combo2)
        layout.addLayout(form)

        self.chk_case = QCheckBox("Distinguir mayusculas/minusculas", self)
        self.chk_case.setChecked(False)
        self.chk_strip = QCheckBox("Ignorar espacios extra", self)
        self.chk_strip.setChecked(True)
        layout.addWidget(self.chk_case)
        layout.addWidget(self.chk_strip)
        layout.addWidget(QLabel("El resultado se carga en Coincidencias: fila D1 y debajo su par D2."))

        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            self,
        )
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

    def seleccion(self) -> tuple[int, int, dict]:
        return (
            self.combo1.currentData(),
            self.combo2.currentData(),
            {
                "case_sensitive": self.chk_case.isChecked(),
                "strip": self.chk_strip.isChecked(),
            },
        )

    @classmethod
    def elegir(
        cls,
        parent: QWidget | None,
        cab1: list[str],
        cab2: list[str],
        n1: int,
        n2: int,
        nombre1: str = "Datos 1",
        nombre2: str = "Datos 2",
    ) -> tuple[int, int, dict] | None:
        if not cab1 or not cab2:
            return None
        dlg = cls(parent, cab1, cab2, n1, n2, nombre1, nombre2)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return None
        return dlg.seleccion()
