from Tkinter import *
import os.path
import sqlite3
import csv
from datetime import datetime
import math


#This function operates and opens the database and writing to CSV file.
def toCSV():
    conn = sqlite3.connect("nmea_to_db.db")
    cursor = conn.cursor()
    INPUT = 'NMEAFiles'
    if os.path.isdir(INPUT):
        l = os.listdir(INPUT)
        for k in range(len(l)):
            spl = str(l[k])
            listName = spl.split('.')
            cursor.execute('SELECT * FROM '+str(listName[0]) )
            print "[ '"+str(listName[0])+"' , CSV FILE ]"
            with open("CSV\\"+listName[0]+".csv", "wb") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)
