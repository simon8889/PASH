import click

class question:
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