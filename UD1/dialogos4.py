from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar,QDialog,QDialogButtonBox,QMessageBox
from PyQt6.QtGui import QPixmap, QAction,QIcon


class MainWindow(QMainWindow): 

    def __init__(self, parent=None):
      super().__init__(parent)
      self.setWindowTitle("Hola")

      etiqueta = QLabel("Heeeeeeeeey")
      etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

      boton = QPushButton("Pulsa aqui")
      boton.clicked.connect(self.botonPulsado)
      self.setCentralWidget(boton)
      













    def botonPulsado(self,s):
      dlg = QMessageBox(self)
      dlg.setWindowTitle("Cuadro de mensaje")
      dlg.setText("Este es el mensaje de mi cuadro de texto")
      dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
      dlg.setIcon(QMessageBox.Icon.Information)

      if dlg.exec() == QMessageBox.StandardButton.Yes:
         print("El usuario ha aceptado")
      else:
         print("El usuario ha rechazado")


    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()