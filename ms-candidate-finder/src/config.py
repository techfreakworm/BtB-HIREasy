import os


class Config(object):
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASS = os.getenv('MONGO_PASS')
    MONGO_DB = os.getenv('MONGO_DB')
    MONGO_DATA_SCRAPE_COLLECTION = 'candidates'