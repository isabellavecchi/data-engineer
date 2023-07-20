from pymongo import MongoClient

class ConectaMongoDB:
    def __init__(self, connection_string, database=None):
        self.connection_string = connection_string
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client.get_database(self.database)
            print("Connected to MongoDB.")
        except Exception as e:
            print(f"An error occurred while connecting to MongoDB: {str(e)}")

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def execute_query(self, collection_name, query, projection=None):
        collection = self.get_collection(collection_name)
        return collection.find(query, projection)
    
    def execute_aggregation(self, collection_name, pipeline):
        collection = self.get_collection(collection_name)
        return collection.aggregate(pipeline)

    def get_collection(self, collection_name):
        try:
            if self.db is not None:
                return self.db[collection_name]
            else:
                raise Exception('Not connected to a database.')
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")

    def insert_document(self, collection_name, document):
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_one(document)
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")

    def insert_documents(self, collection_name, documents):
        try:
            collection = self.get_collection(collection_name)
            return collection.insert_many(documents)
        except Exception as e:
            print(f"An error occurred while inserting users: {str(e)}")

    def update_document(self, collection_name, query, update):
        collection = self.get_collection(collection_name)
        return collection.update_many(query, update)

    def delete_documents(self, collection_name, query=None):
        collection = self.get_collection(collection_name)
        return collection.delete_many(query)
