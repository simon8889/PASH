import click
import json
import os
from pash.cli_utils.questions import question_yes_or_not as question
from pash.cli_utils.connection import connection, get_url
from pash.cli_utils.crypto_utils import generate_key, load_key
from pash.cli_utils.config_mode_utils import  get_show_password_mode, change_show_password_mode
from pash.cli_utils.backup_utils import generate_backup_folder
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
    """ set the database url - initial setup  """
    settings = os.path.abspath("pash/settings.json")
    with open(settings, "a+") as f: 
        f.seek(0)
        try:
            data = json.load(f)
            if "db_url" in data:
                print(data)
                ask = question("the database url is already set you want to change it? -- all your passwords will be lost if you don't backup --")
                if ask.execute():
                    data["db_url"] = url
                    data["show_password"] = get_show_password_mode() 
                    f.seek(0)
                    f.truncate()
                    json.dump(data,f,indent=4)
                    click.secho("db url changed", fg = "green")
        except JSONDecodeError:
            data = {
                "db_url": url,
                "show_password": False
            }
            generate_key()
            generate_backup_folder()
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

@cli.command()
def get_pass_mode():
    """Show if the password output is visible"""
    mode = get_show_password_mode()
    if mode:
        click.secho("show password mode:", fg = "blue")
        click.secho(f"{mode}: passwords will be displayed as text")
    else:
        click.secho("show password mode:", fg = "blue")
        click.secho(f"{mode}: passwords will not be displayed, asterisks will be displayed")

@cli.command()
def change_pass_mode():
    """Change the visisbility of password out put"""
    click.secho("new show password mode:", fg = "blue")
    change_show_password_mode()
    

