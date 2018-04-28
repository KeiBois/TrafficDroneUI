import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.Dashboard import Ui_MainWindow as Dashboard
from DialogTemplate import DialogTemplate

 
class DashBoardController():
 
    def __init__(self, viewManager):
        self.window = Dashboard()
        self.mainWindow = QMainWindow()
        self.viewManager = viewManager
        self.window.setupUi(self.mainWindow)
        self.addEvents()

    def addEvents(self):
    	self.window.droneSchedulerButton.clicked.connect(lambda: self.openDroneScheduler())
    	self.window.analyzeTrafficButton.clicked.connect(lambda: self.openAnalyzeTraffic())
    	self.window.trafficAlertsButton.clicked.connect(lambda: self.openTrafficAlerts())

    def showView(self):
    	self.mainWindow.show()
    	
    def openDroneScheduler(self):
        pass

    def openAnalyzeTraffic(self):
        self.mainWindow.close()
        self.viewManager.openView("mapViewController")

    def openTrafficAlerts(self):
        pass
