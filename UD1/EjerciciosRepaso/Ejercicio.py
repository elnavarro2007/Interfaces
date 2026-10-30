from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QCheckBox, QComboBox, QListWidget, QAbstractItemView, QSlider, QDial, QCalendarWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap

# Asegúrate de tener este archivo o comenta la línea si no la usas
try:
    from Cuadrado import Color
except ImportError:
    pass

class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        plantilla = QVBoxLayout()

        plantilla2 = QHBoxLayout()
        plantilla2.setContentsMargins(20, 20, 20, 20)
        plantilla2.setSpacing(50)

        plantilla3 = QVBoxLayout()
        plantilla3.setContentsMargins(5, 5, 5, 5)
        plantilla3.setSpacing(50)

        self.setWindowTitle("Mi aplicacion")

        self.label = QLabel("Texto")
        self.lineEdit = QLineEdit()

       
        self.boton1 = QCheckBox("opcion 1") 
        self.boton1.stateChanged.connect(self.boton1pulsado)

        self.boton2 = QCheckBox("opcion 2")
        self.boton2.stateChanged.connect(self.boton1pulsado)

        self.boton3 = QCheckBox("opcion 3")
        self.boton3.stateChanged.connect(self.boton1pulsado)

        plantilla2.addWidget(self.label)
        plantilla2.addWidget(self.lineEdit)
        plantilla3.addWidget(self.boton1)
        plantilla3.addWidget(self.boton2)
        plantilla3.addWidget(self.boton3)

        plantilla.addLayout(plantilla2)
        plantilla.addLayout(plantilla3)

        widget = QWidget()
        widget.setLayout(plantilla)

        self.setCentralWidget(widget)

    def boton1pulsado(self, pulsado):

        estado_texto = "Has marcado" if pulsado == 2 else "Has desmarcado"
        print(f"Has pulsado el {self.sender().text()} - {estado_texto}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
