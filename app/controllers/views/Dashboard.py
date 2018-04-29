# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/controllers/views/Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2461, 1572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 2411, 211))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(210, 220, 1541, 601))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 720, 2231, 961))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.droneSchedulerButton = QtWidgets.QPushButton(self.frame)
        self.droneSchedulerButton.setGeometry(QtCore.QRect(50, 120, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.droneSchedulerButton.setFont(font)
        self.droneSchedulerButton.setObjectName("droneSchedulerButton")
        self.description_label_2 = QtWidgets.QLabel(self.frame)
        self.description_label_2.setGeometry(QtCore.QRect(600, 120, 1481, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.description_label_2.setFont(font)
        self.description_label_2.setWordWrap(True)
        self.description_label_2.setObjectName("description_label_2")
        self.analyzeTrafficButton = QtWidgets.QPushButton(self.frame)
        self.analyzeTrafficButton.setGeometry(QtCore.QRect(50, 290, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.analyzeTrafficButton.setFont(font)
        self.analyzeTrafficButton.setObjectName("analyzeTrafficButton")
        self.description_label_4 = QtWidgets.QLabel(self.frame)
        self.description_label_4.setGeometry(QtCore.QRect(590, 450, 1481, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.description_label_4.setFont(font)
        self.description_label_4.setWordWrap(True)
        self.description_label_4.setObjectName("description_label_4")
        self.trafficAlertsButton = QtWidgets.QPushButton(self.frame)
        self.trafficAlertsButton.setGeometry(QtCore.QRect(50, 460, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.trafficAlertsButton.setFont(font)
        self.trafficAlertsButton.setObjectName("trafficAlertsButton")
        self.description_label_5 = QtWidgets.QLabel(self.frame)
        self.description_label_5.setGeometry(QtCore.QRect(600, 300, 1481, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.description_label_5.setFont(font)
        self.description_label_5.setWordWrap(True)
        self.description_label_5.setObjectName("description_label_5")
        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(1890, 650, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color:#e57373 ;\n"
"color: white;")
        self.exitButton.setObjectName("exitButton")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(1810, 250, 571, 421))
        self.logoLabel.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("drone_logo.jpg"))
        self.logoLabel.setObjectName("logoLabel")
        self.description_label.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.logoLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2461, 43))
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
        self.label.setText(_translate("MainWindow", "Drone CV Aided Traffic Monitoring"))
        self.description_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is a prototoype for a traffic monitoring system aided by Drones and processing the image using computer vision. To begin a test run do the following:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the <span style=\" font-weight:600;\">&quot;Drone Flight Scheduler&quot; </span>button and follow the instructions to schedule and record life traffic footage to later be analized</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the <span style=\" font-weight:600;\">&quot;Analyze Traffic&quot; </span>button and follow the instructions to select recorded footage and get meaningful information about the traffic status</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the <span style=\" font-weight:600;\">&quot;Traffic Alerts&quot;</span> button to monitor several traffic status alerts from various locations</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.droneSchedulerButton.setText(_translate("MainWindow", "Drone Flight Scheduler"))
        self.description_label_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Schedule a flight plan for a drone using a Maps Graphical Representation</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.analyzeTrafficButton.setText(_translate("MainWindow", "Analyze Traffic"))
        self.description_label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:12pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</span></p></body></html>"))
        self.trafficAlertsButton.setText(_translate("MainWindow", "Traffic Alerts"))
        self.description_label_5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analyze the areas from the drone captured videos of traffic</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

