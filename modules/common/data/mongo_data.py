

class MongoData:
    """Class hold data for MongoDB interaction tests"""

    db_name = "debtors_db"
    collection_name_1 = "debtors"
    filter_1 = {"ip": "0.1.2.3"}
    values_1 = {"$set": {"money": 50}}
    values_2 = {"$set": {"money": 0}}
    count_all_filter = {}
    usd_rate = 38
    eur_rate = 41
    expected_debt = 101050
    total_sum_debts_pipeline = [
        {
            '$group': {
                '_id': '$currency', 
                'currency_sum': {
                    '$sum': '$money'
                }
            }
        }
    ]

    debtor_1 = {
        "name": "Petro",
        "age": 25,
        "money": 100,
        "currency": "USD",
        "city": "Lviv",
        "ip": "0.1.2.3"
    }

    debtor_2 = {
        "name": "Vasyl",
        "age": 31,
        "money": 200,
        "currency": "USD",
        "city": "Odesa",
        "ip": "1.2.3.4"
    }

    debtor_3 = {
        "name": "Elena",
        "age": 27,
        "money": 150,
        "currency": "EUR",
        "city": "Dnipro",
        "ip": "2.4.3.1"
    }

    debtor_4 = {
        "name": "Dmytro",
        "age": 30,
        "money": 2500,
        "currency": "UAH",
        "city": "Odesa",
        "ip": "1.3.2.4"
    }

    debtor_5 = {
        "name": "Igor",
        "age": 32,
        "money": 1500,
        "currency": "USD",
        "city": "Mykolaiv",
        "ip": "3.5.2.1"
    }

    debtor_6 = {
        "name": "Gleb",
        "age": 29,
        "money": 500,
        "currency": "EUR",
        "city": "Mykolaiv",
        "ip": "3.5.2.1"
    }

    debtor_7 = {
        "name": "Tonia",
        "age": 33,
        "money": 3500,
        "currency": "UAH",
        "city": "Mykolaiv",
        "ip": "3.5.2.1"
    }

    debtors_list = [
        debtor_1,
        debtor_2, 
        debtor_3, 
        debtor_4, 
        debtor_5,
        debtor_6, 
        debtor_7,
    ]

