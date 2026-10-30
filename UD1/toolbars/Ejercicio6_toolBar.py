from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar
from PyQt6.QtGui import QPixmap, QAction,QIcon


class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      self.num = 0
      self.etiqueta = QLabel("Heeeeeeeeey")
      self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
      




      barra = QToolBar("Barra de herramientas")
      barra.setIconSize(QSize(16,16))
      self.addToolBar(barra)


     

      boton = QAction(QIcon("icons/$pixil-frame-0 (4).png")," Mi botón", self)
      boton.setStatusTip("Este es mi boton")
      boton.triggered.connect(self.botonPulsado)
      barra.addAction(boton)


      



      

      barra.addSeparator()


      barra.addWidget(QLabel("Texto"))
      barra.addWidget(QCheckBox("seleccionar"))

      self.setStatusBar(QStatusBar(self))

      menu = self.menuBar()

      menu_archivo = menu.addMenu("&Archivo")

      menu_archivo.addAction(boton)

  







      self.setCentralWidget(self.etiqueta)


    def botonPulsado(self):

      self.num += 1
      self.etiqueta.setText(f"Texto cambiado {self.num}")
      
      
      
      

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()