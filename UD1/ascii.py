from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar,QDialog
from PyQt6.QtGui import QPixmap, QAction,QIcon
from image_to_ascii import ImageToAscii


class CustomDialog(QMainWindow): 

    def __init__(self):
      super().__init__()
      ImageToAscii(imagePath="icons/antifaz",outputFile="output.txt")





      















    

   
app = QApplication([])

window = MainWindow()


window.show()

app.exec()