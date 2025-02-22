from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QSpinBox
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Laptop Price Calculator")
        
        self.create_window()

    def create_window(self):
        vbox = QHBoxLayout()

        label = QLabel("Laptop Price:")
        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(1)  # Set minimum value to 1 to avoid multiplying by 0
        self.spinbox.valueChanged.connect(self.get_result)

        self.result = QLineEdit()
        self.result.setReadOnly(True)  # Make result field read-only

        vbox.addWidget(label)
        vbox.addWidget(self.lineedit)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.result)

        self.setLayout(vbox)

    def get_result(self):
        if self.lineedit.text() != "":
            try:
                price = int(self.lineedit.text())
                total_price = self.spinbox.value() * price
                self.result.setText(str(total_price))
            except ValueError:
                self.result.setText("Invalid input")  # Handle non-integer input


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
