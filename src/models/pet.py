import datetime
from bson import ObjectId

class Pet():
    def __init__(self, name, bride, birthDate, petType, weight, id=None):
        self._id = ObjectId(id) if id else ObjectId()
        self.name = name
        self.bride = bride
        self.birthDate = datetime.strptime(birthDate, '%d/%m/%Y')
        self.type = petType
        self.weight = weight
    
    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'bride': self.bride,
            'birthDate': self.birthDate,
            'type': self.type,
            'weight': self.weight
        }