#Second Exercise

In this project we focused on two subjects:

**1.** Precise and detailed planning of a software library.  
**2.** Writing the project in Python language and testing it on an agreed Benchmark.

##Task 0:

####Introducing with NMEA (National Marine Electronics Association) files:

In this part of the project we have prepared a collection of NMEA files from the Internet and from our mobile phones:  
LG G3, Samsung 5, Sumsung 4s and iPhone 6s.  
The NMEA files was saved in different conditions: walking, driving in a car, flight and missile that was launched.  
In addition, we selected ***two*** software tools that allow visual display of NMEA files:

1. **VisualGPS 4.2 ([link to website](http://www.visualgps.net/visualgps/)):**  
      VisualGPS display graphically specific NMEA 0183 sentences and show the effects of selective availability (SA).  
      *Features:* 1. Azimuth and Elevation Graph: 
        * view all satellites that are in view.
        * plot and print the physical mask angle.
      2. Survey:
        * the survey window displays both position and xDOP (HDOP and VDOP) parameters.
        * monitor Standard Deviation and effects of Selective Availability.  Print the results graphically.
      3. Signal Quality/SNR Window: monitor satellite signal to noise ratios and see them graphically on the screen.
      4. NMEA Command Monitor: view NMEA sentences as they are received.  

2. **SatGen 3 ([link to website](http://www.labsat.co.uk/index.php/en/products/satgen-simulator-software)):**  
      SatGen NMEA is a very powerful, free piece of GPS Simulation software from Racelogic that allows you to create NMEA files and generate real-time NMEA serial streams.  
      *Features:*
      1. Import NMEA file which contains GGA data directly into the software or alternatively to create a route in Google Earth, or build a profile using simple user commands.
      2. Create a static scenario, where a position can be manually inserted or easily determined using the integrated Google Maps screen.
      3. To draw a route by simply clicking-on a series of locations on the map.

##Task 1:

###Planning the system:

In this part of the project we planned a system that allowing to load an NMEA files and save them in database.  
In addition , we added the possibility to produce from the database KML (Keyhole Markup Language) and CSV (Comma-separated values) files.  
[Link to our UML](https://github.com/Most601/SecondExercise/blob/master/UMLmatala2.png)

##Task 2:

###Creating the system:

In the final part of the project we created the program.

## Authors:
* Idan Nahmias
* Aviv Levanon
* Maria Vinogradov
* Adir Harel
