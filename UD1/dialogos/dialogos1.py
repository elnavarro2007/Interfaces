from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar,QDialog
from PyQt6.QtGui import QPixmap, QAction,QIcon


class CustomDialog(QMainWindow): 

    def __init__(self):
      super().__init__()


      etiqueta = QLabel("Heeeeeeeeey")
      etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

      boton = QPushButton("Pulsa aqui")
      boton.clicked.connect(self.botonPulsado)
      self.setCentralWidget(boton)

      













    def botonPulsado(self,s):
      dig = QDialog()
      dig.setWindowTitle("Cuadro de dialogo")
      dig.exec()

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()