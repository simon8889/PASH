import click
from decouple import config as env
import pymongo

def question(text):
    ask = input(f"{text}(y/n)")
    if ask == "y":
        return True
    elif ask == "n":
        return False
    return question(text)

def get_mongo_client():
    url = env("URL_DB")
    if (test_connection(url)):
        return pymongo.MongoClient(url)
    else:
        return False

def valid_cofig():
    try:
        is_config=env("URL _DB")
        return True
    except:
        return False

def test_connection(url):
    try:
        client = pymongo.MongoClient(url)
        client.server_info()
        return True
    except:
        return False

def set_db_url(url):
    print("testing the connection to db ...")
    if test_connection(url):
        with open("./.env","a+") as env_file:
            env_file.writelines([f"URL_DB={url}"])
        print("DB URL SET")
    else:
        print("the url cant connect with the db")

    


@click.group()
def main():
    pass

@main.command()
@click.argument("url_db",default=False)
def config(url_db):
    if not valid_cofig():
        set_db_url(url_db)
    else:
        change_url=question("you want to change the db url? THE DATA WILL CHANGE")
        if change_url:
            set_db_url(url_db)
            print("changed the db url")

#TODo set the action
        

    

if __name__ == "__main__":
    main()