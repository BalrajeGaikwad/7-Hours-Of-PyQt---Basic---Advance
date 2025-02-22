from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QGridLayout,QGroupBox,QRadioButton
import sys
from PyQt5.QtGui import QIcon



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("HBoxlayout")


        self.create_radio()

        vboc=QVBoxLayout()

        vboc.addWidget(self.groupbox)


        self.setLayout(vbocQ)


    def create_radio(self):
        self.groupbox=QGroupBox("What is your favourite sport ?")
        

        hbox=QHBoxLayout()

        self.r1=QRadioButton("Football")
        self.r1.setChecked(True)
        hbox.addWidget(self.r1) 


        self.groupbox.setLayout(hbox)        






app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())