from sqlalchemy import Column, ForeignKey, Integer, String, Date, MetaData, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from models.address import Address
from models.user import User
from models.pet import Pet

Base = declarative_base()

"""--------"""
"""  User  """
"""--------"""

class TbUser(Base):   #TbUser é filho da classe Base
    __tablename__ = 'tb_user'
    id = Column(String(100), primary_key=True)
    name = Column(String(80)) #VARCHAR 
    street = Column(String(200))
    number = Column(String(10))
    city = Column(String(200))
    state = Column(String(200))
    country = Column(String(2))
    birthDate = Column(Date)

    def __init__(self, user: User, address: Address):
        self.name = user.getName()
        self.street = address.getStreet()
        self.number = address.getNumber()
        self.city = address.getCity()
        self.state = address.getState()
        self.country = address.getCountry()
        self.birthDate = user.getBirthDate()

    def serialize(self):
        """Return a dictionary"""
        return {
            '_id': self.id,
            'name': self.name,
            'address': {
                'street': self.street,
                'number': self.number,
                'city': self.city,
                'state': self.state,
                'country': self.country,
            },
            'birthDate': self.birthDate,
            'pets': self.pets,
        }
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getStreet(self):
        return self.street

    def getNumber(self):
        return self.number

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getCountry(self):
        return self.country

    def getBirthDate(self):
        return self.birthDate
    

    def setName(self, name):
        self.name = name

    def setStreet(self, name):
        self.name = name
            
    def setNumber(self, number):
        self.number = number
            
    def setCity(self, city):
        self.city = city
            
    def setState(self, state):
        self.state = state
            
    def setCountry(self, country):
        self.country = country
            
    def setBirthDate(self, birthDate):
        self.birthDate = birthDate


"""--------"""
"""   Pet  """
"""--------"""

class TbPet(Base):   #TbPet é filho da classe Base
    __tablename__ = 'tb_pet'
    id = Column(String(100), primary_key=True)
    name = Column(String(80)) #VARCHAR 
    bride = Column(String(200))
    birthDate = Column(Date)
    type = Column(String(10))
    weight = Column(Integer)

    def __init__(self, pet: Pet):
        self.name = pet.getName()
        self.bride = pet.getBride()
        self.birthDate = pet.getBirthDate()
        self.type = pet.getType()
        self.weight = pet.getWeight()

    def serialize(self):
        """Return a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'bride': self.bride,
            'birthDate': self.birthDate,
            'type': self.type,
            'weight': self.weight,
        }
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getBride(self):
        return self.bride

    def getBirthDate(self):
        return self.birthDate

    def getType(self):
        return self.type

    def getWeight(self):
        return self.weight
    

    def setName(self, name):
        self.name = name

    def setBride(self, bride):
        self.bride = bride
            
    def setBirthDate(self, birthDate):
        self.birthDate = birthDate
            
    def setType(self, petType):
        self.type = petType
            
    def setWeight(self, weight):
        self.weight = weight


"""-----------"""
"""  UserPet  """
"""-----------"""

class TbUserPet(Base):   #TbPet é filho da classe Base
    __tablename__ = 'tb_user_pet'
    userId = Column(String(100), ForeignKey('tb_user.id'))
    petId = Column(String(100), ForeignKey('tb_pet.id'))
    tb_user = relationship("TbUser")
    tb_pet = relationship("TbPet")

    __table_args__ = (
        PrimaryKeyConstraint('userId', 'petId'),
    )


    def __init__(self, userId, petId):
        self.userId = userId
        self.petId = petId

    def serialize(self):
        """Return a dictionary"""
        return {
            'userId': self.userId,
            'petId': self.petId,
        }
    
    def getIdUser(self):
        return self.userId
    
    def getIdPet(self):
        return self.petId
    

    def setIdUser(self, userId):
        self.userId = userId

    def setIdPet(self, userId):
        self.userId = userId