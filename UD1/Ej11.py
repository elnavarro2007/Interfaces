from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        self.botonpulsado = True
        
        self.num = 0
        self.setWindowTitle("Mi aplicacion")

        label = QLabel()
        input = QLineEdit()

        input.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        layout.addWidget(input)
        layout.addWidget(label)

        contenedor = QWidget()
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)




    

       

        


        self.setFixedSize(QSize(800,600))


    def contarVecesNum(self,pulsado):
        self.boton.setText(["Tocado","No tocado"][pulsado])
        




app = QApplication([])


window = MainWindow()


window.show()

app.exec()