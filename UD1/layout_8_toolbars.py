from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar
from PyQt6.QtGui import QPixmap, QAction

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      etiqueta = QLabel("Heeeeeeeeey")
      etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
      




      barra = QToolBar("Barra de herramientas")
      self.addToolBar(barra)

      self.setCentralWidget(etiqueta)

      boton = QAction(" Mi boton", self)
      boton.setStatusTip("Este es mi boton")
      boton.triggered.connect(self.botonPulsado)
      barra.addAction(boton)

      self.setStatusBar(QStatusBar(self))


    def botonPulsado(self,s):
      print("pulsado",s)

    






      



      





 





    
app = QApplication([])

window = MainWindow()


window.show()

app.exec()