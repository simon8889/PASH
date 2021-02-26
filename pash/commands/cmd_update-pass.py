import click
from pash.cli_utils.questions import password_list_question,one_password_question, password_questions
from pash.cli_utils.pass_generator import generator, get_generator_by_questions
from pash.cli_utils.config_mode_utils import get_password_formated
from pash.actions.get_pass import GetPass
from pash.actions.update_pass import UpdatePass 
import colorama
import pyperclip

colorama.init()

@click.command()
@click.option("-r", "--random-pass", "is_random", is_flag=True, help="the password is gererated random")
@click.option("-i", "--introduce-pas", "is_introduced", is_flag=True, help="the password is introduced") 
def cli(is_random, is_introduced):
    """update the password you choose"""
    search = GetPass().search()
    if search: 
        user_info =  password_list_question(search,"select the password you want to UPDATE")["password_selected"]
        if user_info:
            id_to_update = user_info["_id"]
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
            if UpdatePass(id_to_update,password).update_it():
                click.secho("Site", fg ="blue")
                click.secho(user_info["site"])
                click.secho("User", fg ="blue")
                click.secho(str(None) if not "user" in password else password["user"])
                click.secho("password", fg ="blue")
                click.secho(get_password_formated(password))
                pyperclip.copy(password)
                click.secho("The password was updated", fg ="green")
                return click.secho("The password is copy to the clipboard", fg = "green")
        else:
            click.secho("cancelled", fg ="yellow")

        
                