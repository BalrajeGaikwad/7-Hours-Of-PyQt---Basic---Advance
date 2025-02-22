from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QMessageBox, QPushButton,QVBoxLayout,QLabel
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,200)
        self.setWindowTitle("Creating Message Box")
        self.creation()

    def creation(self):
        hbox=QHBoxLayout()

        button1=QPushButton("Warning")
        button1.clicked.connect(self.warning_msg)

        button2=QPushButton("Information")
        button2.clicked.connect(self.Info_msg)

        button3=QPushButton("About")
        button3.clicked.connect(self.about_msg)

        button4=QPushButton("Yes/No")
        button4.clicked.connect(self.multi_choice_msg)

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        hbox.addWidget(button4)

        vbox=QVBoxLayout()

        self.label=QLabel("Text")
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)



        self.setLayout(vbox)

    def warning_msg(self):
        QMessageBox.warning(self,"warning", "This is Warning Msg")

    def Info_msg(self):
        QMessageBox.warning(self,"Information", "This is Information MSG ")

    def about_msg(self):
        QMessageBox.about(self, "About","This is about Message")



    def multi_choice_msg(self):
        message=QMessageBox.question(self, " choice Message", "DO you Like Python ??", QMessageBox.Yes | QMessageBox.No)

        if message== QMessageBox.Yes:
            self.label.setText("Yes I Like Python")
        
        else:
            self.label.setText("No I Dont Like Python")


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())

    