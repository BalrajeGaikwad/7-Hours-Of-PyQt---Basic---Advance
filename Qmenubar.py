from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar,QAction
import sys
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 Menu")

        self.create_menu()



    def create_menu(self):
        main_menu=self.menuBar()
        filemenu=main_menu.addMenu("Files")


        newation=QAction(QIcon('heart-3d-printer.jpg'), "New", self)
        newation.setShortcut("Ctrl+N")
        filemenu.addAction(newation)

        saveation=QAction(QIcon('heart-3d-printer.jpg'), "save", self)
        saveation.setShortcut("Ctrl+s")
        filemenu.addAction(saveation)

        filemenu.addSeparator()

        copyation=QAction(QIcon('heart-3d-printer.jpg'), "copy", self)
        copyation.setShortcut("Ctrl+c")
        filemenu.addAction(copyation)

        Pasteation=QAction(QIcon('heart-3d-printer.jpg'), "New", self)
        Pasteation.setShortcut("Ctrl+N")
        filemenu.addAction(Pasteation)

        exitaction=QAction(QIcon('heart-3d-printer.jpg'),"Exit", self)
        exitaction.triggered.connect(self.close_window)

        filemenu.addAction(exitaction)        


    def close_window(self):
        self.close()


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())
