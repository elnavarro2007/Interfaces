from inspect import stack
from tabnanny import check

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QStackedWidget,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QHBoxLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")

      


      self.setWindowTitle("Mi aplicacion")

      

      tabs = QTabWidget()
      widget = QWidget()
      widget2 = QWidget()
      texto = QLabel("Hola")
      escribir = QLineEdit()
      horizontal = QHBoxLayout()
      vertical = QVBoxLayout()
      boton = QPushButton("pulsa")
      seleccion = QCheckBox("seleccion")


      horizontal.addWidget(texto)
      horizontal.addWidget(escribir)

      widget.setLayout(horizontal)
      widget2.setLayout(vertical)

      vertical.addWidget(seleccion)
      vertical.addWidget(boton)





      tabs.setTabPosition(QTabWidget.TabPosition.North)
      tabs.setMovable(True)

      tabs.addTab(widget,"pestaña 1")
      tabs.addTab(widget2,"pestaña 2")

      self.setCentralWidget(tabs)
       
       
       

 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()