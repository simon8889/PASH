from pash.cli_utils.pass_generator import generator
from pash.cli_utils.questions import password_questions
from PyInquirer import prompt
import click

@click.group()
def cli():
    """Generate a password whitout store it"""
    pass

@cli.command()
def random_pass():
    """Generate a complete random password with 15 characters, symbols, caps, lows and nums"""
    gen = generator()
    click.echo(gen.generate_pass())

@cli.command()
def custom_pass():
    answers = password_questions()
    types = list(map(lambda x: x.split(" ")[0],answers["types"]))
    length = int(answers["lenght"])
    if len(types) == 0:
        return click.echo("you must select at least one characteristic for the password")
    else:
        caps = False
        lows = False
        nums = False
        symb = False
        if "Lowercase" in types:
            lows = True
        if "Upercase" in types:
            caps = True
        if "Numbers" in types:
            nums = True
        if "Symbols" in types:
            symb = True
        if 100 < length or length <= 0:
            length = 15
        return click.echo(f"password: {generator(length=length, symbols=symb, nums=nums, caps=caps, lows=lows).generate_pass()}")


