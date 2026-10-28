from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      
      dial = QDial()
      dial.setRange(-100,10000)
      dial.setNotchesVisible(True)
      dial.valueChanged.connect(self.valorCambiado)


      self.setWindowTitle("Mi aplicacion")

      self.setCentralWidget(dial)

    def valorCambiado(self,value):
       print(value)
      

       



      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()