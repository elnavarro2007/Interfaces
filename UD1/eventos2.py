from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMenu, QWidget, QPushButton,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QCheckBox,QComboBox,QListWidget,QAbstractItemView
from PyQt6.QtGui import QPixmap,QAction





class MainWindow(QMainWindow): 

    def __init__(self):
      super().__init__()
      self.setWindowTitle("My app")


    def contextMenuEvent(self, e):
      context = QMenu(self)
      context.addAction(QAction("Abuelos pegando garrotazos a niños",self))
      context.addAction(QAction("Abuelos pegando garrotazos a bebes",self))
      context.addAction(QAction("Abuelos pegando garrotazos a franceses",self))
      context.exec(e.globalPos())





      

      





app = QApplication([])

window = MainWindow()


window.show()

app.exec()