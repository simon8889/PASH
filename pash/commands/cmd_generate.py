from pash.cli_utils.pass_generator import generator, get_generator_by_questions
from pash.cli_utils.questions import password_questions
from pash.cli_utils.config_mode_utils import get_password_formated
from PyInquirer import prompt
import pyperclip
import click
import colorama

colorama.init()

@click.group()
def cli():
    """Generate a password whitout store it in the database"""
    pass

@cli.command()
def random_pass():
    """Generate a complete random password with 15 characters, symbols, caps, lows and nums"""
    gen = generator()
    click.secho(f"password:",fg= "blue")
    password =  gen.generate_pass()
    click.secho(get_password_formated(password))
    pyperclip.copy(password)
    return click.secho("The password is copy to the clipboard", fg = "green")

@cli.command()
def custom_pass():
    """Generate a password with the characteristics you specify"""
    answers = password_questions()
    if len(answers["types"]) == 0:
        return click.secho("you must select at least one characteristic for the password", fg = "yellow")
    else:
        password = get_generator_by_questions(answers).generate_pass()
        click.secho(f"password:",fg= "blue")
        click.secho(get_password_formated(password))
        pyperclip.copy(password)
        return click.secho("The password is copy to the clipboard", fg = "green")


