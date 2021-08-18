import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_eventswindow import Ui_EventsWindow

class EventsWindow(QMainWindow):

    def __init__(self):
        super(EventsWindow, self).__init__()
        self.ui = Ui_EventsWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Events Creation Window")


        # enable sorting in the lists of positions
        self.ui.fastPositions.setSortingEnabled(True)
        self.ui.slowPositions.setSortingEnabled(True)

        # set button handlers
        self.setupButtonHandlers()

        # set channel presets
        
        

        self.finalizedPositions = False
        self.listFastPositions = []
        self.listSlowPositions = []


    def setupButtonHandlers(self):
        # By default get positions will fill in all the positions in Fast
        self.ui.getPositionsButton.clicked.connect(self.setFastPositionsDefault)

        # Finalize positions will get final positions for both slow and fast
        self.ui.finalizePositionsButton.clicked.connect(self.setFinalPositions)


        # Reset all positions and clean up
        self.ui.resetPositionsButton.clicked.connect(self.resetAllPositions)

        # move from fast to slow
        self.ui.sendToSlowButton.clicked.connect(self.moveToSlow)

        # move from slow to fast
        self.ui.sendToFastButton.clicked.connect(self.moveToFast)

        # Add channel and exposure times to the list 
        self.ui.addPresetButton.clicked.connect(self.addPresetToList)

        # Remove the selected channels from the list
        self.ui.removePresetButton.clicked.connect(self.removePresetToList)

        # Construct events in the correct format
        self.ui.constructEventsButton.clicked.connect(self.constructFinalEvents)

        # Reset events
        self.ui.resetEventsButton.clicked.connect(self.resetFinalEvents)

        # Close window and clean up correctly
        self.ui.closeWindowButton.clicked.connect(self.closeWindow)

    def addPresetToList(self, clicked):
        print("Add preset to list")

    def removePresetToList(self, clicked):
        print("Remove preset from list")

    def constructFinalEvents(self, clicked):
        print("Construct final events pressed")

    def resetFinalEvents(self, clicked):
        print("Reset events pressed")

    def closeWindow(self, clicked):
        print("Window Closed Pressed")
    
    def setFastPositionsDefault(self, clicked):
        positions = getPositionList()
        for position in positions:
            self.ui.fastPositions.addItem(position)
    
    def setFinalPositions(self, clicked):
        if not self.finalizedPositions:
            nFastPositions = self.ui.fastPositions.count()
            nSlowPositions = self.ui.slowPositions.count()

            for i in range(nFastPositions):
                self.listFastPositions.append(self.ui.fastPositions.item(i).text())
            
            for i in range(nSlowPositions):
                self.listSlowPositions.append(self.ui.slowPositions.item(i).text())

            print("Final positions set .... ")
            print(self.listSlowPositions)
            print("---------------")
            print(self.listFastPositions)

            # set that you have finalized positions previously
            self.finalizedPositions = True

        else:
            msgBox = QMessageBox()
            msgBox.setText("You finalized positions previously.. Try resettting positons.")
            msgBox.exec()

        

    def resetAllPositions(self, clicked):
        self.ui.fastPositions.clear()
        self.ui.slowPositions.clear()
        self.finalizedPositions = False
        self.listFastPositions = []
        self.listSlowPositions = []
        msgBox = QMessageBox()
        msgBox.setText("All positions cleared. Reload positions")
        msgBox.exec()

    def moveToFast(self, clicked):
        selectedRow = self.ui.slowPositions.currentRow()
        selectedPosition = self.ui.slowPositions.takeItem(selectedRow)
        self.ui.fastPositions.addItem(selectedPosition)

    def moveToSlow(self, clicked):
        selectedRow = self.ui.fastPositions.currentRow()
        selectedPosition = self.ui.fastPositions.takeItem(selectedRow)
        self.ui.slowPositions.addItem(selectedPosition)




def getPositionList():
    positions = []
    for i in range(20):
        positions.append('Pos' + str(i))
    return positions


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    eventsWindow = EventsWindow()
    eventsWindow.show()

    sys.exit(app.exec())

