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

        vbox=QVBoxLayout()
        self.calender=QCalendarWidget()
        self.calender.setGridVisible(True)
        self.calender.selectionChanged.connect(self.calender_data)

        self.label=QLabel("Hello")
        self.setFont(QFont("Sanserif",15))

        vbox.addWidget(self.calender)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calender_data(self):
        dateselected=self.calender.selectedDate()
        date_in_string=str(dateselected.toPyDate)

        self.label.setText("Date is :"+date_in_string)


    




app=QApplication(sys.argv)
Window=Window()
Window.show()
sys.exit(app.exec_())