from Ej2 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication


#from PyQt6.QtWidgets import QApplication, QMessageBox,QDateEdit, QHBoxLayout, QRadioButton, QTextEdit, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget
#python -m venv App (se añadirá contenido a nuestra carpeta)
#cd App
#cd Scripts
#.\activate
#pip install PyQt6
# pyuic6 Ej1.ui -o Ej1.py 
# python, qt for python, pyqtIntegration
# pip install PySide6
# pyside6-designer
#wordwrap



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
