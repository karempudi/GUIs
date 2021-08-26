import psycopg2 as pgdatabase
from datetime import datetime

def writeToTable():
    
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

def readFromTable():
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

writeToTable()
results = readFromTable()