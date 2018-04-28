import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from views.Dashboard import Ui_MainWindow as Dashboard
from MapViewController import MapViewController
from DialogTemplate import DialogTemplate

 
class DashBoardController():
 
    def __init__(self):
        self.views = dict()
        self.views['mapViewController'] = MapViewController()
        self.window = Dashboard()
        self.mainWindow = QMainWindow()
        self.window.setupUi(self.mainWindow)
        self.addEvents()

    def addEvents(self):
    	self.window.droneSchedulerButton.clicked.connect(lambda: self.openDroneScheduler())
    	self.window.analyzeTrafficButton.clicked.connect(lambda: self.openAnalyzeTraffic())
    	self.window.trafficAlertsButton.clicked.connect(lambda: self.openTrafficAlerts())

    def showView(self):
    	self.mainWindow.show()
    	
    def openDroneScheduler(self):
        self.openView("mapViewController")

    def openAnalyzeTraffict(self):
        pass

    def openTrafficAlerts(self):
        pass

    def openView(self, viewName):
        self.mainWindow.close()
        self.views[viewName].showView()