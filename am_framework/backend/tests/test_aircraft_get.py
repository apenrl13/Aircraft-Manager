from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import aircrafttable, userprofile


"""
This class tests the get method of aircraft table with different filters.
Author: Alvin Cheng
"""


class AircraftTableGetTest(TestCase):
    """
    Create some aircraft instances before each testing
    """

    @classmethod
    def setUpTestData(cls):
        cls.rootUser = userprofile.objects.create(
            username="root", password="1234", role="admin"
        )
        cls.aircrafts = []
        cls.aircrafts.append(
            aircrafttable.objects.create(
                tailNumber="111",
                aircraftType="A320",
                status="Departured",
                location="LAX",
                userId=cls.rootUser,
            )
        )
        cls.aircrafts.append(
            aircrafttable.objects.create(
                tailNumber="222",
                aircraftType="A320",
                status="Arrived",
                location="ORD",
                userId=cls.rootUser,
            )
        )
        cls.aircrafts.append(
            aircrafttable.objects.create(
                tailNumber="333",
                aircraftType="A330",
                status="Departured",
                location="ORD",
                userId=cls.rootUser,
            )
        )
        cls.client = APIClient()

    """
    This is a helper class that compares each fields between the aircraft 
    get from database and the created aircraft.
    """

    def compareHelper(self, aircraftGot: dict, aircraftCreated: aircrafttable):
        self.assertEqual(aircraftGot["aircraftId"], aircraftCreated.aircraftId)
        self.assertEqual(aircraftGot["tailNumber"], aircraftCreated.tailNumber)
        self.assertEqual(aircraftGot["aircraftType"], aircraftCreated.aircraftType)
        self.assertEqual(aircraftGot["status"], aircraftCreated.status)
        self.assertEqual(aircraftGot["location"], aircraftCreated.location)

    """
    Test with no filter, should return all entries of aircrafts
    """

    def test_aircraft_get_all_entries(self):
        # Send response with no parameters
        response = self.client.get("/api/aircraft/")
        # Check if status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if we get all three entries
        data = response.json()["data"]
        self.assertEqual(len(data), 3)

        # Compare each aircraft got from database with created aircrafts
        for i in range(len(data)):
            self.compareHelper(data[i], self.aircrafts[i])

    """
    Test getting only one entry with primaryId
    """

    def test_aircraft_get_single_entry_with_primaryId(self):
        """
        Send get request with primary ID
        """
        for i in range(len(self.aircrafts)):
            # Send response with primary ID (aircraftID) should only get one
            # entry
            response = self.client.get(f"/api/aircraft/?aircraftId={i+1}")
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.aircrafts[i])

    """
    Test getting only one entry with Non-primary ID field
    """

    def test_aircraft_get_single_entry_with_nonprimaryId(self):
        """
        Send get request with tailNumber
        """
        for i in range(len(self.aircrafts)):
            # Send request with tailNumber, should only get one entry
            response = self.client.get(f"/api/aircraft/?tailNumber={(i+1)*111}")
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.aircrafts[i])

        """
        Send get reqeust with aircraftType
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?aircraftType=A330")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[2])

        """
        Send get reqeust with status
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?status=Arrived")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[1])

        """
        Send get reqeust with location
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?location=LAX")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[0])

    """
    Test getting multiple entries with Non-primary ID field
    """

    def test_aircraft_get_multiple_entries_with_nonprimaryId(self):
        """
        Send get reqeust with aircraftType
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?aircraftType=A320")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[0])
        self.compareHelper(data[1], self.aircrafts[1])

        """
        Send get reqeust with status
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?status=Departured")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[0])
        self.compareHelper(data[1], self.aircrafts[2])

        """
        Send get reqeust with location
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/aircraft/?location=ORD")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[1])
        self.compareHelper(data[1], self.aircrafts[2])

    """
    Test getting entries with mutiple fields filter
    """

    def test_aircraft_get_entries_with_multiple_fields(self):
        """
        Use all fields to get the exact entry
        """
        for i, currAircraft in enumerate(self.aircrafts):
            url = (
                f"/api/aircraft/?aircraftId={currAircraft.aircraftId}"
                f"&tailNumber={currAircraft.tailNumber}&aircraftType={currAircraft.aircraftType}"
                f"&status={currAircraft.status}&location={currAircraft.location}"
            )
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.aircrafts[i])

        """
        Use aircraftType and status as filter
        """
        url = "/api/aircraft/?aircraftType=A320&status=Departured"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[0])

        """
        Use aircraftType and location as filter
        """
        url = "/api/aircraft/?aircraftType=A320&location=ORD"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[1])

        """
        Use status and location as filter
        """
        url = "/api/aircraft/?status=Departured&location=ORD"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.aircrafts[2])

    """
    Test getting entries with non-existing fields filter
    """

    def test_aircraft_get_entries_with_nonexisting_fields(self):
        """
        Use non-existing fields to get all entries, all fields should be
        filtered
        """
        url = f"/api/aircraft/?field1=var1&field2=var2"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 3)

        # Compare aircraft got from database with created aircraft
        for i in range(3):
            self.compareHelper(data[i], self.aircrafts[i])

        """
        Use non-existing fields with primary key to get the exact entry,
        non-existing fields should be filtered
        """
        for i in range(3):
            url = f"/api/aircraft/?field1=var1&field2=var2&aircraftId={i+1}"
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.aircrafts[i])
