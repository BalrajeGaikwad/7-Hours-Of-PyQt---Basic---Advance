from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout
import sys
from PyQt5.QtGui import QIcon



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("HBoxlayout")
        #self.setWindowIcon(None)

        layout=QHBoxLayout()

        bt1=QPushButton("Click one")
        bt2=QPushButton("Click two")
        bt3=QPushButton("Click three")
        bt4=QPushButton("Click four")

        layout.addWidget(bt1)
        layout.addWidget(bt2)
        layout.addWidget(bt3)
        layout.addWidget(bt4)

        self.setLayout(layout)
        

app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())