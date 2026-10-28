from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QHBoxLayout
from PyQt6.QtGui import QPixmap

from Cuadrado import Color





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      

      self.calendar = QCalendarWidget()

      self.setWindowTitle("Mi aplicacion")

      plantilla = QVBoxLayout()

      plantilla.addWidget(Color("red"))
      plantilla.addWidget(Color("blue"))
      plantilla.addWidget(Color("green"))

      widget = QWidget()
      widget.setLayout(plantilla)
      self.setCentralWidget(widget)








    def mostrarFecha(self):
       print(self.calendar.selectedDate().toString("dd/MM/yyyy"))
      

       



      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()