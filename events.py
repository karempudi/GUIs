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


        # enable sorting in the lists of positions
        self.ui.fastPositions.setSortingEnabled(True)
        self.ui.slowPositions.setSortingEnabled(True)

        # set button handlers
        self.setupButtonHandlers()

        self.finalizedPositions = False
        self.listFastPositions = []
        self.listSlowPositions = []

    def setupButtonHandlers(self):
        # By default get positions will fill in all the positions in Fast
        self.ui.getPositions.clicked.connect(self.setFastPositionsDefault)

        # Finalize positions will get final positions for both slow and fast
        self.ui.finalizePositions.clicked.connect(self.setFinalPositions)


        # Reset all positions and clean up
        self.ui.resetPositions.clicked.connect(self.resetAllPositions)

        # move from fast to slow
        self.ui.sendToSlow.clicked.connect(self.moveToSlow)

        # move from slow to fast
        self.ui.sendToFast.clicked.connect(self.moveToFast)
    
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
        print("Resetting all positions ... ")

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

