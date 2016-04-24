from Tkinter import *
#from tkFileDialog   import askopenfilename  

import csv
import sqlite3
import math

def nmea():
    from datetime import datetime
    INPUT_FILENAME = "C:/Users/Sara/Desktop/20160401.nmea"
    with open(INPUT_FILENAME, 'r') as input_file:
        reader = csv.reader(input_file)
        conn = sqlite3.connect('nmea_to_db.db')
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS info')
        #flag will tell us if the GPGGA is good if yes continue to the GPRMC
        flag = 0
        # Create table
        c.execute('''CREATE TABLE info
                         (date text,
                         time text,
                         speed float,
                          latitude text,
                           latitude_direction text,
                            longitude text,
                             longitude_direction text,
                             fix text,horizontal_dilution text,
                             altitude text,
                             direct_of_altitude text,
                             altitude_location text)''')
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
                horizontal = row[7]
                altitude = row[8]
                direct_altitude = row[9]
                altitude_location = row[10]
                flag = 1
            elif row[0].startswith('$GPRMC') and flag==1:
                speed = row[7]
                date = row[9]
                warning = row[2]
                if warning == 'V':
                    continue
                c.execute("INSERT INTO info VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(date,time,speed, latitude, lat_direction, longitude, lon_direction,fix,horizontal,altitude,direct_altitude,altitude_location))
            # Save (commit) the changes
                conn.commit()
                flag=0
            else:
                continue
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def toCSV():
    conn = sqlite3.connect("C:/Users/Sara/Desktop/nmea_to_db.db") #open db
    cursor = conn.cursor() #cursor to the db
    cursor.execute("select * from info;") # execute a sql script

    with open("out.csv", "wb") as csv_file: #writing to csv
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description]) # write headers
        csv_writer.writerows(cursor)

def addNmea():
    conn = sqlite3.connect('nmea_to_db.db')
    c = conn.cursor()

root = Tk()
root.title("NMEA TO CSV PROGRAM")
root.geometry("250x150")
app = Frame(root)
app.grid()

NmeaRunButton = Button(app , text = "Click to convert!" , command= nmea)
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
