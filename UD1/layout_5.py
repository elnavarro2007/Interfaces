from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QTabWidget,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")

      


      widget = QWidget()
      plantilla = QGridLayout()

      plantilla.addWidget(Color("red"),0,0)
      plantilla.addWidget(Color("green"),0,1)
      plantilla.addWidget(Color("yellow"),1,2)
      plantilla.addWidget(Color("blue"),2,0)



      widget.setLayout(plantilla)
      self.setCentralWidget(widget)

 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()