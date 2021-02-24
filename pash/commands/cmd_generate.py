from pash.cli_utils.pass_generator import generator, get_generator_by_questions
from pash.cli_utils.questions import password_questions
from PyInquirer import prompt
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
    return click.secho(gen.generate_pass())

@cli.command()
def custom_pass():
    """Generate a password with the characteristics you specify"""
    answers = password_questions()
    if len(answers["types"]) == 0:
        return click.secho("you must select at least one characteristic for the password", fg = "yellow")
    else:
        click.secho(f"password:",fg= "blue")
        return click.secho(get_generator_by_questions(answers).generate_pass())


