from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QGridLayout,QGroupBox,QRadioButton,QDialog,QCheckBox,QLabel
import sys
from PyQt5.QtGui import QIcon



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)

        self.create_checkbox()

    def create_checkbox(self):
        hbox=QHBoxLayout()

        self.check1=QCheckBox("Football")
        self.check1.setIcon(QIcon('download.png'))
        #self.check1.setIconSize(Qs)
        self.check1.toggled.connect(self.item_selected)
        hbox.addWidget(self.check1)

        self.check2=QCheckBox("cricket")
        self.check2.setIcon(QIcon('download.png'))
        #self.check1.setIconSize(Qs)
        self.check2.toggled.connect(self.item_selected)
        hbox.addWidget(self.check2)

        self.check3=QCheckBox("tennis")
        self.check3.setIcon(QIcon('download.png'))
        #self.check1.setIconSize(Qs)
        self.check3.toggled.connect(self.item_selected)
        hbox.addWidget(self.check3)



        Vbox=QVBoxLayout()
        self.label=QLabel("Hello")


        Vbox.addWidget(self.label)

        Vbox.addLayout(hbox)
        self.setLayout(Vbox)

    def item_selected(self):
        value=""
        if self.check1.isChecked():
            value=self.check1.text()

        if self.check2.isChecked():
            value=self.check2.text()
        if self.check3.isChecked():
            value=self.check3.text()


        self.label.setText("You Have Selected : "+value)




app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())