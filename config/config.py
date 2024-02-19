class ConfigDatabase:

    @staticmethod
    def get_db_path(env):

        db_path = ''
        if env == 'local':
            db_path = r"C:\Users\iserp\qa_auto\prometheus_qa_auto" + r"\become_qa_auto.db"
        elif env == 'remote':
            db_path = r"./become_qa_auto.db"
    
        return db_path
    