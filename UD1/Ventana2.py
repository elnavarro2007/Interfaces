from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel

class OtraVentana(QWidget):
   
    def __init__(self):
        super().__init__()

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel("Otra Ventana")
        plantilla.addWidget(self.etiqueta)

        self.setLayout(plantilla)

class MainWindow(QMainWindow): 
    
    def __init__(self): 
        super().__init__()  
        
        self.window = None

        boton = QPushButton("Púlsame!")
        boton.clicked.connect(self.mostrarOtraVentana)

        self.setCentralWidget(boton)

    def mostrarOtraVentana(self):
        if self.window.isVisible():
            self.window.hide()
        else: 
            self.window.show()
          

app = QApplication([])
window = MainWindow()
window.show()
app.exec()