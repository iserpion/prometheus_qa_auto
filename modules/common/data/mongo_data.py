

class MongoData:
    """Class hold data for MongoDB interaction tests"""

    db_name = "debtors_db"
    collection_name = "debtors"
    find_filter_ip = {"ip": "0.1.2.3"}
    filter_all = {}
    upd_money_50 = {"$set": {"money": 50}}
    upd_money_0 = {"$set": {"money": 0}}
    usd_rate = 38
    eur_rate = 41
    top_debtor_city_pipeline = [
      {
          "$group": {
              "_id": "$city", 
              "total_debtors": {
                  "$sum": 1
              }
          }
      }, 
      {
          "$sort": {
              "total_debtors": -1
          }
      }, 
      {
          "$limit": 1
      }
    ]

    total_debt_pipeline = [
        {
          "$addFields": {
            "converted_amount": {
              "$switch": {
                "branches": [
                  { 
                    "case": { "$eq": ["$currency", "UAH"] }, 
                    "then": "$money" 
                  },
                  { 
                    "case": { "$eq": ["$currency", "USD"] }, 
                    "then": { "$multiply": ["$money", 38] } 
                  },
                  { 
                    "case": { "$eq": ["$currency", "EUR"] }, 
                    "then": { "$multiply": ["$money", 41] } 
                  }
                ],
                "default": 0
              }
            }
          }
        },
        {
          "$group": {
            "_id": "",
            "total_amount": { "$sum": "$converted_amount" }
          }
        },
        {
          "$project": {
            "_id": 0,
            "total_amount": 1
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

