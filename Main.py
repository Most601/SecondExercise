from Tkinter import * 
import os.path
import sqlite3
import csv
from datetime import datetime
import math
import os
import time

import DB_to_CSV as csv
import DB_to_KML as kml
import NMEA_to_DB as db
import querytext as querys

##################################


def showGoogleEarth():
    if os.path.isdir('KML'):
        l = os.listdir('KML')
        for k in range(len(l)):
            l2 = str(l[k])
            os.startfile('KML\\'+l2)
            time.sleep(5)



##################################

def querytxt():
    get = query.get()
    get1 = query1.get()
    comm = "select "+get+" from "+get1+";"
    
    querys.myquery(comm)
    return

def querytxt2():
    get = query2.get()
    querys.myquery(get)
    return


root = Tk()
root.title("NMEA TO CSV PROGRAM")
root.geometry("308x290")
app = Frame(root)
app.grid()
query = StringVar()
query1 = StringVar()
query2 = StringVar()

NmeaRunButton = Button(app , text = "Click to convert!" , command = db.load)
NmeaRunButton.pack()

ConvertToCSVbutton = Button(app , text = "Convert This NMEA to CSV!" , command = csv.toCSV)
ConvertToCSVbutton.pack()

ConvertToKMLbutton = Button(app ,text = "Convert This NMEA to KML!"  , command = kml.kml)
ConvertToKMLbutton.pack()

GoogleEbutton = Button(app , text = "Show on Google Maps"  , command =  showGoogleEarth)
GoogleEbutton.pack()

L1 = Label(app, text="Enter Query : ( Exm : data,time )")
L1.pack()

Question = Entry(app,width = 50, textvariable = query)
Question.pack()

L2 = Label(app, text="Enter NMEA File names ")
L2.pack()

Question1 = Entry(app,width = 30, textvariable = query1)
Question1.pack()

EnterQuery = Button(app , text = "Enter", command = querytxt)
EnterQuery.pack()

L3 = Label(app, text="Enter Query, notice this will be an SQL command! :")
L3.pack()

Question2 = Entry(app,width = 50, textvariable = query2)
Question2.pack()

EnterQuery1 = Button(app , text = "Enter", command = querytxt2)
EnterQuery1.pack()


mainloop()
