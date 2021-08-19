import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Signal
from ui_exptsetupwindow import Ui_SetupWindow
from events import EventsWindow



class exptSetupWindow(QMainWindow):


    # Emit when setup is done and handled in the
    # parent window
    setupDone = Signal(object)

    def __init__(self):
        super(exptSetupWindow, self).__init__()
        self.ui = Ui_SetupWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Experiment Setup Window")

        # validataion Variables
        # Check names, positions reads, events and presets are all
        # correctly setup
        self.exptSettingsValidated = False
        # Check if all the algorithms are correctly marked,
        # All database tables are connected, created and ready to go
        self.analysisSettingsValidated = False

        # activate button handlers
        self.setupButtonHandlers()

        # Data that is needed tobe stored
        self.exptNo = None
        self.positionsFromFile = True
        self.positionsFileName = None # positions filename 
        self.eventsCreated = False # Flag to know if events were created
        self.events = None # assign later when the events windows closes
        self.exptDir = '.'

        # additional window references that are needed
        self.eventsWindow = EventsWindow()
        self.eventsWindow.eventsCreated.connect(self.receivedEvents)

    
    # Receiving events list from the create Events subwindow
    def receivedEvents(self, eventsList):
        self.events = eventsList
        self.eventsCreated = True
        #print(self.events)
        print("Events received .... ")
    
    def setupButtonHandlers(self):
        
        #########################################################
        ############## Expt Setup Buttons #######################
        #########################################################
        # expt No set button
        self.ui.exptNoSetButton.clicked.connect(self.setExptNo)
        # clear expt No button
        self.ui.exptNoClearButton.clicked.connect(self.clearExptNo)
        # click the get positions radio buttons
        # TODO: add stuff to get how you are going to get positions
        self.ui.fromFile.toggled.connect(self.fileOptionClicked)
        self.ui.fromMicroManager.toggled.connect(self.micromanagerOptionClicked)

        # select file button
        self.ui.fileSelectionButton.clicked.connect(self.selectPositionsFile)

        # create events button, opens new window
        self.ui.eventsCreationButton.clicked.connect(self.createEvents)

        # validate Expt setup button
        self.ui.validateExptSetupButton.clicked.connect(self.validateExptSetup)

        #########################################################
        ############## Analysis Setup Buttons ###################
        #########################################################
        
        # cell segmentaiton network selection

        # checkbox for channel segmentation

        # deadAlive for rudimentary tracking

        # Growth Rates for full blown analysis

        # validate analysis setup
        self.ui.validateAnalysisSetupButton.clicked.connect(self.validateAnalysisSetup)

        
    def setExptNo(self, clicked):
        if self.exptNo != None and (self.exptNo != self.ui.exptNoText.text()):
            dlg = QMessageBox()
            dlg.setWindowTitle("Please confirm!!!")
            dlg.setText(f"""Experiment no already set to {self.exptNo}.
                            Change to {self.ui.exptNoText.text()}""")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()

            if button == QMessageBox.Yes:
                self.exptNo = self.ui.exptNoText.text()
            elif button == QMessageBox.No:
                self.ui.exptNoText.setText(self.exptNo)
        else:
            self.exptNo = self.ui.exptNoText.text()

        print(f"Experiment no set to {self.exptNo}")
    
    def clearExptNo(self, clicked):
        self.exptNo = None
        self.ui.exptNoText.setText("EXP-21-BP000")

    def fileOptionClicked(self, clicked):
        self.positionsFromFile = self.ui.fromFile.isChecked()
        #print(f"File option toggled {self.positionsFromFile}")


    def micromanagerOptionClicked(self, clicked):
        self.positionsFromFile = not self.ui.fromMicroManager.isChecked()
        #print(f"Micromanger option toggled: {self.positionsFromFile}")

    def selectPositionsFile(self, clicked):
        if self.positionsFromFile == True:
            filename = QFileDialog.getOpenFileName(self, 
                self.tr("Open position file"), self.exptDir , self.tr("Position files (*.pos)"))

            self.positionsFileName = filename[0]
            print(filename)
            print(f"Positions file set to {self.positionsFileName}")
            if self.positionsFileName == '':
                self.positionsFileName = None
                msg = QMessageBox()
                msg.setText("Positions file not set")
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Positions are coming from Micromanager directly")
            msg.exec()
        
    def createEvents(self, clicked):
        self.eventsWindow.show()
    
    def validateExptSetup(self, clicked):
        # Open a window and then ask a question to accept or not  
        if self.exptNo == None:
            msg = QMessageBox()
            msg.setText("Expt number not set")
            msg.exec()
            return
        
        if self.positionsFromFile == True and self.positionsFileName == None:
            msg = QMessageBox()
            msg.setText("Positions File name is not set")
            msg.exec()
            return
        
        # TODO: checking for micromanager option is done yet

        if self.eventsCreated == False or self.events == None:
            msg = QMessageBox()
            msg.setText("Events not created")
            msg.exec()
            return
        
        self.exptSettingsValidated = True
        msg = QMessageBox()
        msg.setText("Experiment settings validated")
        msg.exec()

    
    def validateAnalysisSetup(self, clicked):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exptWindow = exptSetupWindow()
    exptWindow.show()
    sys.exit(app.exec())
