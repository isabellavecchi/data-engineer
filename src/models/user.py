import datetime
from bson import ObjectId

from models.address import Address

class User():
    def __init__(self, name, birthDate, addressStreet, addressNumber, addressCity, addressState, addressCountry, pets=None, id=None):
        self._id = ObjectId(id) if id else ObjectId()
        self.name = name
        self.address = Address(addressStreet, addressNumber, addressCity, addressState, addressCountry)
        # self.birthDate = datetime.strptime(birthDate, '%d/%m/%Y')
        self.birthDate = birthDate
        self.pets = pets if pets else []
    
    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'address': self.address.to_dict(),
            'birthDate': self.birthDate,
            'pets': self.pets,
        }
    
    def addPet(self, petId):
        self.pets.append(petId)
    
    def remPet(self, petId):
        self.pets.remove(petId)
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.addPet
    
    def getBirthDate(self):
        return self.birthDate
    
    def getPets(self):
        return self.pets
    
    
    def setName(self, name):
        self.name = name
    
    def setAddress(self, addPet):
        self.addPet = addPet
    
    def setBirthDate(self, birthDate):
        self.birthDate = birthDate
    
    def setPets(self, pets):
        self.pets = pets
    
    