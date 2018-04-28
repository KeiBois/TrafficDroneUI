import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from controllers.views.MapView import Ui_MainWindow as MapView


class MapViewController():

	def __init__(self, viewManager):
		self.window = MapView()
		self.mainWindow = QMainWindow()
		self.viewManager = viewManager
		self.window.setupUi(self.mainWindow)
		self.window.mapLabel.setPixmap(QtGui.QPixmap("app/controllers/views/map.png"))
		self.addEvents()

	def addEvents(self):
		self.window.menuButton.clicked.connect(lambda: self.openDashboard())

	def showView(self):
		self.mainWindow.show()

	def openDashboard(self):
		self.mainWindow.close()
		self.viewManager.openView("dashBoardController")