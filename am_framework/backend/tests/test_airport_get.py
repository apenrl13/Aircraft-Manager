from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import airporttable, userprofile


"""
This class tests the get method of airport table with different filters.
Author: Alvin Cheng
"""


class AirportTableGetTest(TestCase):
    """
    Create some airport instances before each testing
    """

    @classmethod
    def setUpTestData(cls):
        cls.rootUser = userprofile.objects.create(
            username="root", password="1234", role="admin"
        )
        cls.airports = []
        cls.airports.append(
            airporttable.objects.create(
                airportCode="LAX",
                latitude=33.94,
                longitude=-118.41,
                numAircraft=10,
                userId=cls.rootUser,
            )
        )
        cls.airports.append(
            airporttable.objects.create(
                airportCode="ORD",
                latitude=41.98,
                longitude=-87.90,
                numAircraft=10,
                userId=cls.rootUser,
            )
        )
        cls.airports.append(
            airporttable.objects.create(
                airportCode="LGA",
                latitude=40.77,
                longitude=-73.87,
                numAircraft=15,
                userId=cls.rootUser,
            )
        )
        cls.client = APIClient()

    """
    This is a helper class that compares each fields between the airport
    get from database and the created airport.
    """

    def compareHelper(self, airportGot: dict, airportCreated: airporttable):
        self.assertEqual(airportGot["airportId"], airportCreated.airportId)
        self.assertEqual(airportGot["airportCode"], airportCreated.airportCode)
        self.assertAlmostEqual(
            float(airportGot["latitude"]), airportCreated.latitude, places=2
        )
        self.assertAlmostEqual(
            float(airportGot["longitude"]), airportCreated.longitude, places=2
        )
        self.assertEqual(airportGot["numAircraft"], airportCreated.numAircraft)

    """
    Test with no filter, should return all entries of airports
    """

    def test_airport_get_all_entries(self):
        # Send response with no parameters
        response = self.client.get("/api/airport/")
        # Check if status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if we get all three entries
        data = response.json()["data"]
        self.assertEqual(len(data), 3)

        # Compare each airport got from database with created airports
        for i in range(len(data)):
            self.compareHelper(data[i], self.airports[i])

    """
    Test getting only one entry with primaryId
    """

    def test_airport_get_single_entry_with_primaryId(self):
        """
        Send get request with primary ID
        """
        for i in range(len(self.airports)):
            # Send response with primary ID (airportID) should only get one
            # entry
            response = self.client.get(f"/api/airport/?airportId={i+1}")
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare airport got from database with created airport
            self.compareHelper(data[0], self.airports[i])

    """
    Test getting only one entry with Non-primary ID field
    """

    def test_airport_get_single_entry_with_nonprimaryId(self):
        """
        Send get request with airportCode
        """
        code = ["LAX", "ORD", "LGA"]
        for i in range(len(self.airports)):
            # Send request with tailNumber, should only get one entry
            response = self.client.get(f"/api/airport/?airportCode={code[i]}")
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare airport got from database with created airport
            self.compareHelper(data[0], self.airports[i])

        """
        Send get reqeust with latitude
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/airport/?latitude=33.94")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[0])

        """
        Send get reqeust with longitude
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/airport/?longitude=-87.90")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[1])

        """
        Send get reqeust with numAircraft
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/airport/?numAircraft=15")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[2])

    """
    Test getting multiple entries with Non-primary ID field
    """

    def test_airport_get_multiple_entries_with_nonprimaryId(self):
        """
        Send get reqeust with numAircraft
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(f"/api/airport/?numAircraft=10")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[0])
        self.compareHelper(data[1], self.airports[1])

    """
    Test getting entries with mutiple fields filter
    """

    def test_airport_get_entries_with_multiple_fields(self):
        """
        Use all fields to get the exact entry
        """
        for i, currAirport in enumerate(self.airports):
            url = (
                f"/api/airport/?airportId={currAirport.airportId}"
                f"&airportCode={currAirport.airportCode}&latitude={currAirport.latitude}"
                f"&longitude={currAirport.longitude}&numAircraft={currAirport.numAircraft}"
            )
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare airport got from database with created airport
            self.compareHelper(data[0], self.airports[i])

        """
        Use airportCode and numAircraft as filter
        """
        url = "/api/airport/?airportCode=LAX&numAircraft=10"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[0])

        url = "/api/airport/?airportCode=ORD&numAircraft=10"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare airport got from database with created airport
        self.compareHelper(data[0], self.airports[1])

    """
    Test getting entries with non-existing fields filter
    """

    def test_airport_get_entries_with_nonexisting_fields(self):
        """
        Use non-existing fields to get all entries, all fields should be
        filtered
        """
        url = f"/api/airport/?field1=var1&field2=var2"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 3)

        # Compare airport got from database with created airport
        for i in range(3):
            self.compareHelper(data[i], self.airports[i])

        """
        Use non-existing fields with primary key to get the exact entry,
        non-existing fields should be filtered
        """
        for i in range(3):
            url = f"/api/airport/?field1=var1&field2=var2&airportId={i+1}"
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare airport got from database with created airport
            self.compareHelper(data[0], self.airports[i])
