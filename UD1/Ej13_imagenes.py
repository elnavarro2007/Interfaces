from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout
from PyQt6.QtGui import QPixmap




class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Mi aplicacion")

        label = QLabel("Bajate los pantalones abuela ")
        label.setPixmap(QPixmap("img/adrity.jpg"))
        label.setScaledContents(True)



        formato = label.font()




        formato.setPointSize(50)
        formato.setFamily("Ink Free")
        formato.setBold(True)
        label.setFont(formato)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        self.setCentralWidget(label)
       







    

       

        


        



        




app = QApplication([])


window = MainWindow()


window.show()

app.exec()