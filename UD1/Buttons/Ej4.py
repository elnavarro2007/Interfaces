from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicacion")
        boton = QPushButton("Tocame!!!!!")


        self.setFixedSize(QSize(800,600))

        self.setCentralWidget(boton)
        


app = QApplication([])


window = MainWindow()


window.show()

app.exec()