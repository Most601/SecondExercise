from Tkinter import *
#from tkFileDialog   import askopenfilename  
import os.path
import sqlite3
import csv
from datetime import datetime
import math

def nmea(INPUT,TableName):
    conn = sqlite3.connect('C:\\Users\\Most601\\Downloads\\NMEA files\\nmea_to_db.db')
    c = conn.cursor()
    l = str(TableName)
    listName = l.split('.')
    print(list)
    # Create table
   # c.execute('drop table if exists' + str(listName[0]) )
    c.execute('''CREATE TABLE '''+ str(listName[0]) + '''
                         (date text,time text,speed float,latitude text,latitude_direction text,
                         longitude text,longitude_direction text,fix text,horizontal_dilution text,
                          altitude text,direct_of_altitude text,altitude_location text)''')

    with open(INPUT, 'r') as input_file:
        reader = csv.reader(input_file)
        #flag will tell us if the GPGGA is good if yes continue to the GPRMC
        flag = 0
        # create a csv reader object from the input file (nmea files are basically csv)
        for row in reader:
            # skip all lines that do not start with $GPGGA
            if not row:
                continue
            elif row[0].startswith('$GPGGA') and row[6]=='1':
                time = row[1]
                latitude = row[2]
                lat_direction = row[3]
                longitude = row[4]
                lon_direction = row[5]
                fix = row[6]
                numOfSat = row[7]
                horizontal = row[8]
                altitude = row[9]
                direct_altitude = row[10]
                altitude_location = row[11]
                flag = 1
                
            elif row[0].startswith('$GPRMC') and flag==1:
                speed = row[7]
                date = row[9]
                warning = row[2]
                if warning == 'V':
                    continue
                c.execute("INSERT INTO "+str(listName[0])+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(date,time,speed,
                                                                               latitude, lat_direction,
                                                                               longitude, lon_direction,fix,
                                                                               horizontal,altitude,
                                                                               direct_altitude,
                                                                               altitude_location))
            # Save (commit) the changes
                conn.commit()
                flag=0
            else:
                continue
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.commit()
    conn.close()

def toCSV():
    conn = sqlite3.connect("C:\Users\Most601\Downloads\NMEA files\nmea_to_db.db") #open db
    cursor = conn.cursor() #cursor to the db
    cursor.execute("select * from info;") # execute a sql script

    with open("out.csv", "wb") as csv_file: #writing to csv
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description]) # write headers
        csv_writer.writerows(cursor)

def addNmea():
    conn = sqlite3.connect('nmea_to_db.db')
    c = conn.cursor()

    
##############  NEW   ####################
def load():
    conn = sqlite3.connect('C:\\Users\\Most601\\Downloads\\NMEA files\\nmea_to_db.db')
    c = conn.cursor()
    tables = list(c.execute("select name from sqlite_master where type is 'table'"))
    
    c.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    
    INPUT = 'C:\\Users\\Most601\\Downloads\\NMEA files\\New folder'
    if os.path.isdir(INPUT):
        l = os.listdir(INPUT)
        for k in range(len(l)):
            nmea(INPUT + "\\"+l[k],l[k])

##################################

root = Tk()
root.title("NMEA TO CSV PROGRAM")
root.geometry("250x150")
app = Frame(root)
app.grid()

NmeaRunButton = Button(app , text = "Click to convert!" , command= load)
NmeaRunButton.pack()

ConvertToCSVbutton = Button(app , text = "Convert This NMEA to CSV!" , command = toCSV)
ConvertToCSVbutton.pack()

ConvertToKMLbutton = Button(app ,text = "Convert This NMEA to KML!")
ConvertToKMLbutton.pack()

GoogleEbutton = Button(app , text = "Show on Google Maps")
GoogleEbutton.pack()

L1 = Label(app, text="Enter Question:")
L1.pack(side = LEFT)

Question = Entry(app)
Question.pack(side = RIGHT)

mainloop()
