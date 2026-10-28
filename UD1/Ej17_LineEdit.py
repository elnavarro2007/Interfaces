from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")
      
      self.texto = QLineEdit()
      self.texto.setMaxLength(20)
      self.texto.setPlaceholderText("Introduce tu nombre ")

      #texto.textChanged.connect(self.textoCambiado)
      self.texto.returnPressed.connect(self.introPulsado)


      self.setCentralWidget(self.texto)

    def textoCambiado(self,nombre):
      print(nombre)

    def introPulsado(self):
       print("Intro puasglado")
       print(self.texto.text())



      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()