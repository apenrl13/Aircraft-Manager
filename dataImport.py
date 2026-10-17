# DO NOT USE YET. Not set up for Django integration.

import csv
import mysql.connector


# read in starting data for aircraft_manager database
# Use the aircraft data to populate aircraft table
# Set up initial airports
# Use aircraft data to create initial entries in the movement table
def readcsv():
    aircraft = []
    with open("AircraftInfo.csv", "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for x in csvreader:
            aircraft.append(x)
    print(aircraft)
    # Add data to MySQL Database

    # Create Connection
    db = mysql.connector.connect(
        host="db", user="root", password="1qaz2wsx", database="aircraft_manager"
    )

    cursor = db.cursor()

    # Add admin user to userprofile
    sql = "INSERT INTO backend_userprofile(username,password,role) VALUES (%s,%s,%s)"
    val = ("admin", "thePassword", "corporate")
    cursor.execute(sql, val)
    db.commit()
    adminId = cursor.lastrowid
    # Add Airports to airporttable
    sql = "INSERT INTO backend_airporttable(airportCode,latitude,longitude,userId_id) VALUES(%s,%s,%s,%s)"
    val = ("KORD", 41.98, -87.90, adminId)
    cursor.execute(sql, val)
    db.commit()
    val = ("KLAX", 33.94, -118.40, adminId)
    cursor.execute(sql, val)
    db.commit()
    val = ("KJFK", 40.64, -73.77, adminId)
    cursor.execute(sql, val)
    db.commit()

    # Add to aircrafttable

    for entry in aircraft:
        sql = "INSERT INTO backend_aircrafttable(tailNumber,aircraftType,status,location,userId_id) VALUES(%s,%s,%s,%s,%s)"
        val = (entry[0], entry[1], entry[2], entry[3], adminId)
        cursor.execute(sql, val)
        db.commit()
        aircraftId = cursor.lastrowid
        # query = "SELECT airportId WHERE airporttable.airportCode = "
        # CREATE INITIAL MOVEMENT TABLE ENTRY
        sql = "INSERT INTO backend_movementtable(aircraftId_id,arrivalDate,departureDate,arrivalAirportId,userId_id) VALUES(%s,%s,%s,%s,%s)"
        if entry[3] == "KORD":
            val = (aircraftId, None, None, 1, adminId)
        elif entry[3] == "KLAX":
            val = (aircraftId, None, None, 2, adminId)
        else:
            val = (aircraftId, None, None, 3, adminId)

        cursor.execute(sql, val)
        db.commit()


if __name__ == "__main__":
    readcsv()
