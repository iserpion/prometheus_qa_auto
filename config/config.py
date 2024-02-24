from dotenv import dotenv_values


class ConfigDatabase:

    @property
    def get_db_path(self):

        db_path = r"./become_qa_auto.db"
    
        return db_path
    
    @property
    def get_mongo_uri(self):

        config = dotenv_values(".env")
        mongo_uri = config["MONGODB_URI"]

        return mongo_uri
