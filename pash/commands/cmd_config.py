import click
import json
import os
from pash.cli_utils.questions import question_yes_or_not as question
from pash.cli_utils.connection import connection, get_url
from pash.cli_utils.crypto_utils import generate_key, load_key
from json.decoder import JSONDecodeError

@click.group()
def cli():
    """Config the user and database"""
    pass

@cli.command()
@click.argument("url", required=True)
def set_db_url(url):
    """ set the database url  """
    settings = os.path.abspath("../settings.json")
    with open(settings, "a+") as f: 
        f.seek(0)
        try:
            data = json.load(f)
            if "db_url" in data:
                ask = question("the database url is already set you want to change it? -- all your current data will be lost --")
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
            generate_key()
            json.dump(data,f,indent=4)
            click.echo("url db set")

@cli.command()
def connection_status():
    """Test the connection to database"""
    connection_status = connection().test_connection()
    if connection_status:
        click.echo("the database is connected")

@cli.command()
def get_actual_url():
    """Shows the actual database url"""
    click.echo(get_url())

@cli.command()
def get_crypto_key():
    """Shows your crypto key"""
    click.echo(load_key())