import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from DialogTemplate import DialogTemplate


class MapViewController():

	def __init__(self):
		self.window = MapView()
		self.mainWindow = QMainWindow()
		self.window.setupUi(self.mainWindow)
		self.window.mapLabel.setPixmap(QtGui.QPixmap("app/views/map.png"))
		self.addEvents()

	def addEvents(self):
		pass

	def showView(self):
		self.mainWindow.show()

