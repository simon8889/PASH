import os 
import click
from pash.actions.backups import Backups
from pash.cli_utils.backup_utils import backups_folder_exists
import json
from json.decoder import JSONDecodeError
import time
import colorama
from pash.cli_utils.questions import files_list_question

colorama.init()

@click.group()
def cli():
    """Perform or access backups"""
    pass

@cli.command()
def see_backup():
    """Get all available backups and see the content"""
    if backups_folder_exists():
        mypath = os.path.abspath("pash/backups")
        file_list = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and ".json" in f ]
        if len(file_list) > 0:
            file_selected = files_list_question(file_list, "select the backup you want to SEE")["file_selected"]
            if file_selected:
                with open(f"{mypath}/{file_selected}", "r+") as f:
                    click.secho("Backup content:", fg = "blue")
                    click.secho(f.read())
            else:
                click.secho("Canceled", fg="yellow")
        else:
            click.secho("No backups found", fg ="yellow")

    

@cli.command()
def do_backup():
    """Save a backup"""
    if backups_folder_exists():
        timestr = time.strftime("%Y%m%d-%H%M%S")
        file_name = f"{timestr}.json"
        backup_file = os.path.abspath(f"pash/backups/{file_name}")
        backup = Backups().get_backup()
        if backup:
            with open(backup_file, "a+") as f:
                f.seek(0)
                data = {"backup": backup}
                json.dump(data, f, indent=4)
                click.secho("Backup file name:",fg ="blue")
                click.secho(file_name)
                click.secho("Backup made", fg = "green")


@cli.command()
def delete_backup():
    """Delete a backup file"""
    if backups_folder_exists():
        mypath = os.path.abspath("pash/backups")
        file_list = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and ".json" in f ]
        if len(file_list) > 0:
            file_selected = files_list_question(file_list, "select the backup you want to DELETE")["file_selected"]
            if file_selected:
                try:
                    os.remove(f"{mypath}/{file_selected}")
                    click.secho("Backup deleted", fg = "green")
                except:
                    click.secho("error deleting file", fg="red")
            else:
                click.secho("Canceled", fg="yellow")
        else:
            click.secho("No backups found", fg ="yellow")

@cli.command()
def set_backup():
    """Choose a backup to use"""
    if backups_folder_exists():
        mypath = os.path.abspath("pash/backups")
        file_list = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and ".json" in f ]
        if len(file_list) > 0:
            file_selected = files_list_question(file_list, "select the backup you want to SET IN THE DATABASE")["file_selected"]
            with open(f"{mypath}/{file_selected}", "r+") as f:
                if Backups().set_backup(f):
                    click.secho("Backup seted in the database", fg = "green")
        else:
            click.secho("No backups found", fg ="yellow")
                
