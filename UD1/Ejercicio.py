from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QHBoxLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      plantilla = QVBoxLayout()

      



      plantilla2 = QHBoxLayout()
      plantilla2.setContentsMargins(20,20,20,20)
      plantilla2.setSpacing(50)

      plantilla3 = QVBoxLayout()
      plantilla3.setContentsMargins(5,5,5,5)
      plantilla3.setSpacing(50)

      self.setWindowTitle("Mi aplicacion")


      self.label = QLabel("Texto")
      self.lineEdit = QLineEdit()

      self.boton1 = QCheckBox("opcion 1") 
      self.boton1.setCheckable(True)
      self.boton1.setChecked
      self.boton1.stateChanged.connect( self.boton1pulsado)


      self.boton2 = QCheckBox("opcion 2")
      self.boton2.setCheckable(True)
      self.boton2.setChecked
      self.boton2.stateChanged.connect(self.boton1pulsado)

      



      self.boton3 = QCheckBox("opcion 3")
      self.boton3.setCheckable(True)
      self.boton3.setChecked
      self.boton3.stateChanged.connect(self.boton1pulsado)

      


      


      plantilla2.addWidget(self.label)
      plantilla2.addWidget(self.lineEdit)
      plantilla3.addWidget(self.boton1)
      plantilla3.addWidget(self.boton2)
      plantilla3.addWidget(self.boton3)

      plantilla.addLayout(plantilla2)
      plantilla.addLayout(plantilla3)
      





      



      



      widget = QWidget()
      widget.setLayout(plantilla)


      self.setCentralWidget(widget)

    def boton1pulsado(self, pulsado):
      # importante el sender
      print(f"Has pulsado el  {self.sender().text()} - {["Has desmarcado","","Has marcado"][pulsado]}")





      




app = QApplication([])

window = MainWindow()


window.show()

app.exec()