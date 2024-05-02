from django.test import TestCase
from rest_framework.test import APIClient
from ..models import userprofile
import json

"""
This class tests the post method of userprofile table with different data format.
Author: Alvin Cheng
"""


class UserProfileTablePostTest(TestCase):
    """
    Set up API client before testing
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = APIClient()

    """
    Send the post request with all fields entered
    should return status 201 and be found in database
    """

    def test_userprofile_post_with_all_fields(self):
        # Crate an entry and send it in json format with Corporate Manager role
        data = {"username": "corporate123", "password": "12345678", "role": "Corporate"}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(userprofile.objects.filter(role="Corporate").exists())

        # Crate an entry and send it in json format with Facility Manager role
        data = {"username": "facility456", "password": "12345678", "role": "Facility"}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(userprofile.objects.filter(role="Facility").exists())

    """
    Send the post request with no fields entered
    should return status 400
    """

    def test_userprofile_post_with_no_fields(self):
        # Crate an empty entry and send it in json format
        data = {}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
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

    def test_userprofile_post_with_missing_fields(self):
        # Crate an entry with missing fields and send it in json format
        data = {"username": "user123"}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Crate an entry with missing fields and send it in json format
        data = {"password": "password456"}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

        # Crate an entry with missing fields and send it in json format
        data = {"role": "Facility"}
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is fail (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the resonse message
        self.assertEqual(
            response.json()["message"], "missing necessary fields in request body"
        )
        self.assertEqual(response.json()["success"], False)

    """
    Send the post request with extras fields entered.
    Extras fields will be ignored automatically.
    Resonse should return status 201 and be found in database
    """

    def test_userprofile_post_with_extra_fields(self):
        # Crate an entry with extra fields and send it in json format
        data = {
            "username": "facility456",
            "password": "12345678",
            "role": "Facility",
            "extraFiled1": "ABC",
            "extraFiled2": "XYZ",
        }
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(userprofile.objects.filter(role="Facility").exists())

        # Crate an entry with extra fields and send it in json format
        data = {
            "username": "corporate789",
            "password": "12345678",
            "role": "Corporate",
            "extraFiled1": "ABC",
            "extraFiled2": "XYZ",
        }
        response = self.client.post(
            "/api/userprofile/", json.dumps(data), content_type="application/json"
        )

        # Check if the response is success (status code 201)
        self.assertEqual(response.status_code, 201)
        # Check the resonse message
        self.assertEqual(response.json()["message"], "entry created")
        self.assertEqual(response.json()["success"], True)

        # Check if an entry was created in database
        self.assertTrue(userprofile.objects.filter(role="Corporate").exists())
