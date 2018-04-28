import sys
from PyQt5 import QtGui
from views.window1 import Ui_Dialog as WindowTemplate


class Application(QtGui.QWidget):
    def __init__(self):
        super(Application, self).__init__()
        self.initUI()
  
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
