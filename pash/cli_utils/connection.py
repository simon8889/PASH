import json
from json.decoder import JSONDecodeError
import click
import os
import pymongo

def get_url():
    try: 
        settings = os.path.abspath("../settings.json")
        with open(settings, "r") as f:
            try:
                data = json.load(f)
                return data["db_url"]
            except JSONDecodeError:
                click.echo("please config the db run 'pash config setdb <db url>'")
                return False
    except:
        click.echo("please config the db run 'pash config setdb <db url>'")

class connection:
    def __init__(self):
        try:
            self.__client = pymongo.MongoClient(get_url())
        except:
            self.__cient = None
    
    def test_connection(self):
        try:
            self.__client.server_info()
            return True
        except:
            click.echo("can´t connect with the database")
            return False
    
    def get_client(self):
        if self.test_connection():
            return self.__client
        else:
            return False
