from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()

      
      spinbox = QSlider(Qt.Orientation.Horizontal)
      spinbox.setRange(-10,10)
      spinbox.valueChanged.connect(self.valorCambiado)


      self.setWindowTitle("Mi aplicacion")

      self.setCentralWidget(spinbox)

    def valorCambiado(self,value):
       print(value)
      

       



      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()