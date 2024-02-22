import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.petstore import PetStore
from modules.api.helpers.schema_validator import SchemaValidator
from modules.api.clients.spacex import SpaceX
from sgqlc.operation import Operation
from modules.common.schemas.spacex_query_schema import Query


@pytest.fixture(scope='module')
def github_api():
    api = GitHub()
    yield api

@pytest.fixture(scope='module')
def petstore_api():
    api = PetStore()
    yield api

@pytest.fixture(scope='module')
def pet_validate():
    validator = SchemaValidator()
    yield validator

@pytest.fixture
def spacex_api():
    api = SpaceX()
    yield api

@pytest.fixture()
def spacex_query():
    query = Operation(Query)
    yield query
