from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout


class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Mi aplicacion")

        label = QLabel("Hola ")

        formato = label.font()
        formato.setPointSize(50)
        formato.setFamily("Ink Free")
        formato.setBold(True)
        label.setFont(formato)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)


        self.setCentralWidget(label)
       







    

       

        


        self.setFixedSize(QSize(800,600))



        




app = QApplication([])


window = MainWindow()


window.show()

app.exec()