from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout,QGridLayout,QGroupBox,QRadioButton,QDialog,QCheckBox,QLabel,QLCDNumber
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime, QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("PyQt5 QLCDNumber")
        self.setWindowIcon(QIcon("download.png"))


        timer=QTimer()
        timer.timeout.connect(self.lcd_number)
        timer.start(1000)

        self.lcd_number()


    def lcd_number(self):
        vbox=QVBoxLayout()
        lcd=QLCDNumber()
        vbox.addWidget(lcd)
        time=QTime.currentTime()
        text=time.toString('hh:mm')

        lcd.display(text)

        self.setLayout(vbox)

    




app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())