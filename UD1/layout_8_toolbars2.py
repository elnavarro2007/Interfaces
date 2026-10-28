from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar
from PyQt6.QtGui import QPixmap, QAction,QIcon


class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      etiqueta = QLabel("Heeeeeeeeey")
      etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
      




      barra = QToolBar("Barra de herramientas")
      barra.setIconSize(QSize(16,16))
      self.addToolBar(barra)


     

      boton = QAction(QIcon("icons/$pixil-frame-0 (4).png")," Mi botón", self)
      boton.setStatusTip("Este es mi boton")
      boton.triggered.connect(self.botonPulsado)
      barra.addAction(boton)


      


      boton2 = QAction(QIcon("icons/acorn.png")," Mi otro botón", self)
      boton2.setStatusTip("Este es mi otro boton")
      boton2.triggered.connect(self.botonPulsado)
      barra.addAction(boton2)

      barra.addSeparator()


      barra.addWidget(QLabel("Texto"))
      barra.addWidget(QCheckBox("seleccionar"))

      self.setStatusBar(QStatusBar(self))
      self.setCentralWidget(etiqueta)


    def botonPulsado(self,s):
      print("pulsado",s)

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()