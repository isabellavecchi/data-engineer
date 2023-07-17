from readers.readExcel import DataReader
from models.address import Address
from models.pet import Pet
from models.user import User
from models.postgresTables import TbUser,TbPet,TbUserPet
from connectors.connectPostgres import ConectaPostgreSQL
from connectors.connectMongo import ConectaMongoDB
# from repositories.postgresRepository import 
from repositories.mongoRepository import UserMongoRepository
from services.mongoService import UserMongoService

# Id para a planilha do google docs
file_id = '1CvfQISaVMObNajt_WmOJxFgTE0X2zhi_avX2wSFfl4g'
output_file = 'data.xlsx'

# Create an instance of the DataReader class
data_reader = DataReader(file_id, output_file)

# Read specific sheets and populate class objects
df_users = data_reader.getUsersWithAddressDF()
df_pets = data_reader.getPetsDF()

print(df_users.head())
print(df_pets.head())

# # Instantiate the MongoDBConnector
mongo_connector = ConectaMongoDB(host='192.168.0.10', port=27017, database='database', username='admin', password='password')

# # Connect to MongoDB
mongo_connector.connect()
userMongoRepository = UserMongoRepository(mongo_connector)
userMongoService = UserMongoService(userMongoRepository)

userMongoService.addUsersFromDF(df_users)


# # Insert a document
# document = {'name': 'John Doe', 'age': 30}
# mongo_connector.insert_document('mycollection', document)

# # Find documents
# documents = mongo_connector.find_documents('mycollection')
# for document in documents:
#     print(document)

# # Update documents
# query = {'age': {'$lt': 40}}
# update = {'$set': {'age': 40}}
# mongo_connector.update_document('mycollection', query, update)

# # Delete documents
# query = {'age': 40}
# mongo_connector.delete_documents('mycollection', query)

# # Disconnect from MongoDB
# mongo_connector.disconnect()