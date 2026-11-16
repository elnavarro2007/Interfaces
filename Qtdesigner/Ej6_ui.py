# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ej6.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(278, 260)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.conectar = QPushButton(self.centralwidget)
        self.conectar.setObjectName(u"conectar")

        self.horizontalLayout.addWidget(self.conectar)

        self.actualizar = QPushButton(self.centralwidget)
        self.actualizar.setObjectName(u"actualizar")

        self.horizontalLayout.addWidget(self.actualizar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.led1 = QLabel(self.centralwidget)
        self.led1.setObjectName(u"led1")

        self.horizontalLayout_2.addWidget(self.led1)

        self.on1 = QPushButton(self.centralwidget)
        self.on1.setObjectName(u"on1")

        self.horizontalLayout_2.addWidget(self.on1)

        self.off1 = QPushButton(self.centralwidget)
        self.off1.setObjectName(u"off1")

        self.horizontalLayout_2.addWidget(self.off1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.led4 = QLabel(self.centralwidget)
        self.led4.setObjectName(u"led4")

        self.horizontalLayout_3.addWidget(self.led4)

        self.on2 = QPushButton(self.centralwidget)
        self.on2.setObjectName(u"on2")

        self.horizontalLayout_3.addWidget(self.on2)

        self.off2 = QPushButton(self.centralwidget)
        self.off2.setObjectName(u"off2")

        self.horizontalLayout_3.addWidget(self.off2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.led3 = QLabel(self.centralwidget)
        self.led3.setObjectName(u"led3")

        self.horizontalLayout_4.addWidget(self.led3)

        self.on3 = QPushButton(self.centralwidget)
        self.on3.setObjectName(u"on3")

        self.horizontalLayout_4.addWidget(self.on3)

        self.off3 = QPushButton(self.centralwidget)
        self.off3.setObjectName(u"off3")

        self.horizontalLayout_4.addWidget(self.off3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.led2 = QLabel(self.centralwidget)
        self.led2.setObjectName(u"led2")

        self.horizontalLayout_5.addWidget(self.led2)

        self.on4 = QPushButton(self.centralwidget)
        self.on4.setObjectName(u"on4")

        self.horizontalLayout_5.addWidget(self.on4)

        self.off4 = QPushButton(self.centralwidget)
        self.off4.setObjectName(u"off4")

        self.horizontalLayout_5.addWidget(self.off4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 278, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Encender leds", None))
        self.conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.led1.setText(QCoreApplication.translate("MainWindow", u"Led1", None))
        self.on1.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.off1.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.led4.setText(QCoreApplication.translate("MainWindow", u"Led2", None))
        self.on2.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.off2.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.led3.setText(QCoreApplication.translate("MainWindow", u"Led3", None))
        self.on3.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.off3.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.led2.setText(QCoreApplication.translate("MainWindow", u"Led4", None))
        self.on4.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.off4.setText(QCoreApplication.translate("MainWindow", u"off", None))
    # retranslateUi

