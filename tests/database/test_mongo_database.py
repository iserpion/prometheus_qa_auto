import pytest
from modules.common.data.mongo_data import MongoData


data = MongoData()


@pytest.mark.nosql_db
def test_mongo_connection(mongo_db):
    """Test checks connection to MongoDB cluster"""

    connection_info = mongo_db.test_connection()

    assert connection_info["ismaster"] is True


# MongoDB CRUD operations testing

@pytest.mark.nosql_db
def test_insert_document_one(mongo_db):
    """Test checks inserting one document"""

    mongo_db.insert_document_one(data.collection_name_1, data.debtor_1)
    mongo_db.select_document_one(data.collection_name_1,data.filter_1)

    assert mongo_db.find_one_result["name"] == data.debtor_1["name"]


@pytest.mark.nosql_db
def test_db_name_collection_name_valid(mongo_db):
    """Test checks that created db and collection names are valid"""
    
    mongo_db.list_databases()
    mongo_db.list_collections()

    assert data.db_name in mongo_db.db_list
    assert data.collection_name_1 in mongo_db.collection_list


@pytest.mark.nosql_db
def test_update_document_one(mongo_db):
    """Test checks updating one document"""
    
    mongo_db.update_document_one(
        data.collection_name_1, 
        data.filter_1, 
        data.values_1
    )
    mongo_db.select_document_one(data.collection_name_1,data.filter_1)

    assert mongo_db.find_one_result["money"] == data.values_1["$set"]["money"]


@pytest.mark.nosql_db
def test_delete_document_one(mongo_db):
    """Test checks deleting one document"""

    mongo_db.delete_document_one(data.collection_name_1,data.filter_1)
    mongo_db.select_document_one(data.collection_name_1,data.filter_1)
 
    assert mongo_db.find_one_result is None


@pytest.mark.nosql_db
def test_insert_document_many(mongo_db):
    """Test checks inserting many documents"""

    mongo_db.insert_document_many(data.collection_name_1, data.debtors_list)
    mongo_db.count_documents(data.collection_name_1, data.count_all_filter)

    assert mongo_db.count_result == len(data.debtors_list)


# MongoDB aggregation pipeline testing

@pytest.mark.nosql_db
def test_find_total_debt_in_uah(mongo_db):
    """Test checks finding total debt in UAH"""

    mongo_db.aggregate_documents(
        data.collection_name_1, 
        data.total_sum_debts_pipeline
    )

    total_debt = mongo_db.calculate_total_debt_in_uah(
        mongo_db.aggregation_result,
        data.usd_rate,
        data.eur_rate
    )

    assert total_debt == data.expected_debt


@pytest.mark.nosql_db
def test_forgive_all_debts(mongo_db):
    """Test checks that all debts are zeroed"""

    mongo_db.update_document_many(
        data.collection_name_1, 
        data.count_all_filter, 
        data.values_2
    )

    mongo_db.aggregate_documents(
        data.collection_name_1, 
        data.total_sum_debts_pipeline
    )

    total_debt = mongo_db.calculate_total_debt_in_uah(
        mongo_db.aggregation_result,
        data.usd_rate,
        data.eur_rate
    )

    assert total_debt == 0
