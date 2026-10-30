from PyQt6.QtCore import QSize, Qt, QSize
from PyQt6.QtWidgets import QWidgetAction,QApplication,QToolBar ,QWidget,QTabWidget ,QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView,QSlider,QDial,QCalendarWidget,QGridLayout,QStackedLayout,QStatusBar
from PyQt6.QtGui import QPixmap, QAction,QIcon





class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()

        #etiqueta
        self.etiqueta = QLabel("Hola caracola")
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)




        #barra
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16,16))

        self.addToolBar(barra)


        #Botones y funciones
        self.boton2 = QAction("X",self)
        self.boton3 = QAction("Instagram",self)

        self.boton2.setStatusTip("Siguenos en x")
        self.boton3.setStatusTip("Siguenos en insta")



        #menu principal

        barra.addAction(self.boton2)
        barra.addAction(self.boton3)


        barra.addSeparator

        #Acciones subMenu1 y 2
        self.hola = QAction("hola",self)
        self.hola2 = QAction("hola2",self)



        self.hola3 = QAction("hola3",self)
        self.hola4 = QAction("hola4",self)


        self.hola5 = QAction("hola5",self)
        self.hola6 = QAction("hola6",self)



        #menu 
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        #Añadir menu y submenu
        menu_x = menu.addMenu("&Archivo")
        menu_x.addAction(self.hola)
        menu_x.addAction(self.hola2)



        menu_y = menu.addMenu("&Sexo Gratis")
        menu_y.addAction(self.hola3)
        menu_y.addAction(self.hola4)




        submenuHola = menu_y.addMenu("submenu")
        submenuHola.addAction(self.hola5)



        submenuHola2 = menu_y.addMenu("submenu2")
        submenuHola2.addAction(self.hola6)











       




app = QApplication([])

window = MainWindow()


window.show()

app.exec()
