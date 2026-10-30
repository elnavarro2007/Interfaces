from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        self.botonpulsado = True
        
        self.num = 0
        self.setWindowTitle("Mi aplicacion")
        self.boton = QPushButton("Tocame")
        self.boton.setCheckable(True)
        self.boton.setChecked
        self.boton.pressed.connect(self.contarVecesNum)

        


        self.setFixedSize(QSize(800,600))

        self.setCentralWidget(self.boton)

    def contarVecesNum(self):
        self.boton.setText("Boton ya tocado")
        self.boton.setEnabled(False)




app = QApplication([])


window = MainWindow()


window.show()

app.exec()