from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")

      

      tabs = QTabWidget()
      widget = QWidget()





      tabs.setTabPosition(QTabWidget.TabPosition.North)
      tabs.setMovable(True)

      tabs.addTab(Color("red"),"rojo")
      tabs.addTab(Color("yellow"),"amarillo")
      tabs.addTab(Color("blue"),"azul")
      tabs.addTab(Color("purple"),"morado")
      self.setCentralWidget(tabs)





      



      





 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()