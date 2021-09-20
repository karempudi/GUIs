# File to write to database frequently
# We are testing reading and writing to database
import psycopg2 as pgdatabase
import time
import sys
from datetime import datetime

def createDatabase(dbname='readwritetest', 
        dbuser='postgres', dbpassword='postgres'):
    con = None
    try:
        con = pgdatabase.connect(user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit = True

        # check if db exists and delete it and start over,
        cur.execute("""SELECT datname FROM pg_database""")
        rows = cur.fetchall()
        testDbExists = False
        for row in rows:
            if row[-1] == dbname:
                testDbExists = True

        if testDbExists == True:
            cur.execute("DROP DATABASE " + str(dbname))
            sys.stdout.write("Database already exists .. so removing it\n")

        # create a new one
        cur.execute("CREATE DATABASE " + str(dbname))
        sys.stdout.write(f"Creating database {dbname}\n")
        sys.stdout.flush()
    except pgdatabase.DatabaseError as e:
        sys.stderr.write(f"Error in db creation process {e}\n")
        sys.stderr.flush()
    finally:
        if con:
            con.close()

def createTables(dbname, table='plotter',
        dbuser='postgres', dbpassword='postgres'):
    con = None
    try:
        con = pgdatabase.connect(database=dbname,user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit = True
        # check if table exists, otherwise create it and write
        # create table with schema to plot
        cur.execute("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public'""")

        rows = cur.fetchall()
        for row in rows:
            if row[-1] == table:
                cur.execute("DROP TABLE IF EXISTS " + str(row[-1]))
                sys.stdout.write("Dropped old table, creating a new one\n")

        cur.execute("""CREATE TABLE plotter
            (id SERIAL PRIMARY KEY, time TIMESTAMP, position INT, timepoint INT)
            """)
        sys.stdout.write(f"Created table plotter\n")
        sys.stdout.flush()
    except pgdatabase.DatabaseError as e:
        sys.stderr.write(f"Error in table creation function: {e}\n")
        sys.stderr.flush()
    finally:
        if con:
            con.close()


def createDatabaseAndTable(dbname='readwritetest', table='plotter',
            dbuser='postgres', dbpassword='postgres'):
    createDatabase(dbname=dbname)
    createTables(dbname=dbname, table=table)

def deleteDatabaseAndTable(dbname='readwritetest', table='plotter',
                dbuser='postgres', dbpassword='postgres'):
    con = None
    try:
        con = pgdatabase.connect(user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit = True
        # check if db exists and delete it and start over,
        cur.execute("""SELECT datname FROM pg_database""")
        rows = cur.fetchall()
        testDbExists = False
        for row in rows:
            if row[-1] == dbname:
                testDbExists = True

        if testDbExists == True:
            cur.execute("DROP DATABASE " + str(dbname))

    except pgdatabase.DatabaseError as e:
        sys.stderr.write(f"Error in deleting database and table {e}\n")
        sys.stderr.flush()
    finally:
        if con:
            con.close()
        sys.stdout.write(f"Deleting database: {dbname} and table: {table}\n")
        sys.stdout.flush()


def writeNewEntry(id, dbuser='postgres', dbpassword='postgres', 
        dbname='readwritetest', table='plotter'):

    con = None
    try:
        con = pgdatabase.connect(database=dbname, user=dbuser, password=dbpassword)
        cur = con.cursor()
        con.autocommit = True

        cur.execute("""INSERT INTO plotter  (id, time, position, timepoint)
                VALUES (%s, %s, %s, %s)""", (id, datetime.now(), id%10, id//10))
    
    except pgdatabase.DatabaseError as e:
        sys.stderr.write(f"Error in writing entry {id} : {e}\n")
        sys.stderr.flush()
    finally:
        if con:
            con.close()
        sys.stdout.write(f"Writing entry with id: {id}\n")
        sys.stdout.flush()
            



if __name__ == "__main__":
    createDatabaseAndTable()
    for i in range(100):
        writeNewEntry(i)
        time.sleep(0.3)
    #deleteDatabaseAndTable()
   