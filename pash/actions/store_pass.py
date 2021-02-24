from pash.actions.main import DbActions 
from pash.cli_utils.crypto_utils import Crypto
import click
import colorama 

colorama.init()

class NewStorePass(DbActions):
    def __init__(self, to,password,user = None):
        super().__init__()
        self.to = to
        self.password = Crypto().encrypt_message(password) 
        self.user = user
    
    def is_user_needed(self):
        number_of_pass_whit_this_site = self.collection.count_documents({"site": self.to})
        if number_of_pass_whit_this_site > 0:
            return True
        return False
    
    def is_user_unique(self):
        number_of_user_for = self.collection.count_documents({"site": self.to, "user":  self.user})
        if number_of_user_for > 0:
            return False
        return True
    
    def get_pass_dict(self):
        pass_dict = {
                "site": self.to,
                "password": self.password
        }
        if self.user != None:
            pass_dict["user"] = self.user
        return pass_dict
    
    def store_it(self):
        try:
            if self.is_user_needed() and self.user == None:
                click.secho("you need to specify the user because there is already a pass for this site", fg = "yellow")
                return False
            elif self.user != None and not self.is_user_unique():
                click.secho("the user for the same site has to be unique", fg = "yellow")
                return False
            else:
                self.collection.insert_one(self.get_pass_dict())
                return True
        except:
            click.secho("An error occurred while trying to store the pass", fg = "red")
            return False

        
    