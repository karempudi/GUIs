# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice, QTimer
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # timing of the experimental status plots
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateRunStatus)
        self.timer.start()

        self.showExptStatus()

    def setupButtonHandlers(self):
        pass

    # Used to plot the experimental graphics
    def showExptStatus(self):
        self.x = [1.0, 2.0, 3.0]
        self.y = [10.0, 232.0, 1231.0]
        self.ui.imgArrivalPlot.setBackground('w')
        self.pen = pg.mkPen(color=(0, 0, 0))
        self.data_line = self.ui.imgArrivalPlot.plot(self.x, self.y, pen=self.pen)

    def updateRunStatus(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        self.y[0]  += 1
        self.y[1]  += 10
        self.y[2]  -= 100
        self.data_line.setData(self.x, self.y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())