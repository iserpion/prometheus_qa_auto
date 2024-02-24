import pytest
from modules.common.databases.sql_database import SqlDatabase
from modules.common.databases.mongo_database import MongoDatabase
from config.config import ConfigDatabase
from modules.common.data.mongo_data import MongoData


config = ConfigDatabase()


@pytest.fixture(scope='module')
def sql_db():
    data_base = SqlDatabase(config.get_db_path)

    yield data_base

    data_base.connection.close()


@pytest.fixture
def insert_delete_orders():
    db = SqlDatabase(config.get_db_path)
    db.insert_into_orders()

    yield db
    
    db.delete_from_orders()
    db.connection.close()

@pytest.fixture(scope='module')
def mongo_db():
    data = MongoData()

    try:
        connection_uri = config.get_mongo_uri
    except KeyError:
        pytest.skip("MongoDB environment variable MONGODB_URI is not set")
    
    db = MongoDatabase(connection_uri)
    db.create_database(data.db_name)
    db.create_collection(data.collection_name_1)

    yield db

    db.drop_database(data.db_name)
    db.connection.close()
    