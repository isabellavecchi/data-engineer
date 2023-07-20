import pprint
import pandas as pd
from models.user import User
from models.pet import Pet
from repositories.mongoRepository import UserMongoRepository, PetMongoRepository

class UserMongoService():
    def __init__(self, userMongoRepository: UserMongoRepository):
        self.userMongoRepository = userMongoRepository
        self.users = []

    def addUsersFromDF(self, usersDF: pd.DataFrame):
        for row in usersDF.itertuples():
            user = User(name=row.name, birthDate=row.birthDate, addressStreet=row.street,
                            addressNumber=row.number, addressCity=row.city, addressState=row.state,
                            addressCountry=row.country, pets=row.pets)
            self.users.append(user.to_dict())
        self.userMongoRepository.addUsers(self.users)
    
    def findUsersFromCountry(self, country):
        print("\n\nUsuaries do Brasil")
        for user in self.userMongoRepository.findUsersFromCountry(country):
            print("user")
            pprint.pprint(user)
    
    def findUsersWithPets(self):
        print("\n\nUsuaries e seus pets")
        for user in self.userMongoRepository.findUsersWithPets():
            pprint.pprint(user)
        

class PetMongoService():
    def __init__(self, petMongoRepository: PetMongoRepository):
        self.petMongoRepository = petMongoRepository
        self.pets = []

    def addPetsFromDF(self, petsDF: pd.DataFrame):
        for row in petsDF.itertuples():
            pet = Pet(name=row.name, bride=row.bride, birthDate=row.birthDate,
                    petType=row.type, weight=row.weight)
            self.pets.append(pet.to_dict())
            # print("inserindo pet...")
            # self.petMongoRepository.addPet(pet.to_dict())
        return self.petMongoRepository.addPets(self.pets)
    
    def findPetOwners(self):
        print("\n\nPets e sies Dones")
        for pet in self.petMongoRepository.findPetOwners():
            pprint.pprint(pet)
    
    def findPetTypes(self, petType):
        print("\n\nPets do tipo " + petType)
        for pet in self.petMongoRepository.findPetTypes(petType):
            pprint.pprint(pet)
        
    
