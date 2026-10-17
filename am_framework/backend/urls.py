from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

"""
Define the urls for frontend request based on different tables
"""
urlpatterns = [
    path("aircraft/", views.AircraftTableView.as_view(), name="aircraftTable"),
    path("movement/", views.MovementTableView.as_view(), name="movementTable"),
    path("airport/", views.AirportTableView.as_view(), name="airportTable"),
    path("userprofile/", views.UserProfileTableView.as_view(), name="userProfileTable"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
