import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from views.Dashboard import Ui_MainWindow as Dashboard
from DialogTemplate import DialogTemplate

 
class DashBoardController():
 
    def __init__(self, window):
    	self.window = window
    	self.addEvents()

    def addEvents(self):
    	self.window.droneSchedulerButton.clicked.connect(lambda: self.openDroneScheduler())
    	self.window.analyzeTrafficButton.clicked.connect(lambda: self.openAnalyzeTraffic())
    	self.window.trafficAlertsButton.clicked.connect(lambda: self.openTrafficAlerts())

    def openDroneScheduler(self):
    	sys.exit()
    	pass

    def openAnalyzeTraffict(self):
    	pass

    def openTrafficAlerts(self):
    	pass