from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QGridLayout
import sys
from PyQt5.QtGui import QIcon



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("HBoxlayout")
         
        gird=QGridLayout()

        bt1=QPushButton("Click one")
        bt2=QPushButton("Click two")
        bt3=QPushButton("Click three")
        bt4=QPushButton("Click four")
        bt5=QPushButton("Click five")
        bt6=QPushButton("Click six")
        bt7=QPushButton("Click seven")
        bt8=QPushButton("Click eight")


        gird.addWidget(bt1, 0, 0)
        gird.addWidget(bt2, 0, 1)
        gird.addWidget(bt3, 0, 2)
        gird.addWidget(bt4, 0, 3)
        gird.addWidget(bt5, 1, 0)
        gird.addWidget(bt6, 1, 1)
        gird.addWidget(bt7, 1, 2)
        gird.addWidget(bt8, 1, 3)


        self.setLayout(gird)







app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())