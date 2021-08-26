# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile, QIODevice, QTimer
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg
import psycopg2 as pgdatabase
from datetime import datetime

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

        self.setupButtonHandlers()


    def setupButtonHandlers(self):
        exptname = 'expt21test'
        self.ui.createDbButton.clicked.connect(lambda: createExptDatabase(exptname))
        self.ui.createTablesButton.clicked.connect(lambda: createTablesAnalysis(dbname=exptname))

    # Used to plot the experimental graphics
    def showExptStatus(self):
        self.x = [1.0, 2.0, 3.0]
        self.y = [10.0, 232.0, 1231.0]
        self.ui.imgArrivalPlot.setBackground('w')
        self.pen = pg.mkPen(color=(0, 0, 255))
        self.data_line = self.ui.imgArrivalPlot.plot(self.x, self.y, pen=self.pen)

    def updateRunStatus(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        self.y[0]  += 1
        self.y[1]  += 10
        self.y[2]  -= 100
        self.data_line.setData(self.x, self.y)


# Function will create a new database that will contain all tables 
# used/created in one experiment
def createExptDatabase(dbname, dbuser='postgres', dbpassword='postgres'):
    con = None
    try:
        con = pgdatabase.connect(user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit=True

        # check if there is a database named with the experiment
        # if not then create it
        cur.execute("""SELECT datname FROM pg_database""")
        rows = cur.fetchall()
        exptdatabaseExists = False
        for row in rows:
            if row[0] == dbname:
                exptdatabaseExists = True
    
        if exptdatabaseExists == True:
            msg=QMessageBox()
            msg.setText("Experiment already exists in database ...")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else:
            cur.execute("CREATE DATABASE " + str(dbname))
            print(f"Creating database for the current experiment with name: {dbname}")
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
        msg.QMessageBox()
        msg.setText(f"Expt database creation error {e}")
        msg.setIcon(QMessageBox.warning)
        msg.exec()
    
    finally:
        if con:
            con.close()

    
    # Create all the tables needed for the experiment, based on the options selected
def createTablesAnalysis(tables=['arrival', 'segmented', 'deadalive', 'growth'],
                     dbname=None, dbuser='postgres', dbpassword='postgres'):
    
    con = None

    try:
        con = pgdatabase.connect(database=dbname, user=dbuser, password=dbpassword)
        cur = con.cursor()

        # commit to database immediately
        con.autocommit=True
        # loop over and check if tables exist and clean them up
        cur.execute("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public'""")
        
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            if row[0] in tables:
                cur.execute("DROP TABLE IF EXISTS " + str(row[0]))
        
        print(f"Cleaned up all of the {tables} to start experiment afresh ... ")

        for table in tables:
            print(f"Table {table} is being created ....")
            if table == 'arrival':
                cur.execute("""CREATE TABLE arrival 
                        (id SERIAL PRIMARY KEY, time TIMESTAMP, position INT, timepoint INT)
                        """)
            elif table == 'segmented':
                cur.execute("""CREATE TABLE segmented
                        (id SERIAL PRIMARY KEY, time TIMESTAMP, position INT,
                        segmentedImagePath VARCHAR, rawImagePath VARCHAR, locations BYTEA)
                        """)
            
            elif table == 'deadalive':
                cur.execute("""CREATE TABLE deadalive
                        (id SERIAL PRIMARY KEY, time TIMESTAMP, position INT,
                        channelNumber INT, status BYTEA)
                        """)
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
        msg = QMessageBox()
        msg.setText(f"Database tables creation error {e}")
        msg.setIcon(QMessageBox.Warning)
        msg.exec()
    
    finally:
        if con:
            con.close()

# Clean up all the tables used in the experiment and drop the data, use this
# only in cases where you prematurely start and experiment
def cleanTablesAnalysis():
    pass

# Used only in debug mode to delete the database of a particular experiment
def cleanExptDatabase():
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
