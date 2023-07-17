from pymongo import MongoClient

class ConectaMongoDB:
    def __init__(self, host='localhost', port=27017, database=None, username=None, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
        self.db = self.client[self.database]
        print("conectado")

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def execute_query(self, collection_name, query):
        collection = self.get_collection(collection_name)
        return collection.find(query)

    def get_collection(self, collection_name):
        if self.db is not None:
            return self.db[collection_name]
        else:
            raise Exception('Not connected to a database.')

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        return collection.insert_one(document)

    def insert_documents(self, collection_name, documents):
        collection = self.get_collection(collection_name)
        return collection.insert_many(documents)

    def update_document(self, collection_name, query, update):
        collection = self.get_collection(collection_name)
        return collection.update_many(query, update)

    def delete_documents(self, collection_name, query=None):
        collection = self.get_collection(collection_name)
        return collection.delete_many(query)
