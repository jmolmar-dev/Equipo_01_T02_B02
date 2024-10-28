# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_equipo_1_modificada.ui'
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
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_ventana_registro(object):
    def setupUi(self, Registro_Equipo_1):
        if not Registro_Equipo_1.objectName():
            Registro_Equipo_1.setObjectName(u"Registro_Equipo_1")
        Registro_Equipo_1.resize(571, 708)
        Registro_Equipo_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Registro_Equipo_1.setAutoFillBackground(False)
        Registro_Equipo_1.setStyleSheet(u"background-color: rgb(147, 181, 255);\n"
"font: 11pt  \"Verdana\";")
        Registro_Equipo_1.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionAbrir = QAction(Registro_Equipo_1)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(Registro_Equipo_1)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGuardar_Como = QAction(Registro_Equipo_1)
        self.actionGuardar_Como.setObjectName(u"actionGuardar_Como")
        self.actionSalir = QAction(Registro_Equipo_1)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionDeshacer = QAction(Registro_Equipo_1)
        self.actionDeshacer.setObjectName(u"actionDeshacer")
        self.actionRehacer = QAction(Registro_Equipo_1)
        self.actionRehacer.setObjectName(u"actionRehacer")
        self.actionCortar = QAction(Registro_Equipo_1)
        self.actionCortar.setObjectName(u"actionCortar")
        self.actionCopiar = QAction(Registro_Equipo_1)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionPegar = QAction(Registro_Equipo_1)
        self.actionPegar.setObjectName(u"actionPegar")
        self.actionZoom_in = QAction(Registro_Equipo_1)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_out = QAction(Registro_Equipo_1)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionDocumentacion = QAction(Registro_Equipo_1)
        self.actionDocumentacion.setObjectName(u"actionDocumentacion")
        self.actionAbout = QAction(Registro_Equipo_1)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(Registro_Equipo_1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton_crear_cuenta = QPushButton(self.centralwidget)
        self.boton_crear_cuenta.setObjectName(u"boton_crear_cuenta")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_crear_cuenta.sizePolicy().hasHeightForWidth())
        self.boton_crear_cuenta.setSizePolicy(sizePolicy)
        self.boton_crear_cuenta.setMinimumSize(QSize(460, 51))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.boton_crear_cuenta.setFont(font)
        self.boton_crear_cuenta.setStyleSheet(u"background-color: rgb(140, 255, 255);")
        self.boton_crear_cuenta.setCheckable(False)
        self.boton_crear_cuenta.setChecked(False)

        self.gridLayout.addWidget(self.boton_crear_cuenta, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_info_2 = QLabel(self.centralwidget)
        self.label_info_2.setObjectName(u"label_info_2")
        self.label_info_2.setMinimumSize(QSize(170, 30))
        self.label_info_2.setMaximumSize(QSize(170, 30))
        self.label_info_2.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.horizontalLayout.addWidget(self.label_info_2)

        self.boton_login = QPushButton(self.centralwidget)
        self.boton_login.setObjectName(u"boton_login")
        self.boton_login.setMinimumSize(QSize(150, 30))
        self.boton_login.setMaximumSize(QSize(150, 30))
        self.boton_login.setStyleSheet(u"background-color: rgb(140, 255, 255);")

        self.horizontalLayout.addWidget(self.boton_login)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.label_campo_email = QLabel(self.centralwidget)
        self.label_campo_email.setObjectName(u"label_campo_email")
        self.label_campo_email.setMinimumSize(QSize(121, 51))
        self.label_campo_email.setMaximumSize(QSize(121, 51))
        self.label_campo_email.setFont(font)
        self.label_campo_email.setAutoFillBackground(False)
        self.label_campo_email.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_campo_email)

        self.email_valor = QLineEdit(self.centralwidget)
        self.email_valor.setObjectName(u"email_valor")
        self.email_valor.setMinimumSize(QSize(161, 51))
        self.email_valor.setMaximumSize(QSize(161, 51))
        self.email_valor.setFont(font)
        self.email_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.email_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.email_valor)

        self.label_campo_usuario = QLabel(self.centralwidget)
        self.label_campo_usuario.setObjectName(u"label_campo_usuario")
        self.label_campo_usuario.setMinimumSize(QSize(121, 51))
        self.label_campo_usuario.setMaximumSize(QSize(121, 51))
        self.label_campo_usuario.setFont(font)
        self.label_campo_usuario.setAutoFillBackground(False)
        self.label_campo_usuario.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_campo_usuario)

        self.usuario_valor = QLineEdit(self.centralwidget)
        self.usuario_valor.setObjectName(u"usuario_valor")
        self.usuario_valor.setMinimumSize(QSize(161, 51))
        self.usuario_valor.setMaximumSize(QSize(161, 51))
        self.usuario_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.usuario_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usuario_valor)

        self.label_campo_password_registro = QLabel(self.centralwidget)
        self.label_campo_password_registro.setObjectName(u"label_campo_password_registro")
        self.label_campo_password_registro.setMinimumSize(QSize(121, 51))
        self.label_campo_password_registro.setMaximumSize(QSize(121, 51))
        self.label_campo_password_registro.setFont(font)
        self.label_campo_password_registro.setAutoFillBackground(False)
        self.label_campo_password_registro.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_campo_password_registro)

        self.password_valor = QLineEdit(self.centralwidget)
        self.password_valor.setObjectName(u"password_valor")
        self.password_valor.setMinimumSize(QSize(161, 51))
        self.password_valor.setMaximumSize(QSize(161, 51))
        self.password_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.password_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.password_valor.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.password_valor)

        self.label_confirmar_password = QLabel(self.centralwidget)
        self.label_confirmar_password.setObjectName(u"label_confirmar_password")
        self.label_confirmar_password.setFont(font)
        self.label_confirmar_password.setAutoFillBackground(False)
        self.label_confirmar_password.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_confirmar_password)

        self.password_confirmada_valor = QLineEdit(self.centralwidget)
        self.password_confirmada_valor.setObjectName(u"password_confirmada_valor")
        self.password_confirmada_valor.setMinimumSize(QSize(161, 51))
        self.password_confirmada_valor.setMaximumSize(QSize(161, 51))
        self.password_confirmada_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.password_confirmada_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.password_confirmada_valor.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_confirmada_valor)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        sizePolicy.setHeightForWidth(self.label_titulo.sizePolicy().hasHeightForWidth())
        self.label_titulo.setSizePolicy(sizePolicy)
        self.label_titulo.setMinimumSize(QSize(67, 160))
        self.label_titulo.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"font-size:20pt;")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 1)

        Registro_Equipo_1.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Registro_Equipo_1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 33))
        self.menubar.setStyleSheet(u"color: rgb(59, 182, 111 );")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuArchivo.setStyleSheet(u"color: rgb(59, 182, 111 );")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuEditar.setStyleSheet(u"color: rgb(59, 182, 111);")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName(u"menuVista")
        self.menuVista.setStyleSheet(u"color: rgb(59, 182, 111);")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuAyuda.setStyleSheet(u"color: rgb(59, 182, 111);")
        Registro_Equipo_1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Registro_Equipo_1)
        self.statusbar.setObjectName(u"statusbar")
        Registro_Equipo_1.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionRehacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionPegar)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionZoom_out)
        self.menuAyuda.addAction(self.actionDocumentacion)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAbout)

        self.retranslateUi(Registro_Equipo_1)

        QMetaObject.connectSlotsByName(Registro_Equipo_1)
    # setupUi

    def retranslateUi(self, Registro_Equipo_1):
        Registro_Equipo_1.setWindowTitle(QCoreApplication.translate("ventana_registro", u"Ventana Inicio Sesion", None))
        self.actionAbrir.setText(QCoreApplication.translate("ventana_registro", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("ventana_registro", u"Guardar", None))
        self.actionGuardar_Como.setText(QCoreApplication.translate("ventana_registro", u"Guardar Como", None))
        self.actionSalir.setText(QCoreApplication.translate("ventana_registro", u"Salir", None))
        self.actionDeshacer.setText(QCoreApplication.translate("ventana_registro", u"Deshacer", None))
        self.actionRehacer.setText(QCoreApplication.translate("ventana_registro", u"Rehacer", None))
        self.actionCortar.setText(QCoreApplication.translate("ventana_registro", u"Cortar", None))
        self.actionCopiar.setText(QCoreApplication.translate("ventana_registro", u"Copiar", None))
        self.actionPegar.setText(QCoreApplication.translate("ventana_registro", u"Pegar", None))
        self.actionZoom_in.setText(QCoreApplication.translate("ventana_registro", u"Zoom in", None))
        self.actionZoom_out.setText(QCoreApplication.translate("ventana_registro", u"Zoom out", None))
        self.actionDocumentacion.setText(QCoreApplication.translate("ventana_registro", u"Documentacion", None))
        self.actionAbout.setText(QCoreApplication.translate("ventana_registro", u"About", None))
        self.boton_crear_cuenta.setText(QCoreApplication.translate("ventana_registro", u"Crear Cuenta", None))
        self.label_info_2.setText(QCoreApplication.translate("ventana_registro", u"\u00bfYa tiene una cuenta?", None))
        self.boton_login.setText(QCoreApplication.translate("ventana_registro", u"Login", None))
        self.label_campo_email.setText(QCoreApplication.translate("ventana_registro", u"Email", None))
        self.email_valor.setText(QCoreApplication.translate("ventana_registro", u"lorenzo29@gmail.com", None))
        self.label_campo_usuario.setText(QCoreApplication.translate("ventana_registro", u"Usuario", None))
        self.usuario_valor.setText(QCoreApplication.translate("ventana_registro", u"lorenzo29", None))
        self.label_campo_password_registro.setText(QCoreApplication.translate("ventana_registro", u"Contrase\u00f1a", None))
        self.password_valor.setText(QCoreApplication.translate("ventana_registro", u"duhfhuhdufh", None))
        self.label_confirmar_password.setText(QCoreApplication.translate("ventana_registro", u"Confirmar Contrase\u00f1a", None))
        self.password_confirmada_valor.setText(QCoreApplication.translate("ventana_registro", u"duhfhuhdufh", None))
        self.label_titulo.setText(QCoreApplication.translate("ventana_registro", u"Registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("ventana_registro", u"Archivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("ventana_registro", u"Editar", None))
        self.menuVista.setTitle(QCoreApplication.translate("ventana_registro", u"Vista", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("ventana_registro", u"Ayuda", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear una instancia de QApplication
    mainWindow = QMainWindow()    # Crear una instancia de QMainWindow
    ui = Ui_ventana_registro()     # Crear la instancia de la interfaz
    ui.setupUi(mainWindow)         # Configurar la interfaz en la ventana principal
    mainWindow.show()              # Mostrar la ventana
    sys.exit(app.exec())           # Ejecutar el bucle de eventos
