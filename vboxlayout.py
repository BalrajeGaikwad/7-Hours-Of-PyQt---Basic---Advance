from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
from PyQt5.QtGui import QIcon



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("VBoxlayout")
        #self.setWindowIcon(None)

        vbox=QVBoxLayout()
        bt1=QPushButton("Click one")
        bt2=QPushButton("Click two")
        bt3=QPushButton("Click three")
        bt4=QPushButton("Click four")

        vbox.addWidget(bt1)
        vbox.addWidget(bt2)
        vbox.addWidget(bt3)
        vbox.addWidget(bt4)


        self.setLayout(vbox)




app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())