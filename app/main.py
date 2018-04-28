import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from views.Dashboard import Ui_MainWindow as Dashboard
from DialogTemplate import DialogTemplate
from DashBoardController import DashBoardController

 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        
 
app = QApplication(sys.argv)

window = App()
dashboard = Dashboard()
dashboard.setupUi(window)
dashboardController = DashBoardController(dashboard)
window.show()
# mapView = MapView()
# mapView.setupUi(window)
# window.show()

# dialog = DialogTemplate()


sys.exit(app.exec_())