import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_exptsetupwindow import Ui_SetupWindow


class exptSetupWindow(QMainWindow):

    def __init__(self):
        super(exptSetupWindow, self).__init__()
        self.ui = Ui_SetupWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Experiment Setup Window")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exptWindow = exptSetupWindow()
    exptWindow.show()
    sys.exit(app.exec())

