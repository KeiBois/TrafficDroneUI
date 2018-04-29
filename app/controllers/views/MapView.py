# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/controllers/views/MapView.ui'
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
        self.mapLabel.setGeometry(QtCore.QRect(110, 450, 1391, 1161))
        self.mapLabel.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.mapLabel.setText("")
        self.mapLabel.setPixmap(QtGui.QPixmap("../../views/map.png"))
        self.mapLabel.setObjectName("mapLabel")
        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        self.menuButton.setGeometry(QtCore.QRect(60, 40, 271, 81))
        self.menuButton.setObjectName("menuButton")
        self.districtComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.districtComboBox.setGeometry(QtCore.QRect(340, 360, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.districtComboBox.setFont(font)
        self.districtComboBox.setObjectName("districtComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 349, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 0, 1881, 211))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(120, 190, 2201, 151))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1540, 430, 931, 881))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(50, 390, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 230, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 310, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(50, 600, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.menuButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.menuButton_2.setGeometry(QtCore.QRect(630, 730, 271, 81))
        self.menuButton_2.setObjectName("menuButton_2")
        self.menuButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.menuButton_3.setGeometry(QtCore.QRect(330, 730, 271, 81))
        self.menuButton_3.setObjectName("menuButton_3")
        self.menuButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.menuButton_4.setGeometry(QtCore.QRect(30, 730, 271, 81))
        self.menuButton_4.setObjectName("menuButton_4")
        self.trafficStatusLabel = QtWidgets.QLabel(self.groupBox)
        self.trafficStatusLabel.setGeometry(QtCore.QRect(290, 50, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.trafficStatusLabel.setFont(font)
        self.trafficStatusLabel.setObjectName("trafficStatusLabel")
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
        self.label.setText(_translate("MainWindow", "City District: "))
        self.label_2.setText(_translate("MainWindow", "Analyze Traffic"))
        self.description_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose a <span style=\" font-weight:600;\">district</span> to display a map of the area and get live status updates and recomendations to alleviate traffic</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <br /></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Traffic Status"))
        self.label_3.setText(_translate("MainWindow", "Traffic Status: "))
        self.label_7.setText(_translate("MainWindow", "Traffic Light 1: Go"))
        self.label_4.setText(_translate("MainWindow", "Traffic Light 1: Stop"))
        self.label_5.setText(_translate("MainWindow", "Traffic Light 1: Stop"))
        self.label_6.setText(_translate("MainWindow", "Traffic Light 1: Go"))
        self.label_8.setText(_translate("MainWindow", "Proposed Solution: "))
        self.menuButton_2.setText(_translate("MainWindow", "Make Changes"))
        self.menuButton_3.setText(_translate("MainWindow", "Visualize Solution"))
        self.menuButton_4.setText(_translate("MainWindow", "Edit Solution"))
        self.trafficStatusLabel.setText(_translate("MainWindow", "Stable"))

