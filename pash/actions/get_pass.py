from pash.actions.main import DbActions
import click

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
            search = list(self.collection.find(self.get_search_dict()))
            if search == []:
                click.secho("no passwords found", fg = "yellow")
                return False 
            else:
                return search
        except:
            click.secho("An error occurred while trying to find the pass", fg = "red")
            return False
    
            