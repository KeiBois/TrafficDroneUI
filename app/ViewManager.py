import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from views.MapView import Ui_MainWindow as MapView
from views.Dashboard import Ui_MainWindow as Dashboard
from MapViewController import MapViewController
from DashBoardController import DashBoardController
from DialogTemplate import DialogTemplate

 
class ViewManager():
 
    def __init__(self):
      self.views = dict()
      self.views['mapViewController'] = MapViewController(self)
      self.views['dashBoardController'] = DashBoardController(self)
    	
    def openView(self, viewName):
        self.views[viewName].showView()