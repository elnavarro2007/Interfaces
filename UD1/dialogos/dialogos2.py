from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar,QDialog,QDialogButtonBox
from PyQt6.QtGui import QPixmap, QAction,QIcon


class MainWindow(QDialog): 

    def __init__(self):
      super().__init__()
      self.setWindowTitle("Hola")

      etiqueta = QLabel("Heeeeeeeeey")
      etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

      QBtn = QDialogButtonBox.StandardButton.Ok  | QDialogButtonBox.StandardButton.Cancel
      self.dialogBox = QDialogButtonBox(QBtn)
      self.dialogBox.accepted.connect(self.accept)
      self.dialogBox.accepted.connect(self.reject)

      self.plantilla = QVBoxLayout()
      mensaje = QLabel("Algo ha sucedido, todo ok?")
      self.plantilla.addWidget(mensaje)
      self.plantilla.addWidget(self.dialogBox)
      self.setLayout(self.plantilla)
      













    def botonPulsado(self,s):
        dig = QDialog()
        dig.setWindowTitle("Cuadro de dialogo")

        dig.exec()

    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()