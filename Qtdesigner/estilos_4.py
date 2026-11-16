from Ej6 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])


with open("Estilos/estilo3.qss","r") as f:
    app.setStyleSheet(f.read())

ventana = MainWindow()
ventana.show()
app.exec()