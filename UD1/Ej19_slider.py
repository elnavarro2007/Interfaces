from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider
from PyQt6.QtGui import QPixmap





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()
      spinbox = QSlider()
      spinbox.setRange(-10,10)
      slider.valueChanged.connect


      self.setWindowTitle("Mi aplicacion")
      

       



      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()