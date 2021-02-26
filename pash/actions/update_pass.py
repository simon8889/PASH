from pash.actions.main import DbActions
from pash.cli_utils.crypto_utils import Crypto

class UpdatePass(DbActions):
    def __init__(self, _id, new_password):
        super().__init__()
        self.id = _id
        self.password = Crypto().encrypt_message(new_password)
    
    def update_it(self):
        if self.password == None:
            click.secho("An error occurred while trying to store the pass", fg = "red")
            return False
        try: 
            self.collection.update({"_id": self.id}, {"$set": {"password": self.password }})
            return True
        except:
            return False