from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        self.botonpulsado = True
        

        self.setWindowTitle("Mi aplicacion")
        boton = QPushButton("Tocame!!!!!")
        boton.setCheckable(True)
        boton.clicked.connect(self.botonActivado)
        boton.setChecked(self.botonpulsado)
        


        self.setFixedSize(QSize(800,600))

        self.setCentralWidget(boton)

    def botonActivado(self, checked):
        self.botonpulsado = checked
        print(self.botonpulsado)



app = QApplication([])


window = MainWindow()


window.show()

app.exec()