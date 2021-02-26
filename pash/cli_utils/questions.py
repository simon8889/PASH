import click
import colorama
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
from pash.cli_utils.cli_styles import style

colorama.init()

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='password lenght should be a number',
                cursor_position=len(document.text))  

def password_questions():
    type_options = [
        {
            "name": "Lowercase abc",
            "checked": True
        },
        {
            "name": "Upercase ABC",
            "checked": True
        },
        {
            "name": "Numbers 123",
            "checked": True
        },
        {
            "name": "Symbols $#-",
            "checked": True
        }
    ]
    
    questions = [
        {
            "type": "input",
            "name": "length",
            "message": "length of your password",
            "default": "15",
            "validate": NumberValidator
        },
        {
            "type": "checkbox",
            "name": "types",
            "message": "choose the characteristics of your password",
            "choices": type_options,
        }
    ]
    return prompt(questions, style=style)


def user_site_questions():
    questions = [
        {
            "type": "input",
            "name": "site",
            "message": "enter the site or app for the password: ",
            "validate": lambda x: len(x) > 0
        },
        {
            "type": "input",
            "name": "user",
            "message": "introduce the user (optional if the site is unique in the database, it must be unique per site): ",
        }
    ]
    return prompt(questions,style=style)

def one_password_question():
    questions = [
        {
            "type": "password",
            "name": "password",
            "message": "enter your password: ",
            "validate": lambda x: len(x) > 0
        }
    ]
    return prompt(questions,style=style)

def password_list_question(password_list, message):
    choices = [{
        "name": "CANCEL",
        "value": False 
    }]
    for i in password_list:
        user = None if "user" not in i else i["user"]
        site = i["site"]
        option = {
            "name": f"Site: {site} - User: {user}",
            "value": i
        }
        choices.append(option)


    questions = [
        {
            "type": "list",
            "name": "password_selected",
            "message": message,
            "choices": choices
        }
    ]
    return prompt(questions, style=style)

def files_list_question(file_list,message):
    choices = [{
        "name": "CANCEL",
        "value": False 
    }]
    
    for i in file_list:
        option = {
            "name": i,
            "value": i
        }
        choices.append(option)
    
    questions = [
        {
            "type": "list",
            "name": "file_selected",
            "message": message,
            "choices": choices
        }
    ]
    return prompt(questions, style=style)
        


class question_yes_or_not:
    def __init__(self,text):
        self.text = f"{text}(y/n): "
    
    def execute(self):
        answer = input(self.text)
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            click.secho("invalid answer", fg = "red")
            return self.execute()