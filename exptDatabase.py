import psycopg2 as pgdatabase
import argparse

"""
Useful for bundling all the database creation actions
and hold the information about the database
for a particular experiment, and some query funcitons
that can be called when you are updating the plots
in the main experiment window
"""
class exptDatabse(object):

    def __init__(self, dbname, user='postgres', password='postgres'
                tables=None):
        

    def createDatabase(self):
        pass
    
    def createTable(self):
        pass
    
    def deleteDatabase(self):
        pass
    
    def deleteTables(self):
        pass

    def deleteOneTable(self):
        pass
    
    def queryDataForPlots(self, tableName):
        pass
    

# If you ever want to use this in QProcess 
if __name__ == "__main__":
    print("Creating experiment database ...")