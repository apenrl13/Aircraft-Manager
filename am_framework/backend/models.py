from django.db import models

# The following model are adapted from
# InitialDatabase.sql placed in repo root directory


# Model for the aircrafttable which will hold the individual entries for aircraft
# The aircraftId is the primary key for the table
# tailNumber is the registration number of the aircraft
# type is the aircraft type
# status is the current status of the aircraft
# location is a foreign key to an airportId
class aircrafttable(models.Model):
    aircraftId = models.AutoField(primary_key=True)
    tailNumber = models.CharField(max_length=45, null=True)

    # Define a Django Enum type for the aircraft
    class aType(models.TextChoices):
        A320 = "A320", "A320"
        A321 = "A321", "A321"
        A330 = "A330", "A330"
        A350 = "A350", "A350"
        B737 = "B737", "B737"
        B757 = "B757", "B757"
        B767 = "B767", "B767"
        B787 = "B787", "B787"
        B777 = "B777", "B777"

    aircraftType = models.CharField(choices=aType, max_length=4, null=True)
    status = models.CharField(max_length=45, null=True)
    location = models.CharField(max_length=4, null=True)
    userId = models.ForeignKey("userprofile", on_delete=models.CASCADE, default=1)


# Table in database to store information about airports
# Contains columns for the primary key (airportId)
# AirportCode is the 4 letter ICAO Code.
# Latitude and Longitude for geolocation
# numAircraft to store number of aircraft currently at the airport
# userId store who created the airport
class airporttable(models.Model):
    airportId = models.AutoField(primary_key=True)
    airportCode = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    longitude = models.DecimalField(max_digits=7, decimal_places=3)
    numAircraft = models.IntegerField(null=True)
    userId = models.ForeignKey("userprofile", on_delete=models.CASCADE, default=1)


# Movement table to track all movements of aircraft between models
# This table is where most information and modifications of data will be contained
# The movementId is the primary key for the table
# arrivalAirportId is a foreign key to the arrival airport
# originAirportId is a foreign key to the origin airport
# arrivalDate is a datetime field to determine when a plane arrived
# departureDate is a datetime field to determine when a plane left an airport. Should originally be null
# aircraftId is a foreign key to the aircraft being moved
# userId is a foreign key to the user initiating the movement
class movementtable(models.Model):
    movementId = models.AutoField(primary_key=True)
    arrivalAirportId = models.IntegerField(null=True)
    originAirportId = models.IntegerField(null=True)
    arrivalDate = models.DateTimeField(max_length=8, null=True)
    departureDate = models.DateTimeField(max_length=8, null=True)
    aircraftId = models.ForeignKey("aircrafttable", on_delete=models.CASCADE, default=1)
    userId = models.ForeignKey("userprofile", on_delete=models.CASCADE, default=1)


# The userId controls authorization for the program and stores user info
# userId is the primary key for the usertable
# The username is the login name
# the password is self explanitory
# role is the permission level for the user.
class userprofile(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    # Limit roles to preset conditions
    class roleChoice(models.TextChoices):
        ADMIN = "admin", "Admin"
        CORPORATE = "corporate", "Corporate"
        FACILITY = "facility", "Facility"

    role = models.CharField(choices=roleChoice, max_length=9, null=True)


# @qxu229: the model is not migrated to the database
# Config the database setting in ../am_framework/settings.py first
# Then run `python manage.py makemigrations` and `python manage.py migrate`
# to create the table in the database
# NOTE: DO NOT DIRECTLY RUN SQL COMMANDS TO CREATE TABLES,
# or Django will not be able to manage them
#
