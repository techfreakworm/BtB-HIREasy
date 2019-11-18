from src.db.mongo_adapter import MongoAdapter
from config import Config
from datetime import datetime
from werkzeug.utils import secure_filename


class FileHandler(object):
    def __init__(self, user_email):
        self.user_email = user_email
        # Establish DB connection
        # Establish FTP connection
        

    def save_file(self, file_info, file):
        pass

    def __save_file_to_db(self, file_info):
        mongo_adapter = MongoAdapter(
                host=Config.MONGO_DB,
                db=Config.MONGO_DB,
                username=Config.MONGO_USER,
                password=Config.MONGO_PASS
            )
        # TODO: Replace these custom keys with an actual model in python class
        file_info['createdBy'] = self.user_email
        file_info['createdDate'] = datetime.utcnow()
        file_info['fileName'] = secure_filename(file.filename)
        collection = mongo_adapter.con_db(Config.MONGO_DATA_SCRAPE_COLLECTION)
        collection.insert_one(file_info)

    def __save_file_to_ftp(self, file):
        pass