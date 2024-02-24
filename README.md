# My very first Test Automation Project

This project automates the following tests:
- REST API tests using Python, Pytest, Requests, and Pydantic
- GraphQL API tests using Python, Pytest, Requests, and sgqlc
- SQL database(SQLite) query tests using Python, Pytest, and sqlite3
- NoSQL database(MongoDB) query tests using Python, Pytest, and PyMongo
- Web UI tests using Python, Pytest, Selenium WebDriver, and Faker

## Getting Started
### Prerequisites
- Python >= 3.8
- Pytest >= 7.4
- Requests >= 2.27
- Selenium >= 4.6
- Pydantic >= 2.5
- Faker >= 22.5
- sgqlc >= 16.3
- python-dotenv >= 1.0
- pymongo >= 4.6

### Installation

```
git clone https://github.com/iserpion/prometheus_qa_auto.git
# clone repo

pip install -r requirements.txt
# Download and install needed libraries
```

### Running tests locally
```
pytest -s -v  # Run all tests
pytest -s -v -m rest_api  # Run REST API test suite
pytest -s -v -m gql_api # Run GraphQL API test suite
pytest -s -v -m sql_db # Run SQL database test suite
pytest -s -v -m nosql_db # Run NoSQL database test suite
pytest -s -v -m ui # Run all UI tests
pytest -s -v -m github_ui # Run github.com UI test suite
pytest -s -v -m allo_ui # Run allo.ua UI test suite
pytest -s -v -m nova_ui # Run novaposhta.ua UI test suite
pytest -s -v -m carid_ui # Run carid.com UI test suite

```

### Running tests in Docker
```
docker build -t automation-tests .
docker run automation-tests
```

## Test Framework Structure
### Directory Structure:
```
.
|-- config
|-- modules
|   |-- api
|   |   |-- clients
|   |   `-- helpers
|   |-- common
|   |   |-- data
|   |   |-- databases
|   |   |-- generators
|   |   `-- schemas
|   `-- ui
|       |-- page_locators
|       `-- page_objects
`-- tests
    |-- api
    |-- database
    `-- ui

```
### Organization:

- **config**:
  - Houses configuration files 

- **modules**:
  - Contains reusable components for test execution:
    - **api**:
        - **clients**: Holds specific API client classes interacting with different API endpoints.
        - **helpers**: Provides helper classes for API tests, e.g. schema validation.
    - **common**:
      - **data**: Stores shared test data across various test types.
      - **databases**: Stores database classes.
      - **generators**: Houses generic data generators for dynamic test setup.
      - **schemas**: Defines validation structures for API responses.
    - **ui**:
      - **page_locators**: Contains page locators classes
      - **page_objects**: Contains reusable page object classes representing UI elements and functionalities.
- **tests**:
  - Organizes test cases based on the functionalities they cover:
    - **api**: Holds API tests.
    - **database**: Contains tests interacting directly with the database.
    - **ui**: Houses UI tests.

### Key Points:

- The structure reflects common best practices for modularity and separation of concerns.
- Each directory has a clear purpose and contains related elements.
- Test organization aligns with testing types (API, database, UI) for focused execution.

### Additional Resources
- Python: https://www.python.org/
- Pytest: https://docs.pytest.org/en/8.0.x/
- Requests: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
- Selenium: https://www.selenium.dev/
- Pydantic: https://docs.pydantic.dev/latest/
- Faker: https://faker.readthedocs.io/en/master/
- sglc: https://sgqlc.readthedocs.io/en/latest/
- PyMongo: https://www.mongodb.com/docs/drivers/pymongo/

## Thanks
Many thanks to [Prometheus](https://prometheus.org.ua/) and [GlobalLogic](https://www.globallogic.com/ua/) for the very helpful [test automation course](https://prometheus.org.ua/prometheus-plus/automatic-software-testing/)
and especially to mentor Sergii Butenko who has a big talent for easily describing complex things.


