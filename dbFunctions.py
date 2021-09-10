import psycopg2 as pgdatabase
from datetime import datetime
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

#######################################################
#######################################################
######## CREATING/DELETING DATABASE AND TABLES ########
#######################################################
#######################################################

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
            if row[-1] == dbname:
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
        msg = QMessageBox()
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
            if row[-1] in tables:
                cur.execute("DROP TABLE IF EXISTS " + str(row[-1]))
        
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
def cleanTablesAnalysis(tables=['arrival', 'segmented', 'deadalive', 'growth'],
                        dbname=None, dbuser='postgres', dbpassword='postgres'):
    
    con = None

    try:
        con = pgdatabase.connect(dbname=dbname, user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit = True
    
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
    
    finally:
        if con:
            con.close()


# Used only in debug mode to delete the database of a particular experiment
def cleanExptDatabase():
    pass



#######################################################
#######################################################
######## READING AND WRITING DATA TO DATABASE #########
#######################################################
#######################################################

def insertArrival():
    
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True

    try:
        for pos in range(1, 10):
            for tp in range(1, 5):
                cur.execute("""INSERT INTO arrival (id, time, position, timepoint)
                            VALUES (%s, %s, %s, %s)""", (5*(pos - 1) + tp, datetime.now(), pos, tp, ))
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()

def readArrivals():
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True
    try:

        cur.execute("""SELECT * FROM arrival""")
        result = cur.fetchall()
        
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
    
    finally:
        if con:
            con.close()

def insertSegmented():
    
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True

    try:
        for pos in range(1, 10):
            for tp in range(1, 5):
                cur.execute("""INSERT INTO arrival (id, time, position, timepoint)
                            VALUES (%s, %s, %s, %s)""", (5*(pos - 1) + tp, datetime.now(), pos, tp, ))
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()

def readSegmented():
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True
    try:

        cur.execute("""SELECT * FROM arrival""")
        result = cur.fetchall()
        
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
    
    finally:
        if con:
            con.close()

def insertdeadalive():
    
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True

    try:
        for pos in range(1, 10):
            for tp in range(1, 5):
                cur.execute("""INSERT INTO arrival (id, time, position, timepoint)
                            VALUES (%s, %s, %s, %s)""", (5*(pos - 1) + tp, datetime.now(), pos, tp, ))
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()

def readdeadalive():
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True
    try:

        cur.execute("""SELECT * FROM arrival""")
        result = cur.fetchall()
        
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
    
    finally:
        if con:
            con.close()

def insertGrowths():
    
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True

    try:
        for pos in range(1, 10):
            for tp in range(1, 5):
                cur.execute("""INSERT INTO arrival (id, time, position, timepoint)
                            VALUES (%s, %s, %s, %s)""", (5*(pos - 1) + tp, datetime.now(), pos, tp, ))
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()

def readGrowths():
    con = None
    con = pgdatabase.connect(dbname='expt21test', user='postgres', password='postgres')
    cur = con.cursor()
    con.autocommit = True
    try:

        cur.execute("""SELECT * FROM arrival""")
        result = cur.fetchall()
        
    except pgdatabase.DatabaseError as e:
        print(f"Error: {e}")
    
    finally:
        if con:
            con.close()
