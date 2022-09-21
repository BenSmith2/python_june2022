from mysqlconnection import connectToMySQL

class Users:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.id = data['last_name']
        self.id = data['created_at']
        self.id = data['updated_at']

    @classmethod
    def add_user(cls, ):
        