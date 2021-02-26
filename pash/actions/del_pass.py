from pash.actions.main import DbActions

class DelPass(DbActions):
    def __init__(self, _id):
        super().__init__()
        self.id = _id
    
    def delele(self):
        try: 
            self.collection.delete_one({"_id": self.id})
            return True
        except:
            return False