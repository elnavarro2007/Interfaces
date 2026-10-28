from inspect import stack

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QStackedWidget,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QHBoxLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")

      


      widget = QWidget()
      plantilla = QStackedLayout()
      vertical = QVBoxLayout()
      horizontal = QHBoxLayout()

      boton1 = QPushButton("red")
      boton2 = QPushButton("green")
      boton3 = QPushButton("yellow")


      boton1.clicked.connect(lambda: plantilla.setCurrentIndex(0))
      boton2.clicked.connect(lambda: plantilla.setCurrentIndex(1))
      boton3.clicked.connect(lambda: plantilla.setCurrentIndex(2))





      


      horizontal.addWidget(boton1)
      horizontal.addWidget(boton2)
      horizontal.addWidget(boton3)

      vertical.addLayout(horizontal)
      vertical.addLayout(plantilla)




      

      plantilla.addWidget(Color("red"))
      plantilla.addWidget(Color("green"))
      plantilla.addWidget(Color("yellow"))
      plantilla.addWidget(Color("blue"))


      


      
      





      plantilla.setCurrentIndex(2)


      
      widget.setLayout(vertical)
      
      self.setCentralWidget(widget)

    def botonpulsado(self, ):
      # importante el sender
      print(self.windowIconText)
       
       
       

 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()