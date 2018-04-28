# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/MapView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2500, 1800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mapLabel = QtWidgets.QLabel(self.centralwidget)
        self.mapLabel.setGeometry(QtCore.QRect(130, 190, 1391, 1161))
        self.mapLabel.setText("")
        self.mapLabel.setPixmap(QtGui.QPixmap("map.png"))
        self.mapLabel.setObjectName("mapLabel")
        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        self.menuButton.setGeometry(QtCore.QRect(60, 40, 271, 81))
        self.menuButton.setObjectName("menuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2500, 43))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuButton.setText(_translate("MainWindow", "Back to Dashboard"))

