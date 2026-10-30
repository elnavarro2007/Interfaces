from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QHBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      layout1 = QVBoxLayout()

      grupo1 = QGroupBox("Botones")

      boton1 = QPushButton("Boton 1")
      boton2 = QPushButton("Boton 2")
      boton3 = QPushButton("Boton 3")

      layout1.addWidget(boton1)
      layout1.addWidget(boton2)
      layout1.addWidget(boton3)

      boton1.clicked.connect(self.boton1pulsado)
      boton2.clicked.connect(self.boton1pulsado)
      boton3.clicked.connect(self.boton1pulsado)
      


      grupo1.setLayout(layout1)
      widget = QWidget()
      widget.setLayout(layout1)
      self.setCentralWidget(widget)

    def boton1pulsado(self, ):
      # importante el sender
      print(f"Has pulsado el  {self.sender().text()}")





      




app = QApplication([])

window = MainWindow()


window.show()

app.exec()