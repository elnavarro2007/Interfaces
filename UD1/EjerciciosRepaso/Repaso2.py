from PyQt6.QtCore import QDate, QSize, Qt
from PyQt6.QtWidgets import QApplication, QMessageBox,QDateEdit, QHBoxLayout, QTextEdit, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget
from PyQt6.QtGui import QPixmap



   

       

        

        



class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()
        #Widget Principal
        widget = QWidget() #importante para mostrar la interfaz

        # Vertical y horizontal
        vertical = QVBoxLayout()
        fila1 = QHBoxLayout()
        fila2 = QHBoxLayout()
        fila3 = QHBoxLayout()
        fila4 = QHBoxLayout()
        fila5 = QHBoxLayout()
        fila6 = QHBoxLayout()

        #ventana



        
        self.setWindowTitle("App 1 ")

        # etiquetas 
        textoNombre = QLabel("Nombre")
        apellidos = QLabel("Apellidos")
        fechaAlta = QLabel("Fecha de Alta")
        departamento = QLabel("Departamento")


        

        # botones
        grabar = QPushButton("Grabar")
        resetear = QPushButton("reset")




        # Cuadros de texto
        self.cuadroNombre = QLineEdit()
        self.cuadroApellidos = QLineEdit()

        # Text Edit

                
        #Calendario
        self.calendario = QDateEdit()
        self.calendario.setCalendarPopup(True)
        self.calendario.setMinimumDate(QDate(2006,1,1))

        self.lista = QComboBox()
        self.lista.addItems(["Contbilidad","Administracion","Produccion"])


        



        #Filas 

        fila1.addWidget(textoNombre)
        fila1.addWidget(self.cuadroNombre)


        fila2.addWidget(apellidos)
        fila2.addWidget(self.cuadroApellidos)

        fila3.addWidget(fechaAlta)
        fila3.addWidget(self.calendario)

        fila4.addWidget(departamento)
        fila4.addWidget(self.lista)



        fila6.addWidget(grabar)
        fila6.addWidget(resetear)

        #Layouts
        vertical.addLayout(fila1)
        vertical.addLayout(fila2)
        vertical.addLayout(fila3)
        vertical.addLayout(fila4)
        vertical.addLayout(fila5)
        vertical.addLayout(fila6)


        # funcionalidades elementos
        grabar.clicked.connect(self.botonPulsado)
        resetear.clicked.connect(self.borrado)


        #layoutPrincipal
        widget.setLayout(vertical) # importante para mostrar la interfaz
        self.setCentralWidget(widget) # importante para mostrar la interfaz


    def borrado(self):
        self.cuadroNombre.setText("")
        self.cuadroApellidos.setText("")
        self.calendario.setDate(QDate(2006,1,1))
        self.lista.setCurrentIndex(0)

    def abrirVentana(self):
        self.vetana.show()


    def botonPulsado(self,s):
      dlg = QMessageBox(self)
      dlg.setWindowTitle("Cuadro de mensaje")
      dlg.setText(f"Si eres {self.cuadroNombre.text()} {self.cuadroApellidos.text()} pulsa si")
      dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
      dlg.setIcon(QMessageBox.Icon.Information)

      if dlg.exec() == QMessageBox.StandardButton.Yes:
         window.close()
      else:
         self.close
         self.cuadroNombre.setText("")
         self.cuadroApellidos.setText("")

    
        
        
        




        
    







        





app = QApplication([])

window = MainWindow()


window.show()

app.exec()