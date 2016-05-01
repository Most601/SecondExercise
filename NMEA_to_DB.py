from Tkinter import * 
import os.path
import sqlite3
import csv
from datetime import datetime
import math





###########  NMEA  ##############

def load():
    conn = sqlite3.connect('nmea_to_db.db')
    c = conn.cursor()
    tables = list(c.execute("select name from sqlite_master where type is 'table'"))
    c.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
    
    
    INPUT = 'NMEAFiles'
    if os.path.isdir(INPUT):
        l = os.listdir(INPUT)
        for k in range(len(l)):
            nmea(INPUT + "\\"+l[k],l[k])




def getRMCdata(row):
    warning = row[2]
    if warning == 'V':
        return
    time = row[1]
    latitude = row[3]
    lat_direction = row[4]
    longitude = row[5]
    lon_direction = row[6]
    speed = row[7]
    date =  row[9]
    listRMC = [speed,date,time,latitude,lat_direction,longitude,lon_direction]
    return listRMC

def nmea(INPUT,TableName):
    conn = sqlite3.connect('nmea_to_db.db')
    c = conn.cursor()
    l = str(TableName)
    listName = l.split('.')
    print(listName)
    # Create table
    c.execute('drop table if exists ' + str(listName[0]) )
    c.execute('''CREATE TABLE '''+ str(listName[0]) + '''
                         (time text ,latitude text,latitude_direction text,
                         longitude text,longitude_direction text,fix text,numOfSat, horizontal_dilution text,
                          altitude text,direct_of_altitude text,altitude_location text ,speed float ,date text)''')

    with open(INPUT, 'r') as input_file:
        reader = csv.reader(input_file)
        flag = 0
        for row in reader:
            # skip all lines that do not start with $GPGGA
            if not row:
                continue
            elif row[2] is None:  # if row[2] == None:
                continue
            elif row[2] == "":  # if row[2].len() == 0:
                continue
            elif "GGA" in row[0]  :
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
                c.execute("INSERT INTO "+str(listName[0])+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(time,
                                                                               latitude,
                                                                                lat_direction,
                                                                               longitude,
                                                                                lon_direction,
                                                                                fix,
                                                                                 numOfSat ,              
                                                                               horizontal,
                                                                                altitude,
                                                                               direct_altitude,
                                                                               altitude_location,' ',' ' ))

            elif "RMC" in row[0]:
                listRMC = getRMCdata(row)
                if( listRMC!= None):
                    c.execute("INSERT INTO " + str(listName[0]) + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (listRMC[2],listRMC[3],listRMC[4],listRMC[5],listRMC[6],' ',' ',' ',' ',' ',' ',listRMC[0],listRMC[1] ))
                    # Save (commit) the changes
                conn.commit()
                flag=0
            else:
                continue
    conn.commit()
    conn.close()
