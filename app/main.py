from PyQt5 import uic, QtWidgets
import sys
from ..TrafficDroneUI.views.window1 import Ui_Dialog as WindowTemplate

class Ui(QtWidgets.QDialog):
	def __init__(self):
		super(Ui, self).__init__()
		self.window = WindowTemplate()
		self.window.setupUi(self)
		self.addEvents()
		self.show()

	def addEvents(self):
		self.window.helloButton.clicked.connect(lambda: self.sayHello())
		self.window.exitButton.clicked.connect(lambda: self.plzExit())

	def sayHello(self):
		self.window.myLabel.setText("HELLO!!!")

	def plzExit(self):
		sys.exit()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()

	sys.exit(app.exec_())