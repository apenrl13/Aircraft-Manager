from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import aircrafttable, airporttable, movementtable, userprofile


"""
This class tests the get method of aircraft table with different filters.
Author: Alvin Cheng
"""


class MovementTableGetTest(TestCase):
    """
    Create some aircraft instances before each testing
    """

    @classmethod
    def setUpTestData(cls):
        # delete all entries in the tables first
        aircrafttable.objects.all().delete()
        airporttable.objects.all().delete()
        movementtable.objects.all().delete()
        userprofile.objects.all().delete()

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
                aircraftType="A330",
                status="Departured",
                location="ORD",
                userId=cls.rootUser,
            )
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

        cls.movements = []
        cls.movements.append(
            movementtable.objects.create(
                arrivalAirportId=cls.airports[0].airportId,
                originAirportId=cls.airports[1].airportId,
                arrivalDate="2021-10-01T12:00:00Z",
                departureDate="2021-10-01T10:00:00Z",
                aircraftId=cls.aircrafts[0],
                userId=cls.rootUser,
            )
        )
        cls.movements.append(
            movementtable.objects.create(
                arrivalAirportId=cls.airports[1].airportId,
                originAirportId=cls.airports[0].airportId,
                arrivalDate="2022-10-01T12:00:00Z",
                departureDate="2022-10-01T10:00:00Z",
                aircraftId=cls.aircrafts[1],
                userId=cls.rootUser,
            )
        )

        cls.client = APIClient()

    """
    This is a helper class that compares each fields between the aircraft get
    from database and the created aircraft.
    """

    def compareHelper(self, entryGot: dict, entryCreated: movementtable):
        self.assertEqual(entryGot["movementId"], entryCreated.movementId)
        self.assertEqual(entryGot["arrivalAirportId"], entryCreated.arrivalAirportId)
        self.assertEqual(entryGot["originAirportId"], entryCreated.originAirportId)
        self.assertEqual(entryGot["arrivalDate"], entryCreated.arrivalDate)
        self.assertEqual(entryGot["departureDate"], entryCreated.departureDate)
        self.assertEqual(entryGot["aircraftId"], entryCreated.aircraftId.aircraftId)
        self.assertEqual(entryGot["userId"], entryCreated.userId.userId)

    """
    Test with no filter, should return all entries
    """

    def test_movement_get_all_entries(self):
        # Send response with no parameters
        response = self.client.get("/api/movement/")
        # Check if status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if we get all 2 entries
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare each aircraft got from database with created aircrafts
        for i in range(len(data)):
            self.compareHelper(data[i], self.movements[i])

    """
    Test getting only one entry with primaryId
    """

    def test_movement_get_single_entry_with_primaryId(self):
        """
        Send get request with primary ID
        """
        for i in range(len(self.movements)):
            # Send response with primary key. should only get one entry
            response = self.client.get(f"/api/movement/?movementId={i+1}")
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.movements[i])

    """
    Test getting only one entry with Non-primary key field
    """

    def test_movement_get_single_entry_with_nonPrimaryKey(self):
        """
        Send get request with arrivalAirportId
        """
        for i in range(len(self.movements)):
            # Send request with tailNumber, should only get one entry
            response = self.client.get(
                f"/api/movement/?arrivalAirportId={i+self.airports[0].airportId}"
            )
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.movements[i])

        """
        Send get request with arrivalDate
        """
        # should only get one entry
        response = self.client.get(f"/api/movement/?arrivalDate=2022-10-01T12:00:00Z")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        """
        Send get request with arrivalDate range
        """
        # should only get one entry
        response = self.client.get(
            f"/api/movement/?arrivalDate=2022-10-01T12:00:00Z&arrivalDate2=2022-10-01T12:00:00Z"
        )
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        # should only get one entry
        response = self.client.get(
            f"/api/movement/?arrivalDate=2021-12-01T12:00:00Z&arrivalDate2=2022-12-01T12:00:00Z"
        )
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        """
        Send get request with departureDate range
        """
        # should only get one entry
        response = self.client.get(
            f"/api/movement/?departureDate=2022-10-01T10:00:00Z&departureDate2=2022-10-01T12:00:00Z"
        )
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        # should only get one entry
        response = self.client.get(
            f"/api/movement/?departureDate=2021-12-01T12:00:00Z&departureDate2=2022-12-01T12:00:00Z"
        )
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        """
        Send get request with aircraftId
        """
        # Send request with tailNumber, should only get one entry
        response = self.client.get(
            f"/api/movement/?aircraftId={self.airports[0].airportId}"
        )
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[0])

    """
    Test getting multiple entries with Non-primary ID field
    """

    def test_movement_get_multiple_entries_with_nonprimaryId(self):
        """
        Send get request with aircraftType
        """
        # Send request with userId, should get 2 entries
        response = self.client.get(f"/api/movement/?userId={self.rootUser.userId}")
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[0])
        self.compareHelper(data[1], self.movements[1])

    """
    Test getting entries with mutiple fields filter
    """

    def test_movement_get_entries_with_multiple_fields(self):
        """
        Use all fields to get the exact entry
        """
        for i, currMovement in enumerate(self.movements):
            url = (
                f"/api/movement/?movementId={currMovement.movementId}"
                f"&arrivalAirportId={currMovement.arrivalAirportId}"
                f"&originAirportId={currMovement.originAirportId}"
                f"&arrivalDate={currMovement.arrivalDate}"
                f"&departureDate={currMovement.departureDate}"
                f"&aircraftId={currMovement.aircraftId.aircraftId}"
                f"&userId={currMovement.userId.userId}"
            )
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.movements[i])

        """
        Use arrivalAirportId and originAirportId as filter
        """
        url = f"/api/movement/?arrivalAirportId={self.airports[0].airportId}&originAirportId={self.airports[1].airportId}"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 1)
        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[0])

        """
        Use arrivalDate and departureDate as filter
        """
        url = "/api/movement/?arrivalDate=2022-10-01T12:00:00Z&departureDate=2022-10-01T10:00:00Z"
        response = self.client.get(url)
        data = response.json()["data"]
        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        """
        Use arrivalDate and departureDate range as filter
        """
        url = "/api/movement/?arrivalDate=2021-10-01T12:00:00Z&arrivalDate2=2022-10-01T12:00:00Z&departureDate=2022-10-01T10:00:00Z"

        response = self.client.get(url)
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        url = "/api/movement/?arrivalDate=2021-10-01T12:00:00Z&arrivalDate2=2022-10-01T12:00:00Z&departureDate=2022-10-01T10:00:00Z&departureDate2=2023-10-01T10:00:00Z"
        response = self.client.get(url)
        data = response.json()["data"]
        self.assertEqual(len(data), 1)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[1])

        url = "/api/movement/?arrivalDate=2021-10-01T12:00:00Z&arrivalDate2=2022-10-01T12:00:00Z&departureDate=2021-10-01T10:00:00Z&departureDate2=2022-10-01T10:00:00Z"
        response = self.client.get(url)
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        self.compareHelper(data[0], self.movements[0])
        self.compareHelper(data[1], self.movements[1])

    """
    Test getting entries with non-existing fields filter
    """

    def test_movement_get_entries_with_nonexisting_fields(self):
        """
        Use non-existing fields to get all entries, all fields should be
        filtered.
        """
        url = f"/api/movement/?field1=var1&field2=var2"
        response = self.client.get(url)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertEqual(len(data), 2)

        # Compare aircraft got from database with created aircraft
        for i in range(2):
            self.compareHelper(data[i], self.movements[i])

        """
        Use non-existing fields with primary key to get the exact entry,
        non-existing fields should be filtered
        """
        for i in range(2):
            url = f"/api/movement/?field1=var1&field2=var2&movementId={i+1}"
            response = self.client.get(url)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare aircraft got from database with created aircraft
            self.compareHelper(data[0], self.movements[i])
