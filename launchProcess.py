import os
from pathlib import Path
from collections import OrderedDict
import sys
import torch.multiprocessing as tmp
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Signal, QProcess
from ui_testprocess import Ui_testProcess

def segment():
    for i in range(10):
        time.sleep(1)
        print(f"segment {i} done")

def track():
    for i in range(10):
        time.sleep(1)
        print(f"track {i} done")


class TestWindow(QMainWindow):

    def __init__(self):
        super(TestWindow, self).__init__()
        self.ui = Ui_testProcess()
        self.ui.setupUi(self)
        self.setWindowTitle("Process creation window")

        self.p = None

        self.setupButtonHandlers()

    def setupButtonHandlers(self):
        self.ui.processButton.clicked.connect(self.start_process)

    def message(self, s):
        self.ui.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:
            self.message("Executing Process.")
            self.p = QProcess()
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start("python", ["processScript.py", "100"])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)
    
    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: "Not running",
            QProcess.Starting: "Starting",
            QProcess.Running: "Running",
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    
    def process_finished(self):
        self.message("Process finished.")
        self.p = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())