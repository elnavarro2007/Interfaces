from Ej9 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(lambda : self.label_4.setStyleSheet("color:red;"))
        self.pushButton_2.pressed.connect(lambda : self.label_4.setStyleSheet("color:blue;"))
        self.pushButton_3.pressed.connect(lambda : self.label_4.setStyleSheet("color:green;"))
        self.pushButton_4.pressed.connect(lambda : self.label_4.setStyleSheet("font-family: Verdana, Geneva, Tahoma, sans-serif;"))
        self.pushButton_5.pressed.connect(lambda : self.label_4.setStyleSheet("font-family: Arial, Helvetica, sans-serif;"))
        self.pushButton_6.pressed.connect(lambda : self.label_4.setStyleSheet("font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;"))
        self.pushButton_7.pressed.connect(lambda : self.label_4.setStyleSheet("font-size: 12px;"))
        self.pushButton_8.pressed.connect(lambda : self.label_4.setStyleSheet("font-size: 10px;"))
        self.pushButton_9.pressed.connect(lambda : self.label_4.setStyleSheet("font-size: 14px;"))




app = QApplication([])
with open("Estilos/estilo7.qss","r") as f:
    app.setStyleSheet(f.read())


ventana = MainWindow()
ventana.show()
app.exec()