import os 
import json
import click
import colorama 

colorama.init()

def get_show_password_mode():
    try: 
        settings = os.path.abspath("pash/settings.json")
        with open(settings, "r") as f:
            try: 
                data = json.load(f)
                return data["show_password"]
            except Exception as e:
                print(e)
                return False
    except:
        return False

def change_show_password_mode():
    settings = os.path.abspath("pash/settings.json")
    new_mode = not get_show_password_mode()
    try:
        with open(settings, "r+") as f: 
            f.seek(0)
            data = json.load(f)
            data["show_password"] = new_mode
            f.seek(0)
            f.truncate()
            json.dump(data,f,indent=4)
            if new_mode:
                click.secho(f"{new_mode}: passwords will be displayed as text", fg ="green")
            else:
                click.secho(f"{new_mode}: passwords will not be displayed, asterisks will be displayed", fg ="green")
    except:
        click.secho("Error whit config file", fg = "red")

def get_password_formated(password):
    mode = get_show_password_mode()
    if not  mode: 
        return "*" * len(password) 
    else:
        return password