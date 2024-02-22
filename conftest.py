import pytest
from modules.common.database import Database


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
    