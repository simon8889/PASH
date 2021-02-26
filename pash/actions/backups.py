from pash.actions.main import DbActions
from pash.actions.get_pass import GetPass
from pash.actions.store_pass import NewStorePass
from pash.cli_utils.backup_utils import backups_folder_exists
from pash.cli_utils.crypto_utils import Crypto
import colorama
import click
import json
from progress.bar import Bar

colorama.init()

class Backups(DbActions):
    
    def __init__(self):
        super().__init__() 
    
    def get_backup(self):
        data = GetPass().search()
        if data and backups_folder_exists():
            data_list = []
            bar = Bar("procesing",max=len(data))
            for i in data:
                decrypted = Crypto().decrypt_message(i["password"])
                if decrypted == None:
                    bar.finish()
                    return False
                else:
                    object_to_append = {} 
                    object_to_append["password"] = decrypted
                    object_to_append["site"] = i["site"]
                    if "user" in i:
                        object_to_append["user"] = i["user"]
                    data_list.append(object_to_append)
                    bar.next()
                bar.finish()
            return data_list
        return False
    
    def set_backup(self, backup):
        backup = json.load(backup)["backup"]
        try:
            self.collection.delete_many({})
            bar = Bar("procesing",max=len(backup))
            for i in backup:
                site = i["site"]
                user = i["user"] if "user" in i else None
                password = i["password"]
                if NewStorePass(site, password, user=user).store_it():
                    bar.next()
                else:
                    click.secho(f"an error occurred while storing the password", fg ="red")
                    bar.finish()
                    return False
            bar.finish()
            return True
        except:
            click.secho(f"an error occurred while storing the password", fg ="red")
            return  False
                    

                    
                    
                    
                
        

            
            