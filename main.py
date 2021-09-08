# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile, QIODevice, QTimer
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
from exptSetup import ExptSetupWindow
import pyqtgraph as pg
import psycopg2 as pgdatabase
from datetime import datetime



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Window")

        # timing of the experimental status plots
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateRunStatus)
        self.timer.start()

        self.showExptStatus()

        self.setupButtonHandlers()

        # window for setup
        self.setupWindow =  ExptSetupWindow()
        self.setupWindow.setupDone.connect(self.receivedExptSetup)
        self.setupWindow.analysisSetupDone.connect(self.receivedAnalysisSetup)

    def receivedExptSetup(self, exptSettings):
        pass

    def receivedAnalysisSetup(self, expt):
        pass

    def setupButtonHandlers(self):
        exptname = 'expt21test'
        self.ui.createDbButton.clicked.connect(lambda: createExptDatabase(exptname))
        self.ui.createTablesButton.clicked.connect(lambda: createTablesAnalysis(dbname=exptname))


        # setup button handler
        self.ui.setupButton.clicked.connect(self.showSetupWindow)
        # view setup 
        self.ui.viewExptSetupButton.clicked.connect(self.viewSetup)


    def showSetupWindow(self):
        self.setupWindow.show()

    def viewSetup(self):
        pass


    # Used to plot the experimental graphics
    def showExptStatus(self):
        self.numpy_arrival = np.eye(3)
        #self.ui.imgArrivalPlot.setBackground('w')
        #self.pen = pg.mkPen(color=(0, 0, 255))
        self.ui.imgArrivalPlot.setImage(self.numpy_arrival)
        self.ui.imgArrivalPlot.ui.histogram.hide()
        self.ui.imgArrivalPlot.ui.roiBtn.hide()
        self.ui.imgArrivalPlot.ui.menuBtn.hide()

    def updateRunStatus(self):
        self.numpy_arrival = np.eye(3)  + 1.0 
        self.ui.imgArrivalPlot.setImage(self.numpy_arrival)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
