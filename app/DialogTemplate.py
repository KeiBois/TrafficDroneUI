from PyQt5 import uic, QtWidgets
import sys
from views.window1 import Ui_Dialog as WindowTemplate

class DialogTemplate(QtWidgets.QDialog):
	def __init__(self):
		super(DialogTemplate, self).__init__()
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

# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	window = DialogTemplate()

# 	sys.exit(app.exec_())