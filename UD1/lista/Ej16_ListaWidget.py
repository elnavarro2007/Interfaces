from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()


      self.setWindowTitle("Mi aplicacion")
      
      lista = QListWidget()
      lista.addItems(["Uno","Dos","Tres"])
      lista.currentTextChanged.connect(self.mostrarTexto)
      lista.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)


      self.setCentralWidget(lista)

    def mostrarIndice(self, texto):
      print((texto+1))

    def mostrarTexto(self, texto):
      print(texto)

      

      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()