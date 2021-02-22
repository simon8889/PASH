import click
import json
import os
from pash.cli_utils.question import question
from pash.cli_utils.connection import connection, get_url
from json.decoder import JSONDecodeError

@click.group()
def cli():
    """Config the user and database"""
    pass

@cli.command()
@click.argument("url", required=True)
def setdb(url):
    """ set the database url  """
    settings = os.path.abspath("./pash/settings.json")
    with open(settings, "a+") as f: 
        f.seek(0)
        try:
            data = json.load(f)
            if "db_url" in data:
                ask = question("the database url is already set you want to change it?")
                if (ask.execute()):
                    data["db_url"] = url
                    f.seek(0)
                    f.truncate()
                    json.dump(data,f,indent=4)
                    click.echo("db url changed")
        except JSONDecodeError:
            data = {
                "db_url": url
            }
            json.dump(data,f,indent=4)
            click.echo("url db set")

@cli.command()
def connectionstatus():
    """Test the connection to database"""
    connection_status = connection().test_connection()
    if connection_status:
        click.echo("the database is connected")

@cli.command()
def getactualurl():
    """Shows the actual database url"""
    click.echo(get_url())


        

        
    


