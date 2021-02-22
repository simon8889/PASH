import json
from json.decoder import JSONDecodeError
import click
import os
import pymongo

def get_url():
    settings = os.path.abspath("./pash/settings.json")
    with open(settings, "r") as f:
        try:
            data = json.load(f)
            return data["db_url"]
        except JSONDecodeError:
            click.echo("please config the db run 'pash config setdb <db url>'")
            return False

class connection:
    def __init__(self):
        self.__client = pymongo.MongoClient(get_url())
    
    def test_connection(self):
        try:
            self.__client.server_info()
            return True
        except:
            return False
    
    def get_client(self):
        if self.test_connection():
            return self.__client
        else:
            return False
