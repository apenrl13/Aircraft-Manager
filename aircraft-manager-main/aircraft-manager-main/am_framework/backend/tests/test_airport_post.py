from django.test import TestCase
from rest_framework.test import APIClient
from ..models import airporttable, userprofile
import json

"""
This class tests the post method of airport table with different data format.
Author: Alvin Cheng
"""


class AirportTablePostTest(TestCase):
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

    def test_airport_post_with_all_fields(self):
        # Crate an entry and send it in json format
        data = {
            "airportCode": "LAX",
            "latitude": 33.94,
            "longitude": -118.41,
            "numAircraft": 10,
            "userId": self.rootUser.userId,
        }
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(airporttable.objects.filter(airportCode="LAX").exists())

    """
    Send the post request with no fields entered
    should return status 400
    """

    def test_airport_post_with_no_fields(self):
        # Crate an empty entry and send it in json format
        data = {}
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
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

    def test_airport_post_with_missing_fields(self):
        # Crate an entry with only airportCode and send it in json format
        data = {"airportCode": "LAX"}
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(airporttable.objects.filter(airportCode="LAX").exists())

        # Crate an entry with only latitude and send it in json format
        data = {"latitude": 33.94}
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(airporttable.objects.filter(latitude=33.94).exists())

        # Crate an entry with only longitude and send it in json format
        data = {"longitude": -118.41}
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(airporttable.objects.filter(longitude=-118.41).exists())

        # Crate an entry with only numAircraft and send it in json format
        data = {"numAircraft": 10}
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Check if the entry was created in database
        self.assertFalse(airporttable.objects.filter(numAircraft=10).exists())

    """
    Send the post request with extras fields entered.
    Extras fields will be ignored automatically.
    Resonse should return status 201 and be found in database
    """

    def test_airport_post_with_extra_fields(self):
        # Crate an entry and send it in json format
        data = {
            "airportCode": "LAX",
            "latitude": 33.94,
            "longitude": -118.41,
            "numAircraft": 10,
            "userId": self.rootUser.userId,
            "extraFiled1": "ABC",
            "extraFiled2": "XYZ",
        }
        response = self.client.post(
            "/api/airport/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(airporttable.objects.filter(airportCode="LAX").exists())
