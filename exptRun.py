import multiprocessing as mp
import torch.multiprocessing as tmp
import argparse
import sys
import torch
from pathlib import Path
from PySide6.QtWidgets import QApplication
from main import MainWindow
from pycromanager import Acquisition
from skimage.io import imread
from functools import partial
from torchvision import transforms, utils
from queue import Empty

"""
Expt run class will hold all the information about
processes that run 
"""
class exptRun(object):

    def __init__(self):
        self.exptParameters = None
    
    def setParameters(self, exptParameters):
        self.exptParameters = exptParameters
    
    def segmenation(self):
        pass
    
    def deadAlive(self):
        pass
    
    def growthRates(self):
        pass

    def startProcesses(self):
        pass

def runApplication():
    # Create and run the experiment
    print("Starting experiment analysis")

    # create an experiment Run object and share it with 
    # the application to be able to start all the processes 

    expObject = exptRun()

    # Create the main loop of the application
    app = QApplication(sys.argv)
    window = MainWindow(exptObject = expObject)
    window.show()
    sys.exit(app.exec())


# Run this inside a QProcess in the main GUI window
if __name__ == "__main__":
    # Create and run the experiment
    print("Starting experiment analysis")

    # create an experiment Run object and share it with 
    # the application to be able to start all the processes 

    expObject = exptRun(None)

    # Create the main loop of the application
    app = QApplication(sys.argv)
    window = MainWindow(exptObject = expObject)
    window.show()
    sys.exit(app.exec())

