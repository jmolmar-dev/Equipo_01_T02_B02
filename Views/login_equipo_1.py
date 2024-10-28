# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_equipo_1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_Login_Equipo_1(object):
    def setupUi(self, Login_Equipo_1):
        if not Login_Equipo_1.objectName():
            Login_Equipo_1.setObjectName(u"Login_Equipo_1")
        Login_Equipo_1.resize(480, 620)
        Login_Equipo_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Login_Equipo_1.setAutoFillBackground(False)
        Login_Equipo_1.setStyleSheet(u"background-color: rgb(5, 13, 33);\n"
"font: 10pt \"Arial\";")
        Login_Equipo_1.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionpepe = QAction(Login_Equipo_1)
        self.actionpepe.setObjectName(u"actionpepe")
        self.actionSalir = QAction(Login_Equipo_1)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionGuardar = QAction(Login_Equipo_1)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGuardar_Como = QAction(Login_Equipo_1)
        self.actionGuardar_Como.setObjectName(u"actionGuardar_Como")
        self.actionEditar = QAction(Login_Equipo_1)
        self.actionEditar.setObjectName(u"actionEditar")
        self.actionDeshacer = QAction(Login_Equipo_1)
        self.actionDeshacer.setObjectName(u"actionDeshacer")
        self.actionReahacer = QAction(Login_Equipo_1)
        self.actionReahacer.setObjectName(u"actionReahacer")
        self.actionCortar = QAction(Login_Equipo_1)
        self.actionCortar.setObjectName(u"actionCortar")
        self.actionCopiar = QAction(Login_Equipo_1)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionZoom_in = QAction(Login_Equipo_1)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_out = QAction(Login_Equipo_1)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionDocumentacion = QAction(Login_Equipo_1)
        self.actionDocumentacion.setObjectName(u"actionDocumentacion")
        self.actionAbout = QAction(Login_Equipo_1)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentacion_2 = QAction(Login_Equipo_1)
        self.actionDocumentacion_2.setObjectName(u"actionDocumentacion_2")
        self.actionAbout_2 = QAction(Login_Equipo_1)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.actionPegar = QAction(Login_Equipo_1)
        self.actionPegar.setObjectName(u"actionPegar")
        self.centralwidget = QWidget(Login_Equipo_1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout2 = QHBoxLayout()
        self.layout2.setSpacing(6)
        self.layout2.setObjectName(u"layout2")
        self.layout2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(158, 30))
        self.info.setMaximumSize(QSize(158, 30))
        self.info.setStyleSheet(u"color: rgb(201, 213, 238);")

        self.layout2.addWidget(self.info)

        self.button_login_1 = QPushButton(self.centralwidget)
        self.button_login_1.setObjectName(u"button_login_1")
        self.button_login_1.setMinimumSize(QSize(157, 23))
        self.button_login_1.setMaximumSize(QSize(157, 23))
        self.button_login_1.setStyleSheet(u"background-color: rgb(26, 103, 248);")

        


        self.gridLayout.addLayout(self.layout2, 2, 0, 1, 1)

        self.button_login_2 = QPushButton(self.centralwidget)
        self.button_login_2.setObjectName(u"button_login_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_login_2.sizePolicy().hasHeightForWidth())
        self.button_login_2.setSizePolicy(sizePolicy)
        self.button_login_2.setMinimumSize(QSize(460, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.button_login_2.setFont(font)
        self.button_login_2.setStyleSheet(u"background-color: rgb(26, 103, 248);\n"
"")
        self.button_login_2.setCheckable(False)
        self.button_login_2.setChecked(False)

        self.gridLayout.addWidget(self.button_login_2, 3, 0, 1, 1)

        self.titulo_main = QLabel(self.centralwidget)
        self.titulo_main.setObjectName(u"titulo_main")
        self.titulo_main.setMinimumSize(QSize(67, 160))
        self.titulo_main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titulo_main.setStyleSheet(u"color: rgb(201, 213, 238);\n"
" font-size:20pt;\n"
"")
        self.titulo_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.titulo_main, 0, 0, 1, 1)

        self.layout1 = QFormLayout()
        self.layout1.setObjectName(u"layout1")
        self.layout1.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout1.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout1.setHorizontalSpacing(20)
        self.layout1.setVerticalSpacing(20)
        self.titulo_usuario = QLabel(self.centralwidget)
        self.titulo_usuario.setObjectName(u"titulo_usuario")
        self.titulo_usuario.setMinimumSize(QSize(121, 51))
        self.titulo_usuario.setMaximumSize(QSize(121, 51))
        self.titulo_usuario.setFont(font)
        self.titulo_usuario.setAutoFillBackground(False)
        self.titulo_usuario.setStyleSheet(u"color: rgb(201, 213, 238);")

        self.layout1.setWidget(0, QFormLayout.LabelRole, self.titulo_usuario)

        self.campo_usuario = QLineEdit(self.centralwidget)
        self.campo_usuario.setObjectName(u"campo_usuario")
        self.campo_usuario.setMinimumSize(QSize(161, 51))
        self.campo_usuario.setMaximumSize(QSize(161, 51))
        self.campo_usuario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.campo_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout1.setWidget(0, QFormLayout.FieldRole, self.campo_usuario)

        self.titulo_password = QLabel(self.centralwidget)
        self.titulo_password.setObjectName(u"titulo_password")
        self.titulo_password.setMinimumSize(QSize(121, 51))
        self.titulo_password.setMaximumSize(QSize(121, 51))
        self.titulo_password.setFont(font)
        self.titulo_password.setAutoFillBackground(False)
        self.titulo_password.setStyleSheet(u"color: rgb(201, 213, 238);")

        self.layout1.setWidget(1, QFormLayout.LabelRole, self.titulo_password)

        self.campo_password = QLineEdit(self.centralwidget)
        self.campo_password.setObjectName(u"campo_password")
        self.campo_password.setMinimumSize(QSize(161, 51))
        self.campo_password.setMaximumSize(QSize(161, 51))
        self.campo_password.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.campo_password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.campo_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.layout1.setWidget(1, QFormLayout.FieldRole, self.campo_password)


        self.gridLayout.addLayout(self.layout1, 1, 0, 1, 1)

        Login_Equipo_1.setCentralWidget(self.centralwidget)
        self.titulo_main.raise_()
        self.button_login_2.raise_()
        self.menubar = QMenuBar(Login_Equipo_1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 33))
        self.menubar.setStyleSheet(u"color: rgb(201, 213, 238);")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuEditar.setStyleSheet(u"color: rgb(201, 213, 238);")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName(u"menuVista")
        self.menuVista.setStyleSheet(u"color: rgb(201, 213, 238);")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuArchivo.setStyleSheet(u"color: rgb(201, 213, 238);")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuAyuda.setStyleSheet(u"color: rgb(201, 213, 238);")
        Login_Equipo_1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login_Equipo_1)
        self.statusbar.setObjectName(u"statusbar")
        Login_Equipo_1.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionReahacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionPegar)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionZoom_out)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionEditar)
        self.menuAyuda.addAction(self.actionDocumentacion_2)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAbout_2)

        self.retranslateUi(Login_Equipo_1)

        QMetaObject.connectSlotsByName(Login_Equipo_1)
    # setupUi

    def retranslateUi(self, Login_Equipo_1):
        Login_Equipo_1.setWindowTitle(QCoreApplication.translate("Login_Equipo_1", u"Login_Equipo_1", None))
        self.actionpepe.setText(QCoreApplication.translate("Login_Equipo_1", u"pepe", None))
        self.actionSalir.setText(QCoreApplication.translate("Login_Equipo_1", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("Login_Equipo_1", u"Guardar", None))
        self.actionGuardar_Como.setText(QCoreApplication.translate("Login_Equipo_1", u"Guardar Como", None))
        self.actionEditar.setText(QCoreApplication.translate("Login_Equipo_1", u"Salir", None))
        self.actionDeshacer.setText(QCoreApplication.translate("Login_Equipo_1", u"Deshacer", None))
        self.actionReahacer.setText(QCoreApplication.translate("Login_Equipo_1", u"Reahacer", None))
        self.actionCortar.setText(QCoreApplication.translate("Login_Equipo_1", u"Cortar", None))
        self.actionCopiar.setText(QCoreApplication.translate("Login_Equipo_1", u"Copiar", None))
        self.actionZoom_in.setText(QCoreApplication.translate("Login_Equipo_1", u"Zoom in", None))
        self.actionZoom_out.setText(QCoreApplication.translate("Login_Equipo_1", u"Zoom out", None))
        self.actionDocumentacion.setText(QCoreApplication.translate("Login_Equipo_1", u"Documentacion", None))
        self.actionAbout.setText(QCoreApplication.translate("Login_Equipo_1", u"About", None))
        self.actionDocumentacion_2.setText(QCoreApplication.translate("Login_Equipo_1", u"Documentacion", None))
        self.actionAbout_2.setText(QCoreApplication.translate("Login_Equipo_1", u"About", None))
        self.actionPegar.setText(QCoreApplication.translate("Login_Equipo_1", u"Pegar", None))
        self.info.setText(QCoreApplication.translate("Login_Equipo_1", u"\u00bfNo tiene una cuenta?", None))
        self.button_login_1.setText(QCoreApplication.translate("Login_Equipo_1", u"Crear Cuenta", None))
        self.button_login_2.setText(QCoreApplication.translate("Login_Equipo_1", u"Login", None))
        self.titulo_main.setText(QCoreApplication.translate("Login_Equipo_1", u"Login", None))
        self.titulo_usuario.setText(QCoreApplication.translate("Login_Equipo_1", u"Usuario", None))
        self.campo_usuario.setText(QCoreApplication.translate("Login_Equipo_1", u"lorenzo29", None))
        self.titulo_password.setText(QCoreApplication.translate("Login_Equipo_1", u"Contrase\u00f1a", None))
        self.campo_password.setText(QCoreApplication.translate("Login_Equipo_1", u"duhfhuhdufh", None))
        self.menuEditar.setTitle(QCoreApplication.translate("Login_Equipo_1", u"Editar", None))
        self.menuVista.setTitle(QCoreApplication.translate("Login_Equipo_1", u"Vista", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("Login_Equipo_1", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("Login_Equipo_1", u"Ayuda", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear una instancia de QApplication
    mainWindow = QMainWindow()    # Crear una instancia de QMainWindow
    ui = Ui_Login_Equipo_1()     # Crear la instancia de la interfaz
    ui.setupUi(mainWindow)         # Configurar la interfaz en la ventana principal
    mainWindow.show()              # Mostrar la ventana
    sys.exit(app.exec())           # Ejecutar el bucle de eventos
