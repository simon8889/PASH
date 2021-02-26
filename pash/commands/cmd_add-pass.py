import click
from pash.cli_utils.questions import password_questions, user_site_questions, one_password_question
from pash.cli_utils.pass_generator import get_generator_by_questions, generator
from pash.cli_utils.config_mode_utils import get_password_formated
from pash.actions.store_pass import NewStorePass
import colorama 
import pyperclip

colorama.init()

@click.command() 
@click.option("-r", "--random-pass", "is_random", is_flag=True, help="the password is gererated random")
@click.option("-i", "--introduce-pas", "is_introduced", is_flag=True, help="the password is introduced") 
def cli(is_random, is_introduced):
    """add a new password to database"""
    if is_introduced and is_random:
        return click.secho("You can only choose one password generation option", fg="yellow")
    user_info = user_site_questions()
    if is_random:
        password = generator().generate_pass()
    elif is_introduced:
        password = one_password_question()["password"]
    else:
        password_info = password_questions()
        if len(password_info["types"]) < 0:
            return click.secho("you must select at least one characteristic for the password", fg = "yellow")
        else:
            password = get_generator_by_questions(password_info).generate_pass()
    if user_info["user"]:
        user = user_info["user"]
    else:
        user = None
    click.secho(f"User:",fg= "blue")
    click.secho(str(user))
    click.secho(f"site:",fg= "blue")
    click.secho(user_info["site"])
    click.secho(f"password:",fg= "blue")
    click.secho(get_password_formated(password))
    pyperclip.copy(password)
    click.secho("The password is copy to the clipboard", fg = "green")
    if NewStorePass(user_info["site"], password, user).store_it():
        click.secho("Pass Created", fg ="green")
    

        