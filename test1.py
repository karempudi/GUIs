from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Mother machine live analyzer")
        label = QLabel("This is awesome")

        self.setCentralWidget(label)

app = QApplication()
window1= MainWindow()
window1.show()

window2 = MainWindow()
window2.show()

app.exec()

