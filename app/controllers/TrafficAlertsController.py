import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from controllers.views.TrafficAlerts import Ui_MainWindow as TrafficAlerts


class TrafficAlertsController():

	def __init__(self, viewManager):
		self.window = TrafficAlerts()
		self.mainWindow = QMainWindow()
		self.viewManager = viewManager
		self.window.setupUi(self.mainWindow)
		self.window.districtComboBox.addItems(["North Boulder", "Central Boulder", "University Hill", "Table Mesa"])
		self.alertsTable = self.window.alertsTable
		self.addEvents()

	def addEvents(self):
		self.window.menuButton.clicked.connect(lambda: self.openDashboard())
		self.window.exitButton.clicked.connect(lambda: self.exit())


	def showView(self):
		self.mainWindow.show()

	def openDashboard(self):
		self.mainWindow.close()
		self.viewManager.openView("dashBoardController")


	def exit(self):
		sys.exit()