from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")

      


      widget = QWidget()
      plantilla = QStackedLayout()

      plantilla.addWidget(Color("red"))
      plantilla.addWidget(Color("green"))
      plantilla.addWidget(Color("yellow"))
      plantilla.addWidget(Color("blue"))



      plantilla.setCurrentIndex(2)



      widget.setLayout(plantilla)
      self.setCentralWidget(widget)

 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()