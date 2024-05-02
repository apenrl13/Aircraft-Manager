from django.test import TestCase
from rest_framework.test import APIClient
from ..models import aircrafttable, userprofile
import json

"""
This class tests the post method of aircraft table with different data format.
Author: Alvin Cheng
"""


class AircraftTablePostTest(TestCase):
    """
    Create a fake user and set up the API client before testing
    """

    @classmethod
    def setUpTestData(cls):
        cls.rootUser = userprofile.objects.create(
            username="root", password="1234", role="admin"
        )
        cls.client = APIClient()

    """
    Send the post request with all fields entered
    should return status 201 and be found in database
    """

    def test_aircraft_post_with_all_fields(self):
        # Crate an entry and send it in json format
        data = {
            "tailNumber": "111",
            "aircraftType": "A320",
            "status": "Departured",
            "location": "LAX",
            "userId": self.rootUser.userId,
        }
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(aircrafttable.objects.filter(tailNumber="111").exists())

    """
    Send the post request with no fields entered
    should return status 400
    """

    def test_aircraft_post_with_no_fields(self):
        # Crate an empty entry and send it in json format
        data = {}
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

    """
    Send the post request with only parts of fields entered
    should return status 400
    """

    def test_aircraft_post_with_missing_fields(self):
        # Crate an entry with only tailNumber and send it in json format
        data = {"tailNumber": "222"}
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(aircrafttable.objects.filter(tailNumber="222").exists())

        # Crate an entry with only aircraftType and send it in json format
        data = {"aircraftType": "A330"}
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(aircrafttable.objects.filter(aircraftType="A330").exists())

        # Crate an entry with only status and send it in json format
        data = {"status": "Arrived"}
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(aircrafttable.objects.filter(status="Arrived").exists())

        # Crate an entry with only location and send it in json format
        data = {"location": "ORD"}
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(aircrafttable.objects.filter(location="ORD").exists())

    """
    Send the post request with extras fields entered.
    Extras fields will be ignored automatically.
    Resonse should return status 201 and be found in database
    """

    def test_aircraft_post_with_extra_fields(self):
        # Crate an entry and send it in json format
        data = {
            "tailNumber": "111",
            "aircraftType": "A320",
            "status": "Departured",
            "location": "ORD",
            "userId": self.rootUser.userId,
            "extraFiled1": "ABC",
            "extraFiled2": "XYZ",
        }
        response = self.client.post(
            "/api/aircraft/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(aircrafttable.objects.filter(location="ORD").exists())
