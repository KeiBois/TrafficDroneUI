import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from DialogTemplate import DialogTemplate
from DashBoardController import DashBoardController
from views.MapView import Ui_MainWindow as MapView
from views.Dashboard import Ui_MainWindow as Dashboard

 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        
def myExitHandler():
	print("Im closing")
	mapViewController.showView()

 
app = QApplication(sys.argv)

# MainWindow = App()
dashboardController = DashBoardController()


dashboardController.showView()
app.aboutToQuit.connect(myExitHandler)
# guiStatus = ""
# while(guiStatus != "exit"):
# 	pass
# mapViewController.showView()
# dashboardController.getWindow().show()
# window.show()
# mapView = MapView()
# mapView.setupUi(window)
# window.show()

# dialog = DialogTemplate()


sys.exit(app.exec_())