import click
import colorama
from pash.actions.get_pass import GetPass 
from pash.actions.del_pass import DelPass
from pash.cli_utils.questions import password_list_question

colorama.init()

@click.command()
def cli():
    """delete a password from the database"""
    search = GetPass().search()
    if search: 
        user_info = password_list_question(search, "select the password you want to DELETE")["password_selected"]
        if user_info:
            id_to_delete = user_info["_id"]
            if DelPass(id_to_delete).delele():
                click.secho("Password deleted", fg ="green")
            else:
                click.secho("Cant delete pasword", fg ="red")
        
        else:
            click.secho("cancelled", fg ="yellow")