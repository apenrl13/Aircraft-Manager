import json
from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import fields
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone


class AircraftManagerAPIView(APIView):
    """Base class for RESTful API for table operations in Aircraft Manager"""

    """
    Constructor for AircraftManager class.
    
    :param pk: Field name of primary key of the table.
    :type pk: models.Model
    :param serializer: Serializer for entries of the table.
    :type serializer: serializers.ModelSerializer
    :param foreignKeyNames: List of field names that are foreign keys.
    :type foreignKeyNames: list
    """

    def __init__(
        self, model: models.Model, serializer, foreignKeyNames: list = [], **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.model: models.Model = model
        self.serializer: serializers.ModelSerializer = serializer
        self.pkName: str = self.model._meta.pk.name
        self.foreignKeyNames: list = foreignKeyNames
        # Get all field names (except pk) in the model
        self.modelFieldNames = []
        for f in self.model._meta.get_fields():
            if f.name != self.pkName and isinstance(f, (fields.Field)):
                self.modelFieldNames.append(f.name)

    def checkMissingFields(self, jsonDict: dict) -> bool:
        """
        Check if the dictionary has all the field
        required by the table (except primary key)
        """
        missingFields = []
        # Check for missing fields in the request body
        for fname in self.modelFieldNames:
            if fname not in jsonDict:
                missingFields.append(fname)
        return missingFields  # type: ignore

    def filterExistFields(self, queryDict: dict) -> dict:
        """Filter out fields in the table."""
        # Initialize a dictionary to store filters
        filters = {}
        queryItems = queryDict.items()
        # Iterate through query parameters and construct filters
        modelFieldNames = [f.name for f in self.model._meta.get_fields()]
        for fieldName, fieldValue in queryItems:
            # If the field exists in the model, Add filter to dictionary
            if fieldName in modelFieldNames:
                filters[fieldName] = fieldValue
        return filters

    def get(self, request):
        filters = self.filterExistFields(request.query_params)
        # Return all entries in the table if filter not specified
        if len(filters) == 0:
            all_entries = self.model.objects.all()
            serializer = self.serializer(all_entries, many=True)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "all entries returned since no filter specified",
                    "data": serializer.data,
                },
                status=200,
            )
        # Query the database with the filters
        targetObjectQueryset = self.model.objects.filter(**filters)
        if targetObjectQueryset.exists():
            serializer = self.serializer(targetObjectQueryset, many=True)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "found entries with specified conditions",
                    "data": serializer.data,
                },
                status=200,
            )

        # Specified entry not found, return a 404 status code
        return JsonResponse(
            data={
                "success": False,
                "message": "could not find entry with specified conditions",
                "data": None,
            },
            status=404,
        )

    def post(self, request):
        # convert request.body to a dictionary
        body = request.body.decode("utf-8")
        dataDict: dict = json.loads(body)
        # check if all fields are present
        missingFields = self.checkMissingFields(dataDict)
        if missingFields:
            return JsonResponse(
                data={
                    "success": False,
                    "message": "missing necessary fields in request body",
                    "data": None,
                },
                status=400,
            )
        filteredDataDict = self.filterExistFields(dataDict)
        # print("Filtered dict from JSON in Request Body: ", filteredDataDict)
        # if primary key is specified in the request body, ignore it
        if self.pkName in filteredDataDict:
            # print(
            #     "Found primary key in Dict:",
            #     filteredDataDict[self.pkName],
            #     ", ignoring.",
            # )
            del filteredDataDict[self.pkName]
        # handle foreign key fields
        notFoundForeignKeys: list = []
        for fkName in self.foreignKeyNames:
            if fkName in filteredDataDict:
                relatedModel = self.model._meta.get_field(fkName).related_model
                try:
                    # get the foreign key in the database
                    filteredDataDict[fkName] = relatedModel.objects.get(
                        pk=filteredDataDict[fkName]
                    )
                except ObjectDoesNotExist:
                    notFoundForeignKeys.append(
                        {
                            "key": fkName,
                            "value": filteredDataDict[fkName],
                            "model": relatedModel.__name__,
                        }
                    )
        # if there are foreign keys not found, return a 404 status code
        if notFoundForeignKeys:
            return JsonResponse(
                data={
                    "success": False,
                    "message": "foreign key(s) not found in foreign model(s)",
                    "data": notFoundForeignKeys,
                },
                status=404,
            )
        # create a new table entry
        newEntry = self.model(**filteredDataDict)
        newEntry.save()
        newEntrySerializer = self.serializer(newEntry)
        return JsonResponse(
            data={
                "success": True,
                "message": "entry created",
                "data": newEntrySerializer.data,
            },
            status=201,
        )

    def put(self, request):
        # convert request.body to a dictionary
        body = request.body.decode("utf-8")
        dataDict = json.loads(body)
        filteredDataDict = self.filterExistFields(dataDict)
        # print("Dict from JSON in Request Body: ", filteredDataDict)
        pkVal = filteredDataDict[self.pkName]
        # handle foreign key fields
        notFoundForeignKeys: list = []
        for fkName in self.foreignKeyNames:
            if fkName in filteredDataDict:
                relatedModel = self.model._meta.get_field(fkName).related_model
                try:
                    # get the foreign key in the database
                    filteredDataDict[fkName] = relatedModel.objects.get(
                        pk=filteredDataDict[fkName]
                    )
                except ObjectDoesNotExist:
                    notFoundForeignKeys.append(
                        {
                            "key": filteredDataDict[fkName],
                            "model": relatedModel.__name__,
                        }
                    )
        # if there are foreign keys not found, return a 404 status code
        if notFoundForeignKeys:
            return JsonResponse(
                data={
                    "success": False,
                    "message": "foreign key(s) not found in foreign model(s)",
                    "data": notFoundForeignKeys,
                },
                status=404,
            )
        # print("Primary key in Dict: ", pkVal)
        # check if primary key is already in the database
        if self.model.objects.filter(pk=pkVal).exists():
            # update the existing entry
            self.model.objects.filter(pk=pkVal).update(**filteredDataDict)
            entry = self.model.objects.get(pk=pkVal)
            serializer = self.serializer(entry)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "entry updated",
                    "data": serializer.data,
                },
                status=200,
            )
        # primary key not found
        return JsonResponse(
            data={"success": False, "message": "entry not found", "data": None},
            status=404,
        )

    def delete(self, request):
        # get the ID (primary key) from the request
        id = request.query_params.get(self.pkName, None)
        if not id:
            # ID not provided in request
            return JsonResponse(
                data={
                    "success": False,
                    "message": "ID invalid or not provided in request",
                    "data": None,
                },
                status=400,
            )
        try:
            # delete the entry with the specified primary key
            targetObject = self.model.objects.get(pk=id)
            targetObject.delete()
        except ObjectDoesNotExist:
            # primary key not found, return a 404 status code
            return JsonResponse(
                data={"success": False, "message": "entry not found", "data": None},
                status=404,
            )
        # entry deleted successfully
        return JsonResponse(
            data={"success": True, "message": "entry deleted", "data": None}, status=200
        )


class AircraftTableView(AircraftManagerAPIView):
    """
    RESTful API for AircraftTable operations.
    """

    def __init__(self, **kwargs) -> None:
        model = aircrafttable
        serializer = AircraftSerializer
        foreignKeyNames = ["userId"]
        super().__init__(
            model=model,
            serializer=serializer,
            foreignKeyNames=foreignKeyNames,
            **kwargs
        )


class AirportTableView(AircraftManagerAPIView):
    """
    RESTful API for AirportTable operations.
    """

    def __init__(self, **kwargs) -> None:
        model = airporttable
        serializer = AirportSerializer
        foreignKeyNames = ["userId"]
        super().__init__(
            model=model,
            serializer=serializer,
            foreignKeyNames=foreignKeyNames,
            **kwargs
        )


class MovementTableView(AircraftManagerAPIView):
    """
    RESTful API for MovementTable operations.
    Accept filtering in a range of `arrivalDate` and `departureDate`fields.
    """

    def __init__(self, **kwargs) -> None:
        model = movementtable
        serializer = MovementSerializer
        foreignKeyNames = ["userId", "aircraftId"]
        super().__init__(
            model=model,
            serializer=serializer,
            foreignKeyNames=foreignKeyNames,
            **kwargs
        )

    def filterExistFields(self, queryDict: dict, isGet=False) -> dict:
        superDict = super().filterExistFields(queryDict)

        # For GET method: mutant parameter for ranging filter for "*Date" fields
        if isGet:
            # make ranging criteria if `arrivalDate` and `arrivalDateEnd` appear
            if "arrivalDate" in queryDict:
                if "arrivalDate2" in queryDict:
                    # print("Found arrivalDate and arrivalDate2 in query parameters")
                    superDict["arrivalDate__range"] = [
                        queryDict["arrivalDate"],
                        queryDict["arrivalDate2"],
                    ]
                    del superDict["arrivalDate"]
            # make ranging criteria if `departureDate` and `departureDateEnd` appear
            if "departureDate" in queryDict:
                if "departureDate2" in queryDict:
                    # print("Found departureDate and departureDate2 in query parameters")
                    superDict["departureDate__range"] = [
                        queryDict["departureDate"],
                        queryDict["departureDate2"],
                    ]
                    del superDict["departureDate"]

        return superDict

    def get(self, request):
        filters = self.filterExistFields(request.query_params, isGet=True)
        # Return all entries in the table if filter not specified
        if len(filters) == 0:
            all_entries = self.model.objects.all()
            serializer = self.serializer(all_entries, many=True)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "all entries returned since no filter specified",
                    "data": serializer.data,
                },
                status=200,
            )
        # Query the database with the filters
        targetObjectQueryset = self.model.objects.filter(**filters)
        if targetObjectQueryset.exists():
            serializer = self.serializer(targetObjectQueryset, many=True)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "found entries with specified conditions",
                    "data": serializer.data,
                },
                status=200,
            )

        # Specified entry not found, return a 404 status code
        return JsonResponse(
            data={
                "success": False,
                "message": "could not find entry with specified conditions",
                "data": None,
            },
            status=404,
        )


class UserProfileTableView(AircraftManagerAPIView):
    """
    RESTful API for UserProfileTable operations.
    This table can only create or read from the frontend.
    """

    def __init__(self, **kwargs) -> None:
        model = userprofile
        serializer = UserSerializer
        foreignKeyNames = []  # type: ignore
        super().__init__(
            model=model,
            serializer=serializer,
            foreignKeyNames=foreignKeyNames,
            **kwargs
        )

    def get(self, request):
        filters = self.filterExistFields(request.query_params)

        # Return 404 status code if no username and password specified
        if filters.get("username") is None or filters.get("password") is None:
            return JsonResponse(
                data={
                    "success": False,
                    "message": "no username or password specified",
                    "data": None,
                },
                status=404,
            )

        # Query the database with the filters
        targetObjectQueryset = self.model.objects.filter(**filters)
        if targetObjectQueryset.exists():
            serializer = self.serializer(targetObjectQueryset, many=True)
            return JsonResponse(
                data={
                    "success": True,
                    "message": "found entries with specified conditions",
                    "data": serializer.data,
                },
                status=200,
            )

        # Specified entry not found, return a 404 status code
        return JsonResponse(
            data={
                "success": False,
                "message": "could not find entry with specified conditions",
                "data": None,
            },
            status=404,
        )

    def post(self, request):
        # convert request.body to a dictionary
        body = request.body.decode("utf-8")
        dataDict: dict = json.loads(body)
        # check if all fields are present
        missingFields = self.checkMissingFields(dataDict)
        if missingFields:
            return JsonResponse(
                data={
                    "success": False,
                    "message": "missing necessary fields in request body",
                    "data": None,
                },
                status=400,
            )
        filteredDataDict = self.filterExistFields(dataDict)

        # Check if username is used already
        if self.model.objects.filter(username=filteredDataDict["username"]).exists():
            return JsonResponse(
                data={"success": False, "message": "username used", "data": None},
                status=400,
            )

        # If primary key is specified in the request body, ignore it
        if self.pkName in filteredDataDict:
            # print(
            #     "Found primary key in Dict:",
            #     filteredDataDict[self.pkName],
            #     ", ignoring.",
            # )
            del filteredDataDict[self.pkName]

        # create a new table entry
        newEntry = self.model(**filteredDataDict)
        newEntry.save()
        newEntrySerializer = self.serializer(newEntry)
        return JsonResponse(
            data={
                "success": True,
                "message": "entry created",
                "data": newEntrySerializer.data,
            },
            status=201,
        )

    def delete(self, request):
        pass

    def put(self, request):
        pass


class FutureMovementAPIView(APIView):
    """
    API view to handle recording of future airplane movements by facility managers.

    This view ensures that only movements with a date and/or time in the future are recorded,
    aligning with the requirements for facility managers to schedule future airplane movements.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create new future airplane movements.

        Validates that the specified date and/or time for the airplane movement is in the future.
        If the validation passes, the movement is recorded; otherwise, an error is returned.

        :param request: The HTTP request object.
        :return: A Response object with creation status and data or error message.
        """
        serializer = MovementSerializer(data=request.data)

        if serializer.is_valid():
            movement_date = serializer.validated_data.get("arrivalDate")

            # Check if the movement date is indeed in the future.
            if movement_date and movement_date <= timezone.now():
                return Response(
                    {"error": "The movement date must be in the future."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Save the valid future movement to the database.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return validation errors if the data is not valid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
