from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel

class OtraVentana(QWidget):
   
   def __init__(self): # Creación de una función
        super().__init__() # LLamo al constructor del padre

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel()
        plantilla.addWidget(self.etiqueta)

        self.setLayout(plantilla)

class MainWindow(QMainWindow): # Creación de una clase
    
   def __init__(self): # Creación de una función
      super().__init__() # LLamo al constructor del padre
      
      self.window2 = OtraVentana()

      self.boton = QPushButton("Púlsame!")
      self.boton.clicked.connect(self.mostrarOtraVentana)

      self.input = QLineEdit()
      self.input.textChanged.connect(self.window2.etiqueta.setText)


      plantilla = QVBoxLayout()
      plantilla.addWidget(self.boton)
      plantilla.addWidget(self.input)

      contenedor = QWidget()
      contenedor.setLayout(plantilla)


      self.setCentralWidget(contenedor)

   def mostrarOtraVentana(self):
       self.window2.show()


          

app = QApplication([])
window = MainWindow()
window.show()
app.exec()