import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from DialogTemplate import DialogTemplate
from ViewManager import ViewManager


 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        
 
app = QApplication(sys.argv)

viewManager = ViewManager()
viewManager.openView("dashBoardController")

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