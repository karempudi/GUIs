# File to write to database frequently
# We are testing reading and writing to database

import psycopg2 as pgdatabase

def createDatabaseAndTable(dbname='readWriteTest', table='plotter'):
    print(f"Creating database: {dbname} and table: {table}")

    con = None
    try:
        con = pgdatabase.connect()
        cur = con.cursor()
        con.autocommit = True

def deleteDatabaseAndTable(dbname='readWriteTest', table='plotter'):
    print(f"Deleting database: {dbname} and table: {table}")

def writeNewEntry(id):
    print(f"Writing entry with id: {id}")

if __name__ == "__main__":
    createDatabaseAndTable()
    for i in range(100):
        writeNewEntry(i)
    deleteDatabaseAndTable()


   