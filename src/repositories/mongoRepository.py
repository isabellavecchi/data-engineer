from connectors.connectMongo import ConectaMongoDB

class UserMongoRepository():
    def __init__(self, conectaMongoDB: ConectaMongoDB):
        self.conectaMongoDB = conectaMongoDB
    
    def addUsers(self, dictUsers):
        result = self.conectaMongoDB.insert_documents('users', dictUsers)
        if not result.inserted_ids:
            print("No documents inserted.")
    
    def addUser(self, dictUser):
        result = self.conectaMongoDB.insert_document('users', dictUser)
        # if not result.inserted_ids:
        #     print("No documents inserted.")
