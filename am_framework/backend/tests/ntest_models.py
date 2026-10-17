from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import aircrafttable, airporttable, movementtable, userprofile

User = get_user_model()


class AircraftTableTestCase(TestCase):
    """
    Tests for creating and validating AircraftTable entries.
    """

    @classmethod
    def setUpTestData(cls):
        # Initialize test data for all test methods
        cls.test_user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )

        cls.aircraft1 = aircrafttable.objects.create(
            tailNumber="A12345",
            status="Operational",
            location="JFK",
            userId=cls.test_user,
        )
        cls.aircraft2 = aircrafttable.objects.create(
            tailNumber="B67890",
            status="Maintenance",
            location="LAX",
            userId=cls.test_user,
        )

    def test_aircraft_creation(self):
        """
        Verify that aircraft instances are successfully created and exist in the database.
        """
        self.assertTrue(aircrafttable.objects.filter(tailNumber="A12345").exists())
        self.assertTrue(aircrafttable.objects.filter(tailNumber="B67890").exists())

    def test_aircraft_fields(self):
        """
        Ensure the field values of aircraft instances are correctly saved and retrieved.
        """
        aircraft1 = aircrafttable.objects.get(tailNumber="A12345")
        self.assertEqual(aircraft1.status, "Operational")
        self.assertEqual(aircraft1.location, "JFK")
        self.assertEqual(aircraft1.userId, self.test_user)

        aircraft2 = aircrafttable.objects.get(tailNumber="B67890")
        self.assertEqual(aircraft2.status, "Maintenance")
        self.assertEqual(aircraft2.location, "LAX")
        self.assertEqual(aircraft2.userId, self.test_user)


class AirportTableTestCase(TestCase):
    """
    Tests for creating and validating AirportTable entries.
    """

    @classmethod
    def setUpTestData(cls):
        # Setup initial data for airport tests
        cls.test_user = User.objects.create_user(
            username="airportuser", password="testpassword456"
        )

        cls.airport1 = airporttable.objects.create(
            airportCode="LAX",
            latitude="33.9416",
            longitude="-118.4085",
            numAircraft=5,
            userId=cls.test_user,
        )
        cls.airport2 = airporttable.objects.create(
            airportCode="JFK",
            latitude="40.6413",
            longitude="-73.7781",
            numAircraft=8,
            userId=cls.test_user,
        )

    def test_airport_creation(self):
        """
        Verify that airport instances are successfully created and exist in the database.
        """
        self.assertTrue(airporttable.objects.filter(airportCode="LAX").exists())
        self.assertTrue(airporttable.objects.filter(airportCode="JFK").exists())

    def test_airport_fields(self):
        """
        Ensure the field values of airport instances are correctly saved and retrieved.
        """
        airport1 = airporttable.objects.get(airportCode="LAX")
        self.assertEqual(airport1.latitude, "33.9416")
        self.assertEqual(airport1.longitude, "-118.4085")
        self.assertEqual(airport1.numAircraft, 5)
        self.assertEqual(airport1.userId, self.test_user)

        airport2 = airporttable.objects.get(airportCode="JFK")
        self.assertEqual(airport2.latitude, "40.6413")
        self.assertEqual(airport2.longitude, "-73.7781")
        self.assertEqual(airport2.numAircraft, 8)
        self.assertEqual(airport2.userId, self.test_user)


class MovementTableTestCase(TestCase):
    """
    Tests for creating and validating MovementTable entries.
    """

    @classmethod
    def setUpTestData(cls):
        # Prepare initial data for movement tests
        cls.test_user = userprofile.objects.create(
            username="testmovementuser",
            password="password",
            role=userprofile.roleChoice.ADMIN,
        )

        cls.airport1 = airporttable.objects.create(
            airportCode="AAA",
            latitude="34.0522",
            longitude="-118.2437",
            numAircraft=10,
            userId=cls.test_user,
        )
        cls.airport2 = airporttable.objects.create(
            airportCode="BBB",
            latitude="40.7128",
            longitude="-74.0060",
            numAircraft=5,
            userId=cls.test_user,
        )
        cls.aircraft = aircrafttable.objects.create(
            tailNumber="N12345",
            aircraftType=aircrafttable.aType.A320,
            status="Operational",
            location="AAA",
            userId=cls.test_user,
        )
        cls.movement = movementtable.objects.create(
            arrivalAirportId=cls.airport1,
            originAirportId=cls.airport2,
            arrivalDate=timezone.now(),
            departureDate=timezone.now() - timezone.timedelta(days=1),
            aircraftId=cls.aircraft,
            userId=cls.test_user,
        )

    def test_movement_creation(self):
        """
        Confirm that movement instances are created and can be found in the database.
        """
        self.assertTrue(movementtable.objects.exists())

    def test_movement_fields(self):
        """
        Validate the stored values in movement instances match what was originally provided.
        """
        movement = movementtable.objects.get(pk=self.movement.pk)
        self.assertEqual(movement.arrivalAirportId, self.airport1)
        self.assertEqual(movement.originAirportId, self.airport2)
        self.assertEqual(movement.aircraftId, self.aircraft)
        self.assertEqual(movement.userId, self.test_user)


class UserProfileTestCase(TestCase):
    """
    Tests for creating and validating UserProfile entries.
    """

    @classmethod
    def setUpTestData(cls):
        # Initialize user profile test data
        cls.user1 = userprofile.objects.create(
            username="user1", password="pass1234", role=userprofile.roleChoice.ADMIN
        )
        cls.user2 = userprofile.objects.create(
            username="user2", password="pass5678", role=userprofile.roleChoice.FACILITY
        )

    def test_user_profile_creation(self):
        """
        Ensure user profile instances are successfully created and exist in the database.
        """
        self.assertTrue(userprofile.objects.filter(username="user1").exists())
        self.assertTrue(userprofile.objects.filter(username="user2").exists())

    def test_user_profile_fields(self):
        """
        Verify the accuracy of stored user profile fields against initial values.
        """
        user1 = userprofile.objects.get(username="user1")
        self.assertEqual(user1.username, "user1")
        self.assertEqual(user1.password, "pass1234")
        self.assertEqual(user1.role, userprofile.roleChoice.ADMIN)

        user2 = userprofile.objects.get(username="user2")
        self.assertEqual(user2.username, "user2")
        self.assertEqual(user2.password, "pass5678")
        self.assertEqual(user2.role, userprofile.roleChoice.FACILITY)
