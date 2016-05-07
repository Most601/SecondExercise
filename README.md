#Convert NMEA files to CSV or KML file using python

In this project we created a system that converting NMEA files to CSV (Comma-separated values) or KML (Keyhole Markup Language) file type using python language.  

**The system allows:**  
* Uploading NMEA files to database (we used MySQL).
* Selecting / filtering the wanted data from the NMEA files (height, velocity, etc ...).
* Choosing the file type to receive from database (KML or CSV).
* Producing the selected file.

##Introducing with NMEA (National Marine Electronics Association) files:

In this part of the project we have prepared a collection of NMEA files from the Internet and from our mobile phones:  
LG G3, Samsung 5, Sumsung 4s and iPhone 6s.  
The NMEA files was saved in different conditions: walking, driving in a car, flight and missile that was launched.  
In addition, we selected ***two*** software tools that allow visual display of NMEA files:

1. **VisualGPS 4.2 ([link to website](http://www.visualgps.net/visualgps/)):**  
      VisualGPS display graphically specific NMEA 0183 sentences and show the effects of selective availability (SA).  

      ***Features:***
      1. Azimuth and Elevation Graph: 
        * view all satellites that are in view.
        * plot and print the physical mask angle.
      2. Survey:
        * the survey window displays both position and xDOP (HDOP and VDOP) parameters.
        * monitor Standard Deviation and effects of Selective Availability.  Print the results graphically.
      3. Signal Quality/SNR Window: monitor satellite signal to noise ratios and see them graphically on the screen.
      4. NMEA Command Monitor: view NMEA sentences as they are received.  

2. **SatGen 3 ([link to website](http://www.labsat.co.uk/index.php/en/products/satgen-simulator-software)):**  
      SatGen NMEA is a very powerful, free piece of GPS Simulation software from Racelogic that allows you to create NMEA files and generate real-time NMEA serial streams.  

      ***Features:***
      1. Import NMEA file which contains GGA data directly into the software or alternatively to create a route in Google Earth, or build a profile using simple user commands.
      2. Create a static scenario, where a position can be manually inserted or easily determined using the integrated Google Maps screen.
      3. To draw a route by simply clicking-on a series of locations on the map.

##Planning the system:

In this part of the project we planned a system that allowing to load an NMEA files and save them in database.  
In addition , we added the possibility to produce from the database KML and CSV files.  
[Link to our UML](https://github.com/Most601/SecondExercise/blob/master/UMLmatala2.png)

##Creating the system:

In the final part of the project we created the program.  
Explanation what each python file does:  
**[NMEA_to_DB.py](https://github.com/Most601/SecondExercise/blob/master/NMEA_to_DB.py)-** upload NMEA files to database.  
**[DB_to_CSV.py](https://github.com/Most601/SecondExercise/blob/master/DB_to_CSV.py)-** convert NMEA files from database to CSV files.  
**[DB_to_KML.py](https://github.com/Most601/SecondExercise/blob/master/DB_to_KML.py)-** convert NMEA files from database to KML files.  
**[querytext.py](https://github.com/Most601/SecondExercise/blob/master/querytext.py)-** with a query that was asked returning the relevant information from the database.  
**[Main.py](https://github.com/Most601/SecondExercise/blob/master/Main.py)-** in the main file we use all the mentioned files to create a graphical user interface that lets the user to upload NMEA files and to choose which action he wants to perform: convert the NMEA files to CSV or KML files, enter a query or to see it on Google Earth.

##Our GUI:  

![gui](https://cloud.githubusercontent.com/assets/12721065/15091848/45b5a770-145f-11e6-9eb2-7b0b227f06cc.jpg)

## Authors:
* Idan Nahmias
* Aviv Levanon
* Maria Vinogradov
* Adir Harel
