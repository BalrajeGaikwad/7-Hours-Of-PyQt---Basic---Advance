from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel,QMessageBox
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 QCombo Box")

        vbox=QVBoxLayout()

        self.combo=QComboBox()

        self.combo.addItem("Python")
        self.combo.addItem("java")
        self.combo.addItem("c++")
        self.combo.addItem("c#")
        self.combo.currentIndexChanged.connect(self.combo_selected)
        self.combo.currentIndexChanged.connect(self.popupbox)


        self.labei=QLabel("Hello")


        vbox.addWidget(self.combo)
        vbox.addWidget(self.labei)
        self.setLayout(vbox)


    def combo_selected(self):
        self.item=self.combo.currentText()
        self.labei.setText("You Selected :"+ self.item)
        

    def popupbox(self):
        #QMessageBox.warning(self, "You Selected :"+self.item )
        QMessageBox.warning(self, "Selection", f"You Selected: {self.combo.currentText()}")




if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())

    