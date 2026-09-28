# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(993, 793)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_5, 1, 5, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_6, 1, 4, 1, 1)

        self.tableWidget_origen = QTableWidget(self.frame_2)
        self.tableWidget_origen.setObjectName(u"tableWidget_origen")
        self.tableWidget_origen.setStyleSheet(u"background-color: qconicalgradient(cx:0.0686818, cy:0.063, angle:135.2, stop:0.125 rgba(0, 36, 255, 107), stop:0.375 rgba(0, 135, 255, 69), stop:0.423533 rgba(0, 189, 255, 145), stop:0.45 rgba(0, 168, 255, 208), stop:0.477581 rgba(71, 137, 255, 130), stop:0.518717 rgba(71, 192, 255, 130), stop:0.55 rgba(0, 135, 255, 255), stop:0.57754 rgba(0, 135, 255, 130), stop:0.625 rgba(0, 124, 255, 69), stop:1 rgba(0, 113, 255, 197));")

        self.gridLayout_6.addWidget(self.tableWidget_origen, 0, 0, 1, 6)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 5, 1, 1)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 3, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.tableWidget_destino = QTableWidget(self.frame_3)
        self.tableWidget_destino.setObjectName(u"tableWidget_destino")
        self.tableWidget_destino.setStyleSheet(u"background-color: qconicalgradient(cx:0.938, cy:0.0576818, angle:44.896, stop:0.125 rgba(0, 36, 255, 107), stop:0.375 rgba(0, 135, 255, 69), stop:0.423533 rgba(0, 189, 255, 145), stop:0.45 rgba(0, 168, 255, 208), stop:0.477581 rgba(71, 137, 255, 130), stop:0.518717 rgba(71, 192, 255, 130), stop:0.55 rgba(0, 135, 255, 255), stop:0.57754 rgba(0, 135, 255, 130), stop:0.625 rgba(0, 124, 255, 69), stop:1 rgba(0, 113, 255, 197));")

        self.gridLayout_5.addWidget(self.tableWidget_destino, 0, 0, 1, 6)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 1, 4, 1, 1)

        self.line_7 = QFrame(self.frame_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_7, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_8, 1, 4, 1, 1)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_3, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.pushButton_4, 1, 5, 1, 1)

        self.tableWidget_coincidencias = QTableWidget(self.frame_6)
        self.tableWidget_coincidencias.setObjectName(u"tableWidget_coincidencias")
        self.tableWidget_coincidencias.setStyleSheet(u"background-color: qconicalgradient(cx:0.0681818, cy:0.927, angle:223.1, stop:0.125 rgba(0, 36, 255, 107), stop:0.375 rgba(0, 135, 255, 69), stop:0.423533 rgba(0, 189, 255, 145), stop:0.45 rgba(0, 168, 255, 208), stop:0.477581 rgba(71, 137, 255, 130), stop:0.518717 rgba(71, 192, 255, 130), stop:0.55 rgba(0, 135, 255, 255), stop:0.57754 rgba(0, 135, 255, 130), stop:0.625 rgba(0, 124, 255, 69), stop:1 rgba(0, 113, 255, 197));")

        self.gridLayout_7.addWidget(self.tableWidget_coincidencias, 0, 0, 1, 6)

        self.line_5 = QFrame(self.frame_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_5, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    /* Gradiente invertido suave en tonos plata/aluminio (simula profundidad fija) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(200, 202, 205), \n"
"                                      stop:1 rgb(230, 232, 235));\n"
"    /* Texto negro para m\u00e1xima legibilidad sobre fondo claro */\n"
"    color: #000000; \n"
"    \n"
"    /* Bordes rectos hundidos adaptados a la paleta clara */\n"
"    border-top: 2px solid #757a80;\n"
"    border-left: 2px solid #90959a;\n"
"    border-right: 1px solid #ffffff;\n"
"    border-bottom: 1px solid #ffffff;\n"
"    \n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_9, 1, 4, 1, 1)

        self.tableWidget_faltantes = QTableWidget(self.frame_9)
        self.tableWidget_faltantes.setObjectName(u"tableWidget_faltantes")
        self.tableWidget_faltantes.setStyleSheet(u"background-color: qconicalgradient(cx:0.915, cy:0.932682, angle:312.7, stop:0.125 rgba(0, 36, 255, 107), stop:0.375 rgba(0, 135, 255, 69), stop:0.423533 rgba(0, 189, 255, 145), stop:0.45 rgba(0, 168, 255, 208), stop:0.477581 rgba(71, 137, 255, 130), stop:0.518717 rgba(71, 192, 255, 130), stop:0.55 rgba(0, 135, 255, 255), stop:0.57754 rgba(0, 135, 255, 130), stop:0.625 rgba(0, 124, 255, 69), stop:1 rgba(0, 113, 255, 197));")

        self.gridLayout_8.addWidget(self.tableWidget_faltantes, 0, 0, 1, 6)

        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    /* Gradiente de acero oscuro pulido (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(90, 95, 100), \n"
"                                      stop:1 rgb(60, 65, 70));\n"
"    /* Texto blanco para contrastar fuertemente con el bot\u00f3n oscuro */\n"
"    color: #ffffff;\n"
"    /* Borde sutil pero definido */\n"
"    border: 1px solid #14191f;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Destello met\u00e1lico: se aclara notablemente al pasar el mouse */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(120, 125, 130), \n"
"                                      stop:1 rgb(80, 85, 90));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Efecto hundido extremo (casi negro mate) */\n"
"    background-color: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(40, 45, 50), \n"
"                                      stop:1 rgb(55, 60, 65));\n"
"    border: 2px solid #14191f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Gris apagado gen\u00e9rico para deshabilitado */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a0a5a8, stop:1 #858a8d);\n"
"    color: #d1d5d8;\n"
"    border: 1px solid #7f8c8d;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.pushButton_3, 1, 5, 1, 1)

        self.line_4 = QFrame(self.frame_9)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_4, 1, 3, 1, 1)

        self.line_8 = QFrame(self.frame_9)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_8, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tableWidget_origen, self.tableWidget_destino)
        QWidget.setTabOrder(self.tableWidget_destino, self.tableWidget_faltantes)
        QWidget.setTabOrder(self.tableWidget_faltantes, self.tableWidget_coincidencias)
        QWidget.setTabOrder(self.tableWidget_coincidencias, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cotejo de Datos", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

