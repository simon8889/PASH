import click
import json
import os
from pash.cli_utils.questions import question_yes_or_not as question
from pash.cli_utils.connection import connection, get_url
from pash.cli_utils.crypto_utils import generate_key, load_key
from json.decoder import JSONDecodeError
import colorama

colorama.init()

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
                ask = question("the database url is already set you want to change it? -- all your current data will be changed from database --")
                if (ask.execute()):
                    data["db_url"] = url
                    f.seek(0)
                    f.truncate()
                    json.dump(data,f,indent=4)
                    click.secho("db url changed", fg = "green")
        except JSONDecodeError:
            data = {
                "db_url": url
            }
            generate_key()
            json.dump(data,f,indent=4)
            click.secho("url db set", fg = "green")

@cli.command()
def connection_status():
    """Test the connection to database"""
    connection_status = connection().test_connection()
    if connection_status:
        click.secho("the database is connected",fg="green")

@cli.command()
def get_actual_url():
    """Shows the actual database url"""
    if get_url():
        click.secho("your actual database url:", fg = "blue")
        return click.secho(get_url())

@cli.command()
def get_crypto_key():
    """Shows your crypto key"""
    key = load_key()
    if key:
        click.secho("your actual crypto key:", fg = "blue")
        return click.echo(load_key())