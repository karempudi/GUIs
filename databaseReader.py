# Reading from database and plotting stuff
# Check for errors in the system, any deviation 
# will be made visible
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import pyqtgraph as pg
import numpy as np
import sys
from ui_dbplottest import Ui_dbPlotWindow
import psycopg2 as pgdatabase
import multiprocessing as mp
import time
from functools import partial

class hello(object):

    def __init__(self, x):
        self.x = x

    def hello_function(self, event):
        for i in range(self.x):
            sys.stdout.write(f"Time point is: {i}\n")
            sys.stdout.flush()
            time.sleep(1)

        while not event.is_set():
            sys.stdout.write("Process still alive\n")
            sys.stdout.flush()
            time.sleep(2)
    
        

class dbPlotWindow(QMainWindow):
    
    def __init__(self):
        super(dbPlotWindow, self).__init__()
        self.ui = Ui_dbPlotWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Window")

        self.setupButtonHandlers()

        self.writingProcess = None
        self.plottingStarted = None

        self.helloObject = hello(30)

        self.plotInitialize()

    def startPlotting(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start()

    def setupButtonHandlers(self):
        # start writing in a seperate process
        self.ui.startWriteButton.clicked.connect(self.startWriteProcess)

        # start plotting as soon as the button is clicked
        self.ui.startPlotButton.clicked.connect(self.startPlotting)

        # process button
        self.ui.processButton.clicked.connect(self.startNewPythonProcess)

        # terminate process
        self.ui.terminateButton.clicked.connect(self.terminateProcess)



    def startNewPythonProcess(self):

        self.event = mp.Event()
        self.newPythonProcess = mp.Process(target=self.helloObject.hello_function, args=(self.event,))
        self.newPythonProcess.start()
    
    def terminateProcess(self):
        self.event.set()


    # Launch the write process in a sub-process of the application
    def startWriteProcess(self):
        if self.writingProcess is None:
            print("Started db write process")
            self.writingProcess = QProcess()
            self.writingProcess.readyReadStandardOutput.connect(self.printOutputMessage)
            self.writingProcess.readyReadStandardError.connect(self.printErrorMessage)
            self.writingProcess.finished.connect(self.writingProcessFinished)
            self.writingProcess.start("python", ['databaseWriter.py'])

    def writingProcessFinished(self):
        print("Db writing process finsihed")
        self.writingProcess = None

    # initialize plotting
    def plotInitialize(self):
        self.numpy_arrival = np.zeros((10, 10))
        self.ui.plot.setImage(self.numpy_arrival, levels=(0, 1))
        self.ui.plot.ui.histogram.hide()
        self.ui.plot.ui.roiBtn.hide()
        self.ui.plot.ui.menuBtn.hide()
        self.scatterPlot = self.ui.scatterPlot.getPlotItem()
        self.scatterPlot.setLabel('left', text='position')
        self.scatterPlot.setLabel('bottom', text='position')
        self.scatterPlot.setTitle(title='Image Arrival')

    # update plots
    def updatePlot(self):
        # connect to database and update the plot
        con = None
        data = []
        try:
            con = pgdatabase.connect(database='readwritetest', user='postgres',
                        password='postgres')
            cur = con.cursor()
            con.autocommit = True

            # grab the selection
            cur.execute("SELECT position, timepoint from plotter")
            data = cur.fetchall()
            #print(len(data))
        except pgdatabase.DatabaseError as e:
            print(f"Database error during plot updates")
            data = []
        finally:
            if con:
                con.close()
            if len(data) == 0:
                data = []

        #print(data)
        # now use data to updateplot
        self.numpy_arrival = np.zeros((10, 10))
        for (i, (position, time)) in enumerate(data):
            self.numpy_arrival[int(position), int(time)] +=1
        if len(data) == 100:
            #print(self.numpy_arrival)
            print("100 points acquired\n")

        self.ui.plot.setImage(self.numpy_arrival, levels=(0, 1))
        self.scatterPlot.plot(np.array(data), symbol='o', pen=pg.mkPen(None))


        
    
    def printOutputMessage(self):
        data = self.writingProcess.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        print(stdout)
    
    def printErrorMessage(self):
        data = self.writingProcess.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        print(stderr)


if __name__ == "__main__":
    print("Db reader plotting, checking if there are any block issues ")
    app = QApplication(sys.argv)
    window = dbPlotWindow()
    window.show()
    sys.exit(app.exec())



