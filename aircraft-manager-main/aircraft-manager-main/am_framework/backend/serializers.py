from rest_framework import serializers
from .models import *


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = aircrafttable
        fields = "__all__"


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = airporttable
        fields = "__all__"


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = movementtable
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = "__all__"
