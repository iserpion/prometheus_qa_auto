import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.petstore import PetStore
from modules.api.helpers.schema_validator import SchemaValidator
from modules.common.database import Database


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

@pytest.fixture(scope='module')
def db():
    data_base = Database()

    yield data_base

    data_base.connection.close()


@pytest.fixture
def insert_delete_orders():
    db = Database()
    db.insert_into_orders()

    yield db
    
    db.delete_from_orders()
    db.connection.close()
    