import sys
import webbrowser
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from controllers.views.DashBoard import Ui_MainWindow as Dashboard

 
class DashBoardController():
 
    def __init__(self, viewManager):
        self.window = Dashboard()
        self.mainWindow = QMainWindow()
        self.viewManager = viewManager
        self.window.setupUi(self.mainWindow)
        self.window.logoLabel.setPixmap(QtGui.QPixmap("controllers/views/drone_logo.jpg"))
        self.addEvents()

    def addEvents(self):
        self.window.droneSchedulerButton.clicked.connect(lambda: self.openDroneScheduler())
        self.window.analyzeTrafficButton.clicked.connect(lambda: self.openAnalyzeTraffic())
        self.window.trafficAlertsButton.clicked.connect(lambda: self.openTrafficAlerts())
        self.window.exitButton.clicked.connect(lambda: self.exit())

    def showView(self):
    	self.mainWindow.show()
    	
    def openDroneScheduler(self):
        webbrowser.open('https://my.flytbase.com/')  # Go to example.com

    def openAnalyzeTraffic(self):
        self.mainWindow.close()
        self.viewManager.openView("mapViewController")

    def exit(self):
        sys.exit()

    def openTrafficAlerts(self):
        self.mainWindow.close()
        self.viewManager.openView("trafficAlertsController")
