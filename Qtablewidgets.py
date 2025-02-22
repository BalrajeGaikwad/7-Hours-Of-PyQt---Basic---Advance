from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QLabel,QCalendarWidget,QGridLayout
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QTime, QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("PyQt5 QLCDNumber")
        self.setWindowIcon(QIcon("download.png"))

        


    




app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())