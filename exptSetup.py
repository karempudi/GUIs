import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, Qt
from ui_exptsetupwindow import Ui_SetupWindow
from events import EventsWindow



class ExptSetupWindow(QMainWindow):


    # Emit when setup is done and handled in the
    # parent window
    setupDone = Signal(dict)

    # analysis setup done, emit when setup is done
    analysisSetupDone = Signal(dict)

    def __init__(self):
        super(ExptSetupWindow, self).__init__()
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
        self.exptSetupData = None # assign later when the events windows closes
        self.exptDir = '.'
        self.exptSettings= {}

        # additional window references that are needed
        self.eventsWindow = EventsWindow()
        self.eventsWindow.eventsCreated.connect(self.receivedEvents)

        # analysis setting that need to be stored
        self.analysisSettings = {"cellNet": "normal", 
                    "channelSeg": None, "deadAlive": None, "growthRates": None}

    
    # Receiving events list from the create Events subwindow
    def receivedEvents(self, sentdata):
        self.exptSetupData = sentdata
        self.eventsCreated = True
        #print(self.events)
        print("Events received .... ")
        print("Events in the setup window are set ..")
    
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
        # checkbox for channel segmentation
        self.ui.segChannels.stateChanged.connect(self.setChannelSegmentation)
        # deadAlive for rudimentary tracking
        self.ui.calcDeadAlive.stateChanged.connect(self.setDeadAlive)
        # Growth Rates for full blown analysis
        self.ui.calcGrowthRates.stateChanged.connect(self.setGrowthRates)
        # validate analysis setup
        self.ui.validateAnalysisSetupButton.clicked.connect(self.validateAnalysisSetup)


        # save button and the close button
        self.ui.closeExptSetupButton.clicked.connect(self.closeWindow)
        

        
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
        self.eventsWindow.usePositionsFile = self.positionsFromFile 
        print(f"File option toggled {self.positionsFromFile}")


    def micromanagerOptionClicked(self, clicked):
        self.positionsFromFile = not self.ui.fromMicroManager.isChecked()
        self.eventsWindow.usePositionsFile = self.positionsFromFile
        print(f"Micromanger option toggled: {self.positionsFromFile}")

    def selectPositionsFile(self, clicked):
        if self.positionsFromFile == True:
            filename = QFileDialog.getOpenFileName(self, 
                self.tr("Open position file"), self.exptDir , self.tr("Position files (*.pos)"))

            self.positionsFileName = filename[0]
            print(filename)
            print(f"Positions file set to {self.positionsFileName}")

            # set positions filename so that positions can be picked up in
            # that window
            self.eventsWindow.positionsFileName = self.positionsFileName
            if self.positionsFileName == '':
                self.positionsFileName = None
                msg = QMessageBox()
                msg.setText("Positions file not set")
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Positions are coming from Micromanager directly")
            msg.exec()
        
    # Window gets created in the initialization
    # you just show it
    def createEvents(self, clicked):
        self.eventsWindow.show()
    
    def validateExptSetup(self, clicked):
        # Open a window and then ask a question to accept or not  
        if self.exptNo == None:
            msg = QMessageBox()
            msg.setText("Expt number not set")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            return
        
        if self.positionsFromFile == True and self.positionsFileName == None:
            msg = QMessageBox()
            msg.setText("Positions File name or micromanager option is not set")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            return
        
        # TODO: checking for micromanager option is done yet
        if self.positionsFromFile == False and self.eventsCreated == False:
            msg = QMessageBox()
            msg.setText("Micromanager events are not created ..")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            return

        if self.eventsCreated == False or self.exptSetupData == None:
            msg = QMessageBox()
            msg.setText("Events not created")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            return
        
        self.exptSettingsValidated = True
        # construct everything about experiment setup in a dictionary
        # to be passsed around if needed in other places

        self.exptSettings = {
            "events": self.exptSetupData['events'],
            "nPositions": self.exptSetupData['nPositions'],
            "slowPositions": self.exptSetupData['slowPositions'],
            "fastPositions": self.exptSetupData['fastPositions'],
            "nTimePoints": self.exptSetupData['nTimePoints'],
            "timeInterval": self.exptSetupData['timeInterval'],
            "exptNo": self.exptNo,
            "positionsFileName": self.positionsFileName,
            "posFromFile": self.positionsFromFile
        }
        self.setupDone.emit(self.exptSettings)
    
        msg = QMessageBox()
        msg.setText("Experiment settings validated")
        msg.setIcon(QMessageBox.Information)
        msg.exec()


    def setChannelSegmentation(self, s):
        self.analysisSettingsValidated = False
        if s == Qt.Checked:
            self.analysisSettings["channelSeg"] = True
        elif s == Qt.Unchecked:
            self.analysisSettings["channelSeg"] = None


    def setDeadAlive(self, s):
        self.analysisSettingsValidated = False
        if s == Qt.Checked:
            self.analysisSettings["deadAlive"] = True
        elif s == Qt.Unchecked:
            self.analysisSettings["deadAlive"] = None
    
    def setGrowthRates(self, s):
        self.analysisSettingsValidated = False
        if s == Qt.Checked:
            self.analysisSettings["growthRates"] = True
        elif s == Qt.Unchecked:
            self.analysisSettings["growthRates"] = None
    
    def validateAnalysisSetup(self, clicked):
        if self.exptSettingsValidated != True:
            msg = QMessageBox()
            msg.setText("Experimental setup not completed !!! Do it first")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            return
        
        if self.analysisSettings["channelSeg"] == None:
            msg = QMessageBox()
            msg.setText("Channel Segmentation will not be done ...")
            msg.setIcon(QMessageBox.Information)
            msg.exec()
        
        if self.analysisSettings["deadAlive"] == None:
            msg = QMessageBox()
            msg.setText("Dead Alive calcultations will not be done ...")
            msg.setIcon(QMessageBox.Information)
            msg.exec()
        
        if self.analysisSettings["growthRates"] == None:
            msg = QMessageBox()
            msg.setText("Growth Rates calcultations will not be done ...")
            msg.setIcon(QMessageBox.Information)
            msg.exec()

        self.analysisSettingsValidated = True
        self.analysisSetupDone.emit(self.analysisSettings)
        
        msg = QMessageBox()
        msg.setText("Analysis settings done")
        msg.setIcon(QMessageBox.Information)
        msg.exec()
    
    # close the window, just the view, the object still exists
    def closeWindow(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exptWindow = ExptSetupWindow()
    exptWindow.show()
    sys.exit(app.exec())
