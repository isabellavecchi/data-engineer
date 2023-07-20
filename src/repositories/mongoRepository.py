from connectors.connectMongo import ConectaMongoDB

class UserMongoRepository():
    def __init__(self, conectaMongoDB: ConectaMongoDB):
        self.conectaMongoDB = conectaMongoDB
    
    def addUsers(self, dictUsers):
        try:
            result = self.conectaMongoDB.insert_documents('users', dictUsers)
            if not result.inserted_ids:
                print("No documents inserted.")
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")
    
    def addUser(self, dictUser):
        try:
            result = self.conectaMongoDB.insert_document('users', dictUser)
            # if not result.inserted_ids:
            #     print("No documents inserted.")
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")
    
    def findUsersFromCountry(self, country):
        query = {'address.country': country}
        projection = {'pets': 0}
        return self.conectaMongoDB.execute_query('users', query, projection)

    def findUsersWithPets(self):
        pipeline = [
            {
                '$lookup': {
                    'from': 'pets',
                    'localField': 'pets',
                    'foreignField': '_id',
                    'as': 'pets'
                }
            },
            {
                '$project': {
                    '_id': 0,
                    'address.street': 0,
                    'address.number': 0,
                    'address.state': 0,
                    'address.country': 0,
                    'birthDate': 0
                }
            }
        ]
        return self.conectaMongoDB.execute_aggregation('users', pipeline)

class PetMongoRepository():
    def __init__(self, conectaMongoDB: ConectaMongoDB):
        self.conectaMongoDB = conectaMongoDB
    
    def addPets(self, dictPets):
        try:
            result = self.conectaMongoDB.insert_documents('pets', dictPets)
            if result.inserted_ids:
                return result.inserted_ids
            else:
                print("Nenhum Pet foi adicionado")
        except Exception as e:
            print(f"An error occurred while inserting pets: {str(e)}")
    
    def addPet(self, dictPet):
        try:
            result = self.conectaMongoDB.insert_document('pets', dictPet)
            # if not result.inserted_ids:
            #     print("No documents inserted.")
        except Exception as e:
            print(f"An error occurred while inserting pets: {str(e)}")
    
    def findPetOwners(self):
        pipeline = [
            {
                "$lookup": {
                    "from": "users",
                    "localField": "_id",
                    "foreignField": "pets",
                    "as": "owners"
                }
            },
            {
                "$project": {
                    # "_id": 0,
                    # "birthDate": 0,
                    # "bride": 0,
                    "name": 1,
                    "type": 1,
                    # "weight": 0
                    "owners.name": 1
                }
            }
        ]
        result = self.conectaMongoDB.execute_aggregation('pets', pipeline)
        return result

    def findPetTypes(self, petType):
        query = {'type': petType}
        projection = {'name': 1, 'type': 1, 'weight': 1, '_id': 0}
        return self.conectaMongoDB.execute_query('pets', query, projection)
