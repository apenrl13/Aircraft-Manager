from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import aircrafttable
from ..serializers import AircraftSerializer


class AircraftAPIViewTestCase(APITestCase):
    """
    Test cases for CRUD operations on AircraftTable via AircraftTableView.
    """

    @classmethod
    def setUpTestData(cls):
        # Create test user and set up authentication
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.client.login(username="testuser", password="testpassword")

        # Create test aircraft entries
        cls.aircraft1 = aircrafttable.objects.create(
            tailNumber="A12345",
            aircraftType="A320",
            status="Operational",
            location="JFK",
            userId=cls.user,
        )
        cls.aircraft2 = aircrafttable.objects.create(
            tailNumber="B67890",
            aircraftType="B737",
            status="Maintenance",
            location="LAX",
            userId=cls.user,
        )

        # URL for AircraftTableView
        cls.url = reverse(
            "aircraft-list"
        )  # Use the actual name you have given to the URL in your urls.py

    def test_get_aircraft_list(self):
        """
        Test retrieving a list of all aircraft entries.
        """
        response = self.client.get(self.url)
        aircrafts = aircrafttable.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_aircraft(self):
        """
        Test creating a new aircraft entry.
        """
        data = {
            "tailNumber": "C54321",
            "aircraftType": "A330",
            "status": "Operational",
            "location": "ORD",
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(aircrafttable.objects.count(), 3)
        self.assertEqual(aircrafttable.objects.get(tailNumber="C54321").location, "ORD")

    def test_update_aircraft(self):
        """
        Test updating an existing aircraft entry.
        """
        data = {"status": "In-flight"}
        response = self.client.put(
            reverse("aircraft-detail", args=[self.aircraft1.pk]), data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.aircraft1.refresh_from_db()
        self.assertEqual(self.aircraft1.status, "In-flight")

    def test_delete_aircraft(self):
        """
        Test deleting an aircraft entry.
        """
        response = self.client.delete(
            reverse("aircraft-detail", args=[self.aircraft2.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(aircrafttable.objects.filter(pk=self.aircraft2.pk).exists())


class FrontendReadOnlyAPIViewTestCase(APITestCase):
    """
    Test cases for verifying that the FrontendReadOnlyAPIView correctly
    restricts write operations while allowing read operations.
    """

    @classmethod
    def setUpTestData(cls):
        # Create test user and authenticate
        cls.user = User.objects.create_user(
            username="testuser", password="testuserpassword"
        )
        cls.client.login(username="testuser", password="testuserpassword")

        # Assuming there's a path named 'userprofile-list' in urls.py for GET requests
        cls.url = reverse("userprofile-list")  # Adjust based on your actual URL name

        # Create a sample user profile to test GET
        cls.sample_user_profile = userprofile.objects.create(
            username="sampleuser",
            password="samplepass",
            role=userprofile.roleChoice.ADMIN,
        )

    def test_get_user_profiles(self):
        """
        Ensure GET request is permitted and returns the list of user profiles.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Further checks can be added here to validate response data

    def test_post_user_profile(self):
        """
        Test POST requests are forbidden for read-only views.
        """
        data = {
            "username": "newuser",
            "password": "newpass",
            "role": userprofile.roleChoice.CORPORATE,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_user_profile(self):
        """
        Test PUT requests are forbidden for read-only views.
        """
        data = {"role": userprofile.roleChoice.FACILITY}
        response = self.client.put(
            reverse("userprofile-detail", args=[self.sample_user_profile.pk]),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_user_profile(self):
        """
        Test DELETE requests are forbidden for read-only views.
        """
        response = self.client.delete(
            reverse("userprofile-detail", args=[self.sample_user_profile.pk])
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
