from connectors.connectPostgres import ConectaPostgreSQL
from models.address import Address
from models.user import User
from models.pet import Pet

class UserPostgresRepository():
    def __init__(self, conectaPostgreSQL: ConectaPostgreSQL):
        self.conectaPostgreSQL = conectaPostgreSQL
    
    def addUser(self, user: User, addres: Address):
        try:
            string = "Insert Into Table tb_user(id, name, street, number, city, state, country, birthdate) \
                Values(" + user.id + ", " + user.name + ", " + addres.street  + ", " + addres.number + ", " + addres.city + ", " + addres.state + ", " + addres.country + ", " + user.birthDate + ");"
            self.conectaPostgreSQL.execute_query(string)
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")
    

class PetPostgresRepository():
    def __init__(self, conectaPostgreSQL: ConectaPostgreSQL):
        self.conectaPostgreSQL = conectaPostgreSQL
    
    def addUser(self, pet: Pet):
        try:
            string = "Insert Into Table tb_pet(id, name, bride, birthdate, type, weight) \
                Values(" + user.id + ", " + user.name + ", " + addres.street  + ", " + addres.number + ", " + addres.city + ", " + addres.state + ", " + addres.country + ", " + user.birthDate + ");"
            self.conectaPostgreSQL.execute_query(string)
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")
    

class UserPetPostgresRepository():
    def __init__(self, conectaPostgreSQL: ConectaPostgreSQL):
        self.conectaPostgreSQL = conectaPostgreSQL
    
    def addUser(self, user: User, addres: Address):
        try:
            string = "Insert Into Table tb_user(id, name, street, number, city, state, country, birthdate) \
                Values(" + user.id + ", " + user.name + ", " + addres.street  + ", " + addres.number + ", " + addres.city + ", " + addres.state + ", " + addres.country + ", " + user.birthDate + ");"
            self.conectaPostgreSQL.execute_query(string)
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")