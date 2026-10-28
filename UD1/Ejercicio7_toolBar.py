from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar
from PyQt6.QtGui import QPixmap, QAction,QIcon


class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      self.num = 0
      self.etiqueta = QLabel("Hola!")
      self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
      




      barra = QToolBar("Barra de herramientas")
      barra.setIconSize(QSize(16,16))
      self.addToolBar(barra)


     


      




      boton2 = QAction("X",self)
      boton3 = QAction("Instagram",self)

      boton2.setStatusTip("Siguenos en insta")
      boton3.setStatusTip("Siguenos en x")


      botonG = QAction(QIcon("icons/disk.png"),"Guardar",self)
      botonN = QAction(QIcon("icons/document.png"),"Nuevo",self)
      botonA = QAction(QIcon("icons/application-dock.png"),"Abrir",self)


      barra.addAction(botonG)
      barra.addAction(botonN)
      barra.addAction(botonA)


      



      

      barra.addSeparator()




      self.setStatusBar(QStatusBar(self))

      menu = self.menuBar()

      menu_archivo = menu.addMenu("&Archivo")
      menu_archivo.addAction(botonG)
      menu_archivo.addAction(botonN)
      menu_archivo.addAction(botonA)



      menu_ayuda = menu.addMenu("&Ayuda")
      subMenu = menu_ayuda.addMenu("Siguenos")

      subMenu.addAction(boton2)
      subMenu.addAction(boton3)




      

     

      self.setCentralWidget(self.etiqueta)


    def botonPulsado(self):

      self.num += 1
      self.etiqueta.setText(f"Texto cambiado {self.num}")
      
      
      
      

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()