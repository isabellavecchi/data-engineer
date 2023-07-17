import pandas as pd
from models.user import User
from repositories.mongoRepository import UserMongoRepository

class UserMongoService():
    def __init__(self, userMongoRepository: UserMongoRepository):
        self.userMongoRepository = userMongoRepository
        self.users = []

    def addUsersFromDF(self, usersDF: pd.DataFrame):
        for row in usersDF.itertuples():
            user = User(name=row.name, birthDate=row.birthDate, addressStreet=row.street,
                            addressNumber=row.number, addressCity=row.city, addressState=row.state,
                            addressCountry=row.country)
            # self.users.append(user.to_dict())
            self.userMongoRepository.addUsers
        # self.userMongoRepository.addUsers(self.users)
        
    
