# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/controllers/views/window1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 627)
        self.helloButton = QtWidgets.QPushButton(Dialog)
        self.helloButton.setGeometry(QtCore.QRect(350, 360, 168, 51))
        self.helloButton.setObjectName("helloButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(170, 360, 168, 51))
        self.exitButton.setObjectName("exitButton")
        self.myLabel = QtWidgets.QLabel(Dialog)
        self.myLabel.setGeometry(QtCore.QRect(240, 160, 103, 30))
        self.myLabel.setObjectName("myLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.helloButton.setText(_translate("Dialog", "Say Hello"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.myLabel.setText(_translate("Dialog", "TextLabel"))

