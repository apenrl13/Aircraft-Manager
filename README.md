# Requirements and Specification Document

## TeamName

<!--The name of your team.-->

## *Python Airways*

***


### Project Abstract

<!--A one paragraph summary of what the software will do.-->

This document outlines the requirements and specifications for Python Airways. This is a comprehensive web application that is designed for the aviation industry to track and manage their aircract inventory across different airports. This inventory management system is designed to offer real-time visibility into the status as well as the location of an aircraft, ensuring that businesses have accurate records of all aircrafts at all times. 

### Customer

### Scrum Masters and Product Owners for All Sprints

| Sprint #    |    Scrum Masters    |    Product Owners |
| ------ | :-------: | ------: |
| 0/1 |    @figenblat    | @kgautam3 |
| 2    | @qxu229 |  @CCHENG93    |
| 3| @sbyun9 |@nbaumeister|

<!--A brief description of the customer for this software, both in general (the population who might eventually use such a system) and specifically for this document (the customer(s) who informed this document). Every project will have a customer from the CS506 instructional staff. Requirements should not be derived simply from discussion among team members. Ideally your customer should not only talk to you about requirements but also be excited later in the semester to use the system.-->

### User Requirements

<!--This section lists the behavior that the users see. This information needs to be presented in a logical, organized fashion. It is most helpful if this section is organized in outline form: a bullet list of major topics (e.g., one for each kind of user, or each major piece of system functionality) each with some number of subtopics.-->

The following user requirements reflect the unique aspects of Python Airways' operation. They focus on secure access, location-specific data interaction, mandatory reporting for operational consistency, view-only access for higher-level management, and the procedurues of scheduling aircraft movements. These requirements ensure the system supports efficient, secure, and user-friendly management of aircraft across Python Airways' network.

| ID   | Description                                                  | Priority | Status |
| ---- | ------------------------------------------------------------ | -------- | ------ |
| R11  | When the user first opens the web page, the frontend SHALL prompt the user to login. Upon logging in, the backend SHALL authenticate users by validating their existing company credentials against the company's user database. | Med      | Open   |
| R12 | Successful authentication should grant access to the application, ensuring secure user access. If authentication fails due to incorrect company credentials entered by the user, the frontend should display an error message and do not grant access to the application. | Med | Open |
| R13  | After clicking airports on the map, the front SHALL request data from backend and display the corresponding information. The backend SHALL access the database and return the results back to frontend. | High     | Currently working   |
| R14 | The system provides a functionality that allows users to select a specific date and time range. Upon selection, the frontend SHALL display a list of all scheduled aircraft arrivals and departures within the chosen timeframe. This list includes details such as flight number, aircraft type, estimated time of arrival or departure and deprature or arrival airports | High |Currently working |
| R15 | The system provides an interactive map interface allowing authorized user roles to create a new airport after selecting a location on the map with a mouse click. Upon mouse click, the system SHALL prompt the user to enter required information for adding a new airport, including airport name, airport code, and geographical coordinates. The backend SHALL validate the entered information for completeness and uniqueness against the existing airport database. If validation succeeds, the system SHALL add the new airport to the database and visually indicate the addition on the interactive map. If validation fails, the system SHALL display an error message detailing the reason for failure.| High | Currently working|
| R16  | The system provides an interface to schedule future aircraft arrivals and departures. This interface SHALL allow airport managers to specify the date, time, airline, flight number, and aircraft type for each arrival or departure. Upon submission of a new schedule, the backend SHALL validate the entry for conflicts with existing schedules. If the new schedule passes validation, the system SHALL record it in the movements database. If the validation fails, the system SHALL display an informative error message. | High     |  Currently Working   |

<!-- <div align="center"><small><i>Excerpt from Crookshanks Table 2-2 showing example user requirements for a timekeeping system</i></small></div> -->


### User Stories & Acceptance Criteria

#### Corporate Manager User Stories for Python Airways:

- As a corporate manager, I want to create a new airport.
    - When corporate manager clicks on create button, the application will prompt user to input the following details: Airport Code, Latitude, Longtitude, and Number of Aircraft.
    - Each input fileds above must have validation rules and any errors should be displayed clearly to the user.
    - If all inputs are verified, the new airport will be created and showed on the map.
- As a corporate manager, I want to see an aggregate of the airplane movements that has come in to and gone out from all airports over an arbitrary time span.
    - Corporate manager must be able to select any arbitrary time span.
    - Corporate mangers can filter the aggregated data by specific arrival or departure airports and airplane type if desired.
- As a corporate manager, I want to see my airports represented on a map.
    - The map should accuratly display all airports based on the longtitude and latitude.
    - Corporate managers should be able to zoom in and out and navigate (pan) the map to view different areas in detail.
- As a corporate manager, I want to mark that an airport has ceased operation as of some date. I don't want that facility included in aggregates after that date.
    - After clicking on an airport on the map, corporate managers can marked it as a ceased airport with a date.
    - The movement of ceased airports should but be aggregated when getting the aggregated airplane movements if the ceased date is after the slected time span.
- As a corporate manager, I want to see a count of how many airports I have.
    - The count of airports should be prominently displayed on the corporate manager's dashboard.
    - The count must be updated in real-time to reflect any additions, removals, or changes in the status of airports.
- [SCRAPPED]As a corporate manager, I want to create an account if I do not have one, or log in if I do.
    -Allow different privilages for corporate manager
    -Use cookies to maintain login status

#### Facility (Airport) Manager User Stories for Python Airways:

- As a facility manager, I want to view what airplanes and how many I have in my airports.
    - After clicking on an airport on the map, the system should provide a detailed list showing the quantity of each airplane model.
    - The information displayed should be updated in real-time to reflect recent arrivals or departures.
- As a facility manager, I want to see a list of movement that had the same airplane ID.
    - Facility managers can view the list of movement by choosing the specific airplane type and filter it with arrival or departure airports if desired.
- As a facility manager, I want to record a future airplane movement (a shipment whose date and/or time is in the future).
    - When recording future movement, the system should ask the facility manager to provide following details: Arrival and Departure Airport ID, Arrival and Departure Date and Aircraft ID.
    - The system must validate the scheduled date and time to ensure they are in the future.
    - The system must make sure that the departure airport has enough airplanes and display an error message if the airport does not.
- As a facility manager, I want to record an airplane movement that has arrived at or left the airport and I want this to automatically update my airport.
    - When recording past movement, the system should ask the facility manager to provide following details: Arrival and Departure Airport ID, Arrival and Departure Date and Aircraft ID.
    - The system must validate the scheduled date and time to ensure they are in the past.
    - After recording the movement, the number of aircraft at the airports should reflect the change.
- As a facility manager, I want to view what I used to have in my airports at some time in the past, and what I will have in my airport at some point in the future.
    - Facility manager can select a specific date after clicking on the airport and see the number of airport based on corresponding date.
- [SCRAPPED]As a facility manager, I want to create an account if I do not have one, or log in if I do.
    -Allow different privilages for facility manager
    -Use cookies to maintain login status

### Testing Plan for User Stories

#### As a corporate manager, I want to create a new airport.

|Tests| Status |
|---- | -------- |
|Database Unit Test| N/A |
|Backend Unit Test - Airport Table Post| Test Passed |
|Frontend Unit Test - Send post request with json data | Test Passed |
|Integration Test | Test Passed |
|Manual Testing - Get all entries stored in database| Test Passed |

- As a corporate manager, I want to see my airports represented on a map.

|Tests| Status |
|---- | -------- |
|Database Unit Test| N/A |
|Backend Unit Test - Airport Table Get| Test Passed |
|Frontend Unit Test - Send get request | Test Passed |
|Integration Test | Test Passed |
|Manual Testing - Send data to backend and create new entry in database | Test Passed |
- As a corporate manager, I want to see an aggregate of the airplane movements that has come in to and gone out from all airports over an arbitrary time span.

|Tests| Status |
|---- | -------- |
|Database Unit Test| N/A |
|Backend Unit Test - Movement Table Get| Test Passed |
|Frontend Unit Test - Send get request | Test Passed |
|Integration Test | Test Passed |
|Manual Testing - Get all entries over the time span from database| N/A |
- As a facility manager, I want to view what airplanes and how many I have in my airports.

|Tests| Status |
|---- | -------- |
|Database Unit Test| N/A |
|Backend Unit Test - Aircraft Table Get| Test Passed |
|Frontend Unit Test - Send get request | Test Passed |
|Integration Test | Test Passed |
|Manual Testing - Get all entries in any airport from database| N/A |

### User Interface Requirements

<!--Describes any customer user interface requirements including graphical user interface requirements as well as data exchange format requirements. This also should include necessary reporting and other forms of human readable input and output. This should focus on how the feature or product and user interact to create the desired workflow. Describing your intended interface as “easy” or “intuitive” will get you nowhere unless it is accompanied by details.-->

<!--NOTE: Please include illustrations or screenshots of what your user interface would look like -- even if they’re rough -- and interleave it with your description.-->

Images can be included with `![alt_text](image_path)`

The following UI requirements are designed to ensure that the inventory management system is not only functional but also user-friendly, accommodating the specific needs of corporate and airport managers within Python Airways. By focusing on responsiveness, ease of use, accessibility, and security, the system can provide a seamless experience for all users.

| Requirement ID | Description                                                                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UI01           | The interface should be responsive, adapting seamlessly to desktop, tablet, and mobile devices to ensure accessibility across different platforms.          |
| UI02           | Implement a dashboard view for corporate managers featuring summary statistics, aggregate inventory movements, and map visualizations of airports.          |
| UI03           | Airport managers should have a clear, intuitive interface for viewing current and historical aircraft inventory, as well as scheduling and recording shipments. |
| UI04           | Use a consistent, aviation-themed color scheme and typography throughout the application to reinforce branding and improve visual cohesion.                |
| UI05           | Navigation menus should be clearly labeled and logically organized to facilitate easy access to different sections of the application.                     |
| UI06           | Forms for entering or updating aircraft information and scheduling shipments should include validation feedback to prevent user errors.                     |
| UI07           | Implement modals for confirming actions (e.g., adding a new airport, marking an airport as ceased operation) to prevent accidental data changes.            |
| UI08           | Provide a search function with filtering capabilities to quickly locate specific aircraft, airports, or shipments within the system.                       |
| UI09           | Include interactive tooltips and help icons throughout the application to offer users guidance and explanations for various features and data fields.      |
| UI10           | Implement a secure login page with clear input fields for username and password, including the option for password visibility toggle and forgot password link. |
| UI11           | The UI should provide real-time feedback to users after actions are taken, such as successful data submission or error messages.                          |
| UI12           | Integrate a comprehensive reporting section where users can generate, view, and export reports based on various criteria (time periods, airports, etc.).    |



### Security Requirements

<!--Discuss what security requirements are necessary and why. Are there privacy or confidentiality issues? Is your system vulnerable to denial-of-service attacks?-->

### System Requirements

<!--List here all of the external entities, other than users, on which your system will depend. For example, if your system inter-operates with sendmail, or if you will depend on Apache for the web server, or if you must target both Unix and Windows, list those requirements here. List also memory requirements, performance/speed requirements, data capacity requirements, if applicable.-->

| Requirement Category | Requirement Description                                                                                                                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Database: MySQL**  | - Support for complex queries for aircraft and user information. <br> - Optimized schema for efficient data storage and retrieval.                                                                                                        |
| **Back End: Django (Python)** | - Utilize Django’s ORM for database interactions. <br> - Implement RESTful APIs for frontend-backend communication. <br> - Adhere to security practices for authentication and data protection.                                          |
| **Front End: React** | - Develop a responsive UI with React for enhanced user experience. <br> - Implement dynamic updates using React's state management.                                                                                                       |
| **External Dependencies** | - Compatibility with WSGI (Web Server Gateway Interface is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request. WSGI is a Python standard.) servers like Gunicorn or uWSGI. <br> - Deployable on cloud platforms (AWS, GCP, Azure) supporting the tech stack.                                                                                                |
| **System Architecture** | - Seamless communication through REST APIs and Django ORM.                                                                                      |

### Specification

<!--A detailed specification of the system. UML, or other diagrams, such as finite automata, or other appropriate specification formalisms, are encouraged over natural language.-->

<!--Include sections, for example, illustrating the database architecture (with, for example, an ERD).-->

<!--Included below are some sample diagrams, including some example tech stack diagrams.-->

You can make headings at different levels by writing `# Heading` with the number of `#` corresponding to the heading level (e.g. `## h2`).

#### Initial Roles
| DjangoBackend    |    ReactFrontend    |    Database |
| ------ | :-------: | ------: |
| @CCHENG93 |    @sbyun9    | @nbaumeister |
| @qxu229    | @figenblat |         |
|@kgautam3||

#### Technology Stack

The Technology Stack of a web app contains three parts: **Front end**, **Back end** and **Database** (in order from user to server.)

- **Database:** in our project, database will be used to store information of aircrafts and users (including username and hashed password,) Since MySQL is a requirement for this class, we will use **MySQL.**

- **Back end:** multiple back-end frameworks are available for modern web apps. We will use **Django** in **Python** for our back-end implementation.

- **Front end:** modern front-end frameworks includes React and Vue.js. We will use **React** library for our front-end implementation.

#### System Architecture Diagram

```mermaid
flowchart RL
subgraph Front End
	A(Javascript: React)
end
	
subgraph Back End
	B(Python: Django)
end
	
subgraph Database
	C[(MySQL)]
end

A <-->|"REST API"| B
B <-->|Django ORM| C
```


#### Database

```mermaid
---
title: Database for Aircraft Manager
---
erDiagram
    userprofile ||--o{ aircrafttable : "created by"
    userprofile ||--o{ airporttable : "created by"
    userprofile ||--o{ movementtable : "created by"
    airporttable ||--o{ movementtable : "included in"
    aircrafttable ||--o{ movementtable : "included in"
    airporttable ||--o{ aircrafttable : "included in"

    userprofile {
        int userId PK
        string username
        string password
        enum role
    }

    aircrafttable {
        int aircraftId PK
        int tailNumber
        enum aircraftType
        string status
        string location
    }

    airporttable {
        int airportId PK
        string airportCode
        decimal latitude
        decimal longitude
        int numAircraft
        int userId FK
    }

    movementtable {
        int movementId PK
        int arrivalAirportId FK
        int originAirportId FK
        DateTimeField arrivalDate
        DateTimeField departureDate
        int aircraftId FK
        int userId FK
    }
```

#### Sequence Diagram

The sequence diagram is inherited from the system tech stack. For front-end and back-end, we follow the normal sequence of REST. For back-end and database, as we mentioned, Django ORM (a standard module of Django perform general SQL querying commands) is utilized to communicate with the database.

```mermaid
sequenceDiagram

participant ReactFrontend
participant DjangoBackend
participant MySQLDatabase

ReactFrontend ->> DjangoBackend: HTTP Request (no HTTPS)
activate DjangoBackend

DjangoBackend ->> MySQLDatabase: Query
activate MySQLDatabase

MySQLDatabase -->> DjangoBackend: Result
deactivate MySQLDatabase

DjangoBackend -->> ReactFrontend: JSON Object
deactivate DjangoBackend
```

### Standards & Conventions

<!--Here you can document your coding standards and conventions. This includes decisions about naming, style guides, etc.-->

#### 1. Introduction

This document outlines the coding standards and best practices for T27. Its goal is to ensure that our codebase is consistent, readable, and maintainable by all team members and future contributors. Adherence to these guidelines is crucial for effective collaboration and the long-term success of the project.

#### 2. Coding Style Guidelines

##### Indentation

- Use `tabs`, not white spaces, with a standard indent size of 4 spaces.

- Each nested block should be properly indented and spaced.

##### Line Length

- Aim for a maximum line length of 80 characters where possible for better readability across various environments.

##### Whitespace

- Use blank lines sparingly to separate logical blocks of code.

##### Braces

- Use the `one true brace style` variant of the K&R style for braces except for python. Consider the example below from [indentation style wikipedia](https://en.wikipedia.org/wiki/Indentation_style).
```
while (x == y) {
    foo();
    bar();
}
```

#### 3. Naming Conventions

##### Variables

- Use `camelCase` or `lower camel case` for variable names and be descriptive.

##### Functions/Methods

- Use `camelCase` or `lower camel case` for functions/methods and start with a verb to indicate action.

##### Classes/Interfaces

- Use `PascalCase` or `upper camel case` for classes and interfaces.

##### Constants

- Use `UPPER_SNAKE_CASE` for constants.

##### Global Variables

- Avoid using global variables in all contexts.

#### 4. File Organization

##### Directory Structure

- Organize the project into logical directories, with separate folders for source code, tests, documentation, and assets.

##### File Naming

- Name files consistently, using a convention that reflects the file's purpose or the type of content it holds.

##### Module Organization

- Group related functions, classes, and variables together within modules or files.

#### 5. Commenting and Documentation

##### Inline Comments

- Use inline comments sparingly to explain "why" rather than "what" the code does.

##### Block Comments

- Use block comments for more detailed explanations or to mark off sections of code.

##### Documentation Comments

- Use documentation comments to automatically generate API documentation.
- See [javadoc wikipedia](https://en.wikipedia.org/wiki/Javadoc) for more information.

##### READMEs and Other Docs

- Maintain a comprehensive README file at the root of the project, along with any other necessary documentation (installation guides, usage examples, etc.).

#### 6. Version Control Practices

##### Branching Model

- Follow a standardized branching model (e.g., Git Flow or GitHub Flow) for development, features, releases, and hotfixes.

##### Commit Messages

- Write clear, concise commit messages that explain the changes made and the reason for them.

##### Pull Requests and Code Reviews

- Use pull requests for merging code into the main branch and conduct code reviews to maintain quality.

#### 7. Performance Considerations

##### Efficient Algorithms

- Choose or implement algorithms that are efficient in terms of time and space complexity.

##### Memory Management

- Be mindful of memory allocation and deallocation, especially in languages where manual memory management is necessary.

#### 8. Tooling and Environment

##### IDEs/Editors

- Recommend specific IDEs/editors that are well-suited for the project, along with plugins or extensions that enforce the coding standards.

##### Build Tools

- Specify the build tools and scripts used in the project to ensure consistency in builds.

##### Dependency Management

- Use a dependency management tool to manage libraries and frameworks the project depends on, ensuring that everyone uses the same version.

#### 9. Unit Testing

##### Test Structure and Naming Conventions

- **Test Files:** Test files should reside in a dedicated `tests directory` that mirrors the structure of the project's source code. Each test file name should start with `test_` followed by the name of the module it's testing.

- **Test Functions:** Test functions should be named using the pattern `test_<functionality_being_tested>`. This naming convention ensures clarity and ease of understanding regarding what each test does and what it aims to verify.

##### Test Isolation
- Each unit test should focus on a single aspect of functionality and should run independently of other tests.

##### Assertive and Clear Test Cases
- Tests should assert conditions directly and clearly, with assertions made about the expected outcome of the test.
- Aim for simplicity and clarity in test logic to make tests easy to understand and maintain.

##### Documentation and Comments

- Include a brief comment at the beginning of each test function describing what the test aims to verify. Especially, when testing special cases or edge cases.

##### Frontend

- Use `React.js` as the unit testing framework for javascript.

##### Backend

- Use `Django's unit test (Django.test)` which utilizes python standard library `unittest` as the unit testing framework for python.
- More information could be found [here](https://docs.djangoproject.com/en/5.0/topics/testing/overview/).

#### 10. CI/CD

- Use GitLab's CI/CD pipeline for testing new commits to Gitlab
- Use python black library to lint code
- Use docker environments to test code
