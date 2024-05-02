from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import userprofile


"""
This class tests the get method of userprofile table with different filters.
Author: Alvin Cheng
"""


class UserProfileTableGetTests(TestCase):
    """
    Create some user instances before each testing
    """

    @classmethod
    def setUpTestData(cls):
        cls.users = []
        cls.users.append(
            userprofile.objects.create(username="root", password="123456", role="admin")
        )
        cls.users.append(
            userprofile.objects.create(
                username="corporate123", password="1qaz2wsx", role="corporate"
            )
        )
        cls.users.append(
            userprofile.objects.create(
                username="facility123", password="qwertyuio", role="facility"
            )
        )
        cls.client = APIClient()

    """
    This is a helper class that compares each fields between the user 
    get from database and the created user.
    """

    def compareHelper(self, userGot: dict, userCreated: userprofile):
        self.assertEqual(userGot["username"], userCreated.username)
        self.assertEqual(userGot["password"], userCreated.password)
        self.assertEqual(userGot["role"], userCreated.role)

    """
    Test getting the role with username and password
    """

    def test_userprofile_get_with_username_and_password(self):
        for user in self.users:
            # Send response with username and password should only get one entry
            url = f"/api/userprofile/?username={user.username}&password={user.password}"
            response = self.client.get(url)

            # Check if status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare user got from databases with created user
            self.compareHelper(data[0], user)

    """
    Test getting the role with only username or password
    """

    def test_userprofile_get_with_one_username_or_password(self):
        for user in self.users:
            # Send response with username should get no entry
            url = f"/api/userprofile/?username={user.username}"
            response = self.client.get(url)

            # Check if status code is 404 (fail)
            self.assertEqual(response.status_code, 404)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertIsNone(data)

            # Send response with password should get no entry
            url = f"/api/userprofile/?password={user.password}"
            response = self.client.get(url)

            # Check if status code is 404 (fail)
            self.assertEqual(response.status_code, 404)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertIsNone(data)

    """
    Test getting the role with no filter
    """

    def test_userprofile_get_with_no_filter(self):
        # Send response with no filter
        url = f"/api/userprofile/"
        response = self.client.get(url)

        # Check if status code is 404 (fail)
        self.assertEqual(response.status_code, 404)
        # Check if we get only one entry
        data = response.json()["data"]
        self.assertIsNone(data)

    """
    Test getting the role with extra filters
    """

    def test_userprofile_with_extra_filters(self):
        # Extra filters with username and password
        for user in self.users:
            # Send response with username, password and extra filter should only get one entry
            url = f"/api/userprofile/?username={user.username}&password={user.password}&f1=val1&f2=val2"
            response = self.client.get(url)

            # Check if status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertEqual(len(data), 1)

            # Compare user got from databases with created user
            self.compareHelper(data[0], user)

        # Extra filters with no username or password
        for user in self.users:
            # Send response with only extra filter should get no entry
            url = f"/api/userprofile/?f1=val1&f2=val2"
            response = self.client.get(url)

            # Check if status code is 404 (fail)
            self.assertEqual(response.status_code, 404)
            # Check if we get only one entry
            data = response.json()["data"]
            self.assertIsNone(data)
