from pash.actions.main import DbActions
from pash.cli_utils.crypto_utils import Crypto

def map_serch_list(x):
    new_dict =  x
    new_dict["password"] = Crypto().decrypt_message(x["password"])
    return new_dict
    

class GetPass(DbActions):
    def __init__(self, user = None, site = None):
        super().__init__()
        self.user = user
        self.site = site
    
    def get_search_dict(self):
        search_dict = {}
        if self.user:
            search_dict["user"] = self.user
        if self.site:
            search_dict["site"] = self.site
        return search_dict
    
    def search(self):
        try:
            return list(self.collection.find(self.get_search_dict()))
        except:
            click.secho("An error occurred while trying to find the pass", fg = "red")
            return False
    
    def search_whit_decrypt_pass(self):
        result = self.search()
        if result:
            return list(map(map_serch_list, result))
        else:
            return False

        


x = GetPass().search_whit_decrypt_pass()
print(x)

