# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\VierGewinnt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VierGewinnt(object):
    def setupUi(self, VierGewinnt):
        VierGewinnt.setObjectName("VierGewinnt")
        VierGewinnt.resize(461, 491)
        self.centralwidget = QtWidgets.QWidget(VierGewinnt)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.feldBesetzen = QtWidgets.QPushButton(self.centralwidget)
        self.feldBesetzen.setObjectName("feldBesetzen")
        self.gridLayout.addWidget(self.feldBesetzen, 0, 2, 1, 2)
        self.feldLabel = QtWidgets.QLabel(self.centralwidget)
        self.feldLabel.setObjectName("feldLabel")
        self.gridLayout.addWidget(self.feldLabel, 0, 0, 1, 1)
        self.webserviceBox = QtWidgets.QCheckBox(self.centralwidget)
        self.webserviceBox.setChecked(True)
        self.webserviceBox.setTristate(False)
        self.webserviceBox.setObjectName("webserviceBox")
        self.gridLayout.addWidget(self.webserviceBox, 0, 4, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 5)
        self.beenden = QtWidgets.QPushButton(self.centralwidget)
        self.beenden.setObjectName("beenden")
        self.gridLayout.addWidget(self.beenden, 2, 3, 1, 2)
        self.neueSpiel = QtWidgets.QPushButton(self.centralwidget)
        self.neueSpiel.setObjectName("neueSpiel")
        self.gridLayout.addWidget(self.neueSpiel, 2, 0, 1, 3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(79, 22))
        self.spinBox.setMaximum(3)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        VierGewinnt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VierGewinnt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 26))
        self.menubar.setObjectName("menubar")
        VierGewinnt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VierGewinnt)
        self.statusbar.setObjectName("statusbar")
        VierGewinnt.setStatusBar(self.statusbar)

        self.retranslateUi(VierGewinnt)
        QtCore.QMetaObject.connectSlotsByName(VierGewinnt)

    def retranslateUi(self, VierGewinnt):
        _translate = QtCore.QCoreApplication.translate
        VierGewinnt.setWindowTitle(_translate("VierGewinnt", "VierGewinnt"))
        self.feldBesetzen.setText(_translate("VierGewinnt", "Feld besetzen"))
        self.feldLabel.setText(_translate("VierGewinnt", "Feld (0-3)"))
        self.webserviceBox.setText(_translate("VierGewinnt", "Webservice"))
        self.beenden.setText(_translate("VierGewinnt", "Beenden"))
        self.neueSpiel.setText(_translate("VierGewinnt", "Neues Spiel"))

