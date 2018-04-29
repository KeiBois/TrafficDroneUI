import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from controllers.views.MapView import Ui_MainWindow as MapView


class MapViewController():

    def __init__(self, viewManager):
        self.window = MapView()
        self.mainWindow = QMainWindow()
        self.viewManager = viewManager
        self.window.setupUi(self.mainWindow)
        self.window.mapLabel.setPixmap(QtGui.QPixmap("controllers/views/north_boulder.png"))
        self.status = 0
        self.window.light1.setPixmap(QtGui.QPixmap("controllers/views/red.png"))
        self.window.light2.setPixmap(QtGui.QPixmap("controllers/views/green.png"))
        self.window.trafficStatusLabel.setStyleSheet("color: green;")
        self.mapImages = dict()
        self.mapImages["North Boulder"] = "north_boulder.png"
        self.mapImages["Central Boulder"] = "central_boulder.png"
        self.mapImages["University Hill"] = "university_hill.png"
        self.mapImages["Table Mesa"] = "north_boulder.png"
        self.window.districtComboBox.addItems(["North Boulder", "Central Boulder", "University Hill", "Table Mesa"])
        self.timer = QTimer()
        self.timer.start(1000)
        self.addEvents()

    def addEvents(self):
        self.window.menuButton.clicked.connect(lambda: self.openDashboard())
        self.window.districtComboBox.activated.connect(lambda: self.comboBoxChanged())
        self.window.exitButton.clicked.connect(lambda: self.exit())
        self.timer.timeout.connect(lambda: self.switch_lights())



    def comboBoxChanged(self):
        currentLocation = self.window.districtComboBox.currentText()
        imageName = self.mapImages[currentLocation]
        self.window.mapLabel.setPixmap(QtGui.QPixmap("controllers/views/" + imageName))

    def showView(self):
        self.mainWindow.show()

    def openDashboard(self):
        self.mainWindow.close()
        self.viewManager.openView("dashBoardController")

    def switch_lights(self):
        self.status += 1
        if self.status > 16:
            self.timer.stop()
            self.timer.start(1000)
            self.status = 0
            self.window.trafficStatusLabel.setText("Stable")
            self.window.trafficStatusLabel.setStyleSheet("color: green")
        elif self.status > 10:
            self.timer.stop()
            self.timer.start(2000)
            self.window.trafficStatusLabel.setText("Jam")
            self.window.trafficStatusLabel.setStyleSheet("color: red")
        if self.status % 2 == 0:
            self.window.light1.setPixmap(QtGui.QPixmap("controllers/views/red.png"))
            self.window.light2.setPixmap(QtGui.QPixmap("controllers/views/green.png"))
        else:
            self.window.light2.setPixmap(QtGui.QPixmap("controllers/views/red.png"))
            self.window.light1.setPixmap(QtGui.QPixmap("controllers/views/green.png"))
    def exit(self):
        sys.exit()