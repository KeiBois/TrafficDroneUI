import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from DialogTemplate import DialogTemplate


class MapViewController():

	def __init__(self, viewManager):
		self.window = MapView()
		self.mainWindow = QMainWindow()
		self.viewManager = viewManager
		self.window.setupUi(self.mainWindow)
		self.window.mapLabel.setPixmap(QtGui.QPixmap("app/views/map.png"))
		self.addEvents()

	def addEvents(self):
		self.window.menuButton.clicked.connect(lambda: self.openDashboard())

	def showView(self):
		self.mainWindow.show()

	def openDashboard(self):
		self.mainWindow.close()
		self.viewManager.openView("dashBoardController")