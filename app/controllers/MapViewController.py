import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
from controllers.views.MapView import Ui_MainWindow as MapView


class MapViewController():

	def __init__(self, viewManager):
		self.window = MapView()
		self.mainWindow = QMainWindow()
		self.viewManager = viewManager
		self.window.setupUi(self.mainWindow)
		self.window.mapLabel.setPixmap(QtGui.QPixmap("controllers/views/north_boulder.png"))
		self.window.trafficStatusLabel.setStyleSheet("color: green;")
		self.mapImages = dict()
		self.mapImages["North Boulder"] = "north_boulder.png"
		self.mapImages["Central Boulder"] = "central_boulder.png"
		self.mapImages["University Hill"] = "university_hill.png"
		self.mapImages["Table Mesa"] = "north_boulder.png"
		self.window.districtComboBox.addItems(["North Boulder", "Central Boulder", "University Hill", "Table Mesa"])
		self.addEvents()

	def addEvents(self):
		self.window.menuButton.clicked.connect(lambda: self.openDashboard())
		self.window.districtComboBox.activated.connect(lambda: self.comboBoxChanged())

	def comboBoxChanged(self):
		currentLocation = self.window.districtComboBox.currentText()
		imageName = self.mapImages[currentLocation]
		self.window.mapLabel.setPixmap(QtGui.QPixmap("controllers/views/" + imageName))

	def showView(self):
		self.mainWindow.show()

	def openDashboard(self):
		self.mainWindow.close()
		self.viewManager.openView("dashBoardController")