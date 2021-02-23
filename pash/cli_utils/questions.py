import click
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

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
        {"name": "Upercase ABC"},
        {"name": "Numbers 123"},
        {"name": "Symbols $#-"}
    ]
    
    questions = [
        {
            "type": "input",
            "name": "lenght",
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
    return prompt(questions)

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
            click.echo("invalid answer")
            return self.execute()