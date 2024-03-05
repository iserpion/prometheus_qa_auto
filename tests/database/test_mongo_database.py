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

    mongo_db.insert_document_one(data.collection_name, data.debtor_1)
    mongo_db.select_document_one(data.collection_name,data.find_filter_ip)

    assert mongo_db.find_one_result["name"] == data.debtor_1["name"]


@pytest.mark.nosql_db
def test_check_db_name_and_collection_name(mongo_db):
    """Test checks that created db and collection names are valid"""
    
    mongo_db.list_databases()
    mongo_db.list_collections()

    assert data.db_name in mongo_db.db_list
    assert data.collection_name in mongo_db.collection_list


@pytest.mark.nosql_db
def test_update_document_one(mongo_db):
    """Test checks updating one document"""
    
    mongo_db.update_document_one(
        data.collection_name, 
        data.find_filter_ip, 
        data.upd_money_50
    )
    mongo_db.select_document_one(data.collection_name,data.find_filter_ip)

    assert (
        mongo_db.find_one_result["money"] == data.upd_money_50["$set"]["money"]
    )


@pytest.mark.nosql_db
def test_delete_document_one(mongo_db):
    """Test checks deleting one document"""

    mongo_db.delete_document_one(data.collection_name,data.find_filter_ip)
    mongo_db.select_document_one(data.collection_name,data.find_filter_ip)
 
    assert mongo_db.find_one_result is None


@pytest.mark.nosql_db
def test_insert_document_many(mongo_db):
    """Test checks inserting many documents to a collection"""

    mongo_db.insert_document_many(data.collection_name, data.debtors_list)
    mongo_db.count_documents(data.collection_name, data.filter_all)

    assert mongo_db.count_result == len(data.debtors_list)


# MongoDB aggregation pipeline testing
    
@pytest.mark.nosql_db
def test_find_top_debtor_city(mongo_db):
    """
    Test checks finding the top debtors city 
    using MongoDB aggregation pipeline 
    and python method to check the result
    """

    mongo_db.aggregate_documents(
        data.collection_name, 
        data.top_debtor_city_pipeline
    )
    
    top_debtor_city_py = mongo_db.calculate_top_debtor_city(data.debtors_list)

    assert mongo_db.aggregation_result.next()['_id'] == top_debtor_city_py


@pytest.mark.nosql_db
def test_find_total_debt_in_uah(mongo_db):
    """
    Test checks finding total debt in UAH from MongoDB
    using aggregation pipeline and compare it with python method result
    """

    mongo_db.aggregate_documents(
        data.collection_name, 
        data.total_debt_pipeline
    )

    total_debt_py = mongo_db.calculate_total_debt_in_uah(
        data.debtors_list,
        data.usd_rate,
        data.eur_rate
    )

    assert mongo_db.aggregation_result.next()['total_amount'] == total_debt_py


@pytest.mark.nosql_db
def test_forgive_all_debts(mongo_db):
    """
    Test checks that all debts are zeroed 
    using MonoDB update_many() method for zeroing
    and aggregation pipeline to check the result
    """

    mongo_db.update_document_many(
        data.collection_name, 
        data.filter_all, 
        data.upd_money_0
    )

    mongo_db.aggregate_documents(
        data.collection_name, 
        data.total_debt_pipeline
    )

    assert mongo_db.aggregation_result.next()['total_amount'] == 0
