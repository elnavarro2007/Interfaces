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


      boton3 = QAction(QIcon("icons/steam.png")," Mi otro botón", self)
      boton3.setStatusTip("Este es mi otro boton")
      boton3.triggered.connect(self.botonPulsado)
      

      barra.addSeparator()


      barra.addWidget(QLabel("Texto"))
      barra.addWidget(QCheckBox("seleccionar"))

      self.setStatusBar(QStatusBar(self))

      menu = self.menuBar()

      menu_archivo = menu.addMenu("&Archivo")
      menu_editar = menu.addMenu("&Editar")
      menu_insertar = menu.addMenu("&insertar")
      menu_archivo.addAction(boton)
      menu_archivo.addAction(boton2)
      menu_archivo.addSeparator()
      menu_mas = menu_archivo.addMenu("mas")
      menu_mas.addAction(boton)
      menu_mas.addAction(boton2)
      menu_mas.addAction(boton3)







      self.setCentralWidget(etiqueta)


    def botonPulsado(self,s):
      print("pulsado",s)

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()