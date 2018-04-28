import sys
from controllers.MapViewController import MapViewController
from controllers.DashBoardController import DashBoardController

 
class ViewManager():
 
    def __init__(self):
      self.views = dict()
      self.views['mapViewController'] = MapViewController(self)
      self.views['dashBoardController'] = DashBoardController(self)
    	
    def openView(self, viewName):
        self.views[viewName].showView()