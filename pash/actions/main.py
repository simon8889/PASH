from pash.cli_utils.connection import connection

class DbActions:
    def __init__(self):
        self.connection = connection()
        self.set_client()
    
    def set_client(self):
        client =  self.connection.get_client()
        if client:
            self.collection =  client["passdb"]["pass"]
