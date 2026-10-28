from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        self.botonpulsado = True
        

        self.setWindowTitle("Mi aplicacion")
        boton = QPushButton("Tocame")
        boton.setCheckable(True)
        boton.pressed.connect(self.botonActivado)
        boton.released.connect(self.botonDesactivado)
        boton.clicked.connect(self.botonSoltado)
        


        self.setFixedSize(QSize(800,600))

        self.setCentralWidget(boton)

    def botonActivado(self):
        print("boton Pulsado")


    def botonDesactivado(self):
        print("Boton Soltado")

    def botonSoltado(self):
         print("Boton Soltado y Pulsado")



app = QApplication([])


window = MainWindow()


window.show()

app.exec()