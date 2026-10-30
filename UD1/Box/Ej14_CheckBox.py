from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")
      casilla = QCheckBox("Casilla de verificacion")

      formato = casilla.font()

      formato.setBold(True)
      casilla.setFont(formato)
      

      casilla.stateChanged.connect(self.mostrarEstado)

      self.setCentralWidget(casilla)

    def mostrarEstado(self, s):
      print(s)



app = QApplication([])

window = MainWindow()


window.show()

app.exec()