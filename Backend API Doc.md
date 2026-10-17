# Backend API Documentations

This is the documentation of backend APIs.

This documentation covers interfaces in `/am_backend/backend/views.py`. Models used across the backend request handling are explicitly written in `/am_backend/backend/models.py`.

## Common URLs and response

### URLs

APIs has common parent URL scheme `{baserurl}/api/{apisetname}`, where:

- `{baserurl}` is the **domain name / base URL** of backend server.
- `{apisetname}` is the **path** of an API set to access any specific database table. This is defined by each API set itself.

### Table field types

| Type            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `int`           | Integer.                                                     |
| `varchar(n)`    | String, with maximum length being `n`.                       |
| `decimal(m, n)` | Decimal number, with `m` total digits and `n` decimal digits. |
| `datetime(n)`   | Date & time, with maximum precision of seconds being `n` decimal digits.<br />If passed in a string (e.g. a parameter in an HTTP request), then the string should have this format: `"%Y-%m-%dT%H:%M:%SZ"`. <br />Example: String `"2022-02-01T14:01:01Z"` represents for `02/01/2022 2:01:01 PM`. |
| `choice`        | Field values should be **one of the given choices.** Choices will be indicated below in this documentation. |



### Response

The response is a `django.http.JsonResponse`  with standard HTTP status code. Its `JSON object` has the following format:

```json
{
    "success": False, # boolean
    "message": "sample", # string
    "data": null # arbitrary type, can either be null or a list of JSON object
}
```

## Base class `AircraftManagerAPIView`

Inherits Django REST Framework API base class `APIView`, and is the base class of APIs handling requests from frontend for database entries; cannot be instantiated directly for use.

It provides a basic layer of abstraction, and all API sets accessing specific tables are based on it.

#### Notes

- Invalid or non-existing field names in parameters / request bodies will be **ignored when parsing**, and **no error will be given** in the response.
- **Unless otherwise stated, API sets have the same scheme as defined in the base class.**

### HTTP Request Interfaces

#### `GET` request

##### Request Usage

- URL Scheme: `{apisetname}/?field1=val1&field2=val2&...`
- Body: None

##### Description

Get entries from the target table, with no or an arbitrary number of filtering criteria being `field1 = val1`, `field2 = val2`, and so on.

Criteria specifying invalid or non-existing field names will be **ignored when parsing**, and **no error will be given** in the response.

**NOTE:** if there is *no valid* filtering criterion, the response will contain **all entries in the target table**.

##### Response

- `success: "False"` if no entry matches given criteria.

  - Status code will be `HTTP 400`.
  - `data` item will be `null`.
  - `"message": "could not find entry with specified conditions"` will be given.
- `success: "True"` if there exists valid entries matching given criteria, OR no valid filtering criteria is given.

  - Status code will be `HTTP 200`.
  - `data` item will be a JSON list, containing valid entries as serialized JSON objects.
  - `"message": "all entries returned since no filter specified"` will be given, if no valid filtering criteria is given.
  - `"message": "found entries with specified conditions"` will be given, if valid filtering criteria are given AND there exists valid entries matching given criteria.

#### `POST` request

##### Request Usage

- URL Scheme: `{apisetname}/`
- Body: JSON object containing field name and corresponding values of the table.

##### Description

Create entries from the target table with corresponding field names and values.

**NOTE:** Invalid or non-existing field names will be **ignored when parsing**, and **no error will be given** in the response.

##### Response

- `success: "False"` if one or more fields (**except primary keys**) of the table are not presented in the request.
  
  - Status code will be `HTTP 400`.
  - `data` item will be `null`.
  - `"message": "missing necessary fields in request body"` will be given.
- `success: "False"` if at least one foreign key cannot be found in its corresponding database table.
  - Status code will be `HTTP 404`.
  - `data` item will be a JSON list containing JSON objects. Each object has the following format:
    ```json
    {
        "key": "Field Name of Foreign Key",
        "value": "Value of Foreign Key in request",
        "model": "Name of Model this Foreign Key related to"
    }
    ```
  - `"message": "foreign key(s) not found in foreign model(s)"` will be given.
- `success: "True"` if an entry has been created successfully.
  - Status code will be `HTTP 200`.
  - `data` item will be a JSON list, containing a single JSON object serialized from the entry just created in the table.
  - `"message": "entry created"` will be given.

#### `PUT` request

##### Request Usage

- URL Scheme: `{apisetname}/`
- Body: JSON object containing:
  - Primary key of the entry you want to modify.
  - Field names (keys) and corresponding values of the table.

##### Description

Modify the entry with specified primary key value from the target table with corresponding field names and values.

**NOTE:** Primary keys presented in requests will be **ignored**, since they are auto-increment in tables.

##### Response

- `success: "False"` if the entry specified in the request body cannot be found.
  - Status code will be `HTTP 404`.
  - `data` item will be `null`.
  - `"message": "entry not found"`will be given.
- `success: "False"` if at least one foreign key cannot be found in its corresponding database table.
  - Status code will be `HTTP 404`.
  - `data` item will be a JSON list containing JSON objects. Each object has the following format:
    ```json
    {
        "key": "Field Name of Foreign Key",
        "value": "Value of Foreign Key in request",
        "model": "Name of Model this Foreign Key related to"
    }
    ```
  - `"message": "foreign key(s) not found in foreign model(s)"` will be given.
- `success: "True"` if the entry specified is found and updated.
  - Status code will be `HTTP 200`.
  - `data` item will be `null`.
  - `"message": "entry updated"` will be given.

#### `DELETE` request

##### Request Usage

- URL Scheme: `{apisetname}/?{pk}=val`
- Body: None

##### Description

Delete an entry from the target table. The entry can only be specified with primary key.

Only parameter `{pk}`: Primary key name of the target table, with the value be the primary key value of the entry specified.

##### Response

- `success: "False"` if the entry specified by `pk` cannot be found.
  - Status code will be `HTTP 404`.
  - `data` item will be `null`.
  - `"message": "entry not found"`will be given.
- `success: "True"` if the entry specified is found and updated.
  - Status code will be `HTTP 200`.
  - `data` item will be `null`.
  - `"message": "entry deleted"` will be given.

## Class `FrontendReadOnlyAPIView`

**Extend from `AircraftManagerAPIView`**

### Description

Only `GET` is available under this `View`. Any other type of REST API request will be rejected with the following response, with status code `HTTP 405`:

```json
{
    "success": False,
    "message": "interface read-only",
    "data": None
}
```

## Class `AircraftTableView`

**Extend from `AircraftManagerAPIView`**

### Description

RESTful API for operations on `aircrafttable`.

### Specified parameters in Scheme

- `{apisetname} = aircraft`

### Special parameters

### Field names and types

| Field Name   | Type        | Can be NULL? <br />(Is an Optional Field for `POST` Requests?) | Key Type | Default Value |
|-------------|-------------|------|-----|---------|
| `aircraftId` | `int`       | YES (auto increment; will be ignored in `POST` requests) | **Primary**                                   | NULL    |
| `tailNumber` | `varchar(45)` | YES  |     | NULL    |
| `status`     | `varchar(45)` | YES  |     | NULL    |
| `location`   | `varchar(4)` | YES  |     | NULL    |
| `aircraftType` | `varchar(4)` `choice` | YES  |     | NULL    |
| `userId` (`userId_id` in actual tables) | `int`       | NO | **Foreign** (`userId` in table `userprofile`) | NULL    |

- `choice` of `aircraftType`: `A320`, `A321`, `A330`, `A350`, `B737`, `B757`, `B767`, `B787`, `B777`.

## Class `MovementTableView`

**Extend from `AircraftManagerAPIView`**

### Description

RESTful API for operations on `movementtable`.

### Specified parameters in Scheme

- `{apisetname} = movement`

### Mutant parameters in Scheme

#### `GET` method : Ranging filter for field name `arrivalDate` and `departureDate`

When  `*Date` and `*Date2` parameters appears as a pair in a `GET` request (here `arrivalDate` and `arrivalDate2`, or `departureDate` and `departureDate2`):

- The two parameters will be regarded as one filtering criterion, which filters out entries that have  `*Date` field values ranging **between** the values specified by these two parameters.
- If `*Date` and `*Date2` parameters do not appear as a pair in a request, or the request is not `GET`, the mutant will not be triggered.
  - If the request only has `*Date` parameter, it will be regarded as a normal filter.
  - If the request only has `*Date2` parameter, it will be ignored.
- **Note:** Value of `*Date2` **must be bigger** than `*Date`, otherwise there will be no entry matching the criteria.
- Example:
  - Request parameters: `departureDate=2022-10-22T10:34:06Z`, `departureDate2=2022-10-22T10:42:06Z`, `userId=1`
  - Response: Response will contain entries with `userId=1` and `departureDate` between `10/22/2022 10:34:06 AM` and `10/22/2022 10:42:06 AM`.

### Field names and types

| Field Name   | Type        | Can be NULL? <br />(Is an Optional Field for `POST` Requests?) | Key Type | Default Value |
| ------------ | ----------- | ---- | ---- | ------- |
| `movementId`     | `int`       | YES (auto increment; will be ignored in `POST` requests) | **Primary** | NULL    |
| `arrivalAirportId` | `int`       | YES  |     | NULL    |
| `arrivalDate`    | `datetime(6)` | NO   |     | NULL    |
| `departureDate`  | `datetime(6)` | NO   |     | NULL    |
| `aircraftId` (`aircraftId_id` in actual tables) | `int`       | NO   | **Foreign** (`aircraftId` in table `aircraftId`) | NULL    |
| `userId` (`userId_id` in actual tables) | `int`       | NO   | **Foreign** (`userId` in table `userprofile`)    | NULL    |
| `originAirportId` | `int`       | YES  |     | NULL    |

## Class `AirportTableView`

**Extend from `AircraftManagerAPIView`**

### Description

RESTful API for operations on `airporttable`.

### Specified parameters in Scheme

- `{apisetname} = airport`

### Field names and types

| Field Name   | Type        | Can be NULL? <br />(Is an Optional Field for `POST` Requests?) | Key Type | Default Value |
| ------------ | ----------- | ---- | ---- | ------- |
| `airportId` | `int`        | YES (auto increment; will be ignored in `POST` requests) | **Primary**                                   | NULL    |
| `airportCode` | `varchar(4)` | NO   |     | NULL    |
| `latitude` | `decimal(6,3)` | NO   |     | NULL    |
| `longitude` | `decimal(7,3)` | NO   |     | NULL    |
| `numAircraft` | `int`        | YES  |     | NULL    |
| `userId` (`userId_id` in actual tables) | `int`        | NO   | **Foreign** (`userId` in table `userprofile`) | NULL    |

