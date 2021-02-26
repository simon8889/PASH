import click
from pash.actions.get_pass import GetPass 
from pash.cli_utils.questions import password_list_question
from pash.cli_utils.config_mode_utils import get_password_formated
from pash.cli_utils.crypto_utils import Crypto
import pyperclip
import colorama

colorama.init()

@click.command()
@click.option("-u","--user","user",default = False)
@click.option("-s","--site","site",default = False)
def cli(user, site):
    """Search a password in the database"""
    user = None if user == False else user
    site = None if site == False else site
    search = GetPass(user = user, site = site).search()
    if search:
        try:
            password_info = password_list_question(search,"select the password you want to OBTAIN")["password_selected"]
            if password_info:
                password = Crypto().decrypt_message(password_info["password"])
                click.secho("Site:", fg = "blue")
                click.secho(password_info["site"])
                click.secho("User:", fg = "blue")
                click.secho(str(None) if not "user" in password_info else password_info["user"])
                click.secho("Password:", fg = "blue")
                click.secho(get_password_formated(password))
                pyperclip.copy(password)
                return click.secho("The password is copy to the clipboard", fg = "green")
            else:
                click.secho("cancelled", fg ="yellow")
        except:
            pass