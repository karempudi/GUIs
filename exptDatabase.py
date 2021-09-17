import psycopg2 as pgdatabase
import argparse

"""
Useful for bundling all the database creation actions
and hold the information about the database
for a particular experiment
"""
class exptDatabse(object):

    def __init__(self, dbname, user='postgres', password='postgres'
                tables=None):
        pass

    def createDatabase(self):
        pass
    
    def createTable(self):
        pass
    

# If you ever want to use this in QProcess 
if __name__ == "__main__":
    print("Creating experiment database ...")