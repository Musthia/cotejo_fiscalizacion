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
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1202, 842)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/ico/Datcorr.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-image: url(:/ico/image (1).png);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_datos2 = QTableWidget(self.frame_3)
        self.tableWidget_datos2.setObjectName(u"tableWidget_datos2")
        self.tableWidget_datos2.setStyleSheet(u"background-color: rgb(172, 240, 255);")

        self.gridLayout_3.addWidget(self.tableWidget_datos2, 0, 0, 1, 3)

        self.pushButton_datos_db_2 = QPushButton(self.frame_3)
        self.pushButton_datos_db_2.setObjectName(u"pushButton_datos_db_2")
        self.pushButton_datos_db_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_db_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_datos_db_2, 2, 0, 1, 1)

        self.pushButton_datos_excel_2 = QPushButton(self.frame_3)
        self.pushButton_datos_excel_2.setObjectName(u"pushButton_datos_excel_2")
        self.pushButton_datos_excel_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_excel_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_datos_excel_2, 1, 0, 1, 1)

        self.pushButton_nomb_archiv_2 = QPushButton(self.frame_3)
        self.pushButton_nomb_archiv_2.setObjectName(u"pushButton_nomb_archiv_2")
        self.pushButton_nomb_archiv_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_nomb_archiv_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_nomb_archiv_2, 2, 2, 1, 1)

        self.pushButton_datos_csv_2 = QPushButton(self.frame_3)
        self.pushButton_datos_csv_2.setObjectName(u"pushButton_datos_csv_2")
        self.pushButton_datos_csv_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_csv_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_datos_csv_2, 1, 1, 1, 1)

        self.pushButton_datos_txt_2 = QPushButton(self.frame_3)
        self.pushButton_datos_txt_2.setObjectName(u"pushButton_datos_txt_2")
        self.pushButton_datos_txt_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_txt_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_datos_txt_2, 1, 2, 1, 1)

        self.pushButton_datos_acces_2 = QPushButton(self.frame_3)
        self.pushButton_datos_acces_2.setObjectName(u"pushButton_datos_acces_2")
        self.pushButton_datos_acces_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_acces_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_datos_acces_2, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_faltantes = QTableWidget(self.frame_9)
        self.tableWidget_faltantes.setObjectName(u"tableWidget_faltantes")
        self.tableWidget_faltantes.setStyleSheet(u"background-color: rgb(172, 240, 255);")

        self.gridLayout_6.addWidget(self.tableWidget_faltantes, 0, 0, 1, 4)

        self.line_4 = QFrame(self.frame_9)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_4, 1, 2, 1, 1)

        self.line_8 = QFrame(self.frame_9)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_8, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.pushButton_export_falt = QPushButton(self.frame_9)
        self.pushButton_export_falt.setObjectName(u"pushButton_export_falt")
        self.pushButton_export_falt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_export_falt.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_export_falt, 1, 0, 1, 1)

        self.label_2_info = QLabel(self.frame_9)
        self.label_2_info.setObjectName(u"label_2_info")
        sizePolicy.setHeightForWidth(self.label_2_info.sizePolicy().hasHeightForWidth())
        self.label_2_info.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_2_info, 2, 0, 1, 4)


        self.gridLayout_2.addWidget(self.frame_9, 3, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_datos1 = QTableWidget(self.frame_2)
        self.tableWidget_datos1.setObjectName(u"tableWidget_datos1")
        self.tableWidget_datos1.setStyleSheet(u"background-color: rgb(172, 240, 255);")

        self.gridLayout_4.addWidget(self.tableWidget_datos1, 0, 0, 1, 3)

        self.pushButton_datos_acces = QPushButton(self.frame_2)
        self.pushButton_datos_acces.setObjectName(u"pushButton_datos_acces")
        self.pushButton_datos_acces.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_acces.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_datos_acces, 2, 1, 1, 1)

        self.pushButton_datos_db = QPushButton(self.frame_2)
        self.pushButton_datos_db.setObjectName(u"pushButton_datos_db")
        self.pushButton_datos_db.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_db.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_datos_db, 2, 0, 1, 1)

        self.pushButton_datos_txt = QPushButton(self.frame_2)
        self.pushButton_datos_txt.setObjectName(u"pushButton_datos_txt")
        self.pushButton_datos_txt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_txt.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_datos_txt, 1, 2, 1, 1)

        self.pushButton_nomb_archiv = QPushButton(self.frame_2)
        self.pushButton_nomb_archiv.setObjectName(u"pushButton_nomb_archiv")
        self.pushButton_nomb_archiv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_nomb_archiv.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_nomb_archiv, 2, 2, 1, 1)

        self.pushButton_datos_csv = QPushButton(self.frame_2)
        self.pushButton_datos_csv.setObjectName(u"pushButton_datos_csv")
        self.pushButton_datos_csv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_csv.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_datos_csv, 1, 1, 1, 1)

        self.pushButton_datos_excel = QPushButton(self.frame_2)
        self.pushButton_datos_excel.setObjectName(u"pushButton_datos_excel")
        self.pushButton_datos_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_datos_excel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_datos_excel.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_datos_excel, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_1_info = QLabel(self.frame_6)
        self.label_1_info.setObjectName(u"label_1_info")
        sizePolicy.setHeightForWidth(self.label_1_info.sizePolicy().hasHeightForWidth())
        self.label_1_info.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_1_info, 4, 0, 1, 4)

        self.line_5 = QFrame(self.frame_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 1, 2, 1, 1)

        self.tableWidget_coincidencias = QTableWidget(self.frame_6)
        self.tableWidget_coincidencias.setObjectName(u"tableWidget_coincidencias")
        self.tableWidget_coincidencias.setStyleSheet(u"background-color: rgb(172, 240, 255);")

        self.gridLayout_5.addWidget(self.tableWidget_coincidencias, 0, 0, 1, 4)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.tableWidget_parciales = QTableWidget(self.frame_6)
        self.tableWidget_parciales.setObjectName(u"tableWidget_parciales")
        self.tableWidget_parciales.setStyleSheet(u"background-color: rgb(172, 240, 255);")

        self.gridLayout_5.addWidget(self.tableWidget_parciales, 2, 0, 1, 4)

        self.pushButton_export_coinc = QPushButton(self.frame_6)
        self.pushButton_export_coinc.setObjectName(u"pushButton_export_coinc")
        self.pushButton_export_coinc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_export_coinc.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_export_coinc, 1, 0, 1, 1)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 1, 1, 1)

        self.pushButton_export_parciales = QPushButton(self.frame_6)
        self.pushButton_export_parciales.setObjectName(u"pushButton_export_parciales")
        self.pushButton_export_parciales.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_export_parciales.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_export_parciales, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_5, 3, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 1)

        self.pushButton_comparar = QPushButton(self.frame)
        self.pushButton_comparar.setObjectName(u"pushButton_comparar")
        self.pushButton_comparar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_comparar.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(15, 25, 40), \n"
"                                      stop:1 rgb(25, 35, 50));\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_comparar, 1, 0, 1, 2)

        self.pushButton_limpiar_todo = QPushButton(self.frame)
        self.pushButton_limpiar_todo.setObjectName(u"pushButton_limpiar_todo")
        self.pushButton_limpiar_todo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_limpiar_todo.setStyleSheet(u"QPushButton {\n"
"    /* Base de acero azul oscuro profundo (volumen hacia afuera) */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(50, 65, 85), \n"
"                                      stop:1 rgb(30, 40, 55));\n"
"    color: #FFFFFF;\n"
"    /* Borde oscuro con reflejo superior azul brillante */\n"
"    border: 1px solid #0b111a;\n"
"    border-top: 1px solid #6391c2; \n"
"    border-radius: 6px;\n"
"    padding: 7px 14px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* El azul base se enciende e intensifica notablemente */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                      stop:0 rgb(80, 110, 145), \n"
"                                      stop:1 rgb(45, 65, 90));\n"
"    /* Texto cian brillante para m\u00e1ximo contraste en hover */\n"
"    color: #3ae2ff;\n"
"    /* Bordes el\u00e9ctricos integrados */\n"
"    border: 1px so"
                        "lid #163654;\n"
"    border-top: 1px solid #5cb3ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Hundimiento extremo en azul marino casi negro */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                     stop:0 #D2DC00, \n"
"                                      stop:1 #E2E8F0);\n"
"    color: #00bfff;\n"
"    border: 1px solid #050b14;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* Desaturado completo (gris ligeramente fr\u00edo) para indicar inactividad */\n"
"    background-color: #4b525a;\n"
"    color: #828a94;\n"
"    border: 1px solid #363b40;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_limpiar_todo, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tableWidget_datos1, self.tableWidget_datos2)
        QWidget.setTabOrder(self.tableWidget_datos2, self.tableWidget_faltantes)
        QWidget.setTabOrder(self.tableWidget_faltantes, self.tableWidget_coincidencias)
        QWidget.setTabOrder(self.tableWidget_coincidencias, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cotejo de Datos", None))
        self.pushButton_datos_db_2.setText(QCoreApplication.translate("MainWindow", u"BASES DE DATOS", None))
        self.pushButton_datos_excel_2.setText(QCoreApplication.translate("MainWindow", u"DATOS EN EXCEL", None))
        self.pushButton_nomb_archiv_2.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE ARCHIVOS", None))
        self.pushButton_datos_csv_2.setText(QCoreApplication.translate("MainWindow", u"DATSOS EN CSV", None))
        self.pushButton_datos_txt_2.setText(QCoreApplication.translate("MainWindow", u"DATOS EN TXT", None))
        self.pushButton_datos_acces_2.setText(QCoreApplication.translate("MainWindow", u"DATOS EN ACCES", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_export_falt.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.label_2_info.setText("")
        self.pushButton_datos_acces.setText(QCoreApplication.translate("MainWindow", u"DATOS EN ACCES", None))
        self.pushButton_datos_db.setText(QCoreApplication.translate("MainWindow", u"BASES DE DATOS", None))
        self.pushButton_datos_txt.setText(QCoreApplication.translate("MainWindow", u"DATCOS EN TXT", None))
        self.pushButton_nomb_archiv.setText(QCoreApplication.translate("MainWindow", u"NOMBRES DE ARCHIVOS", None))
        self.pushButton_datos_csv.setText(QCoreApplication.translate("MainWindow", u"DATCOS EN CSV", None))
        self.pushButton_datos_excel.setText(QCoreApplication.translate("MainWindow", u"DATOS EN EXCEL", None))
        self.label_1_info.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_export_coinc.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.pushButton_export_parciales.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_comparar.setText(QCoreApplication.translate("MainWindow", u"COMPARAR", None))
        self.pushButton_limpiar_todo.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR TABLAS", None))
    # retranslateUi

