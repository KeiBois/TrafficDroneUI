import sys
from PyQt5.QtWidgets import QApplication
from ViewManager import ViewManager


 
class App():
 
    def __init__(self):
      app = QApplication(sys.argv)
      viewManager = ViewManager()
      viewManager.openView("dashBoardController")
      sys.exit(app.exec_())
        
app = App()