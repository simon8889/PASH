import os 
import json
import click
import colorama 

colorama.init()

def backups_folder_exists():
    backups = os.path.abspath("pash/backups")
    if os.path.isdir(backups):
        return True
    else:
        click.secho("Backups folder not found", fg = "yellow")
        return False


