from pash.cli_utils.connection import connection

class NewStorePass:
    def __init__(to,password,user = None):
        self.to = to
        self.password = password 
        self.user = user
        self.connection = connection()
    