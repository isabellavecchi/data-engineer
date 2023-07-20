from readers.readExcel import DataReader
from models.address import Address
from models.pet import Pet
from models.user import User
from models.postgresTables import TbUser,TbPet,TbUserPet
from connectors.connectPostgres import ConectaPostgreSQL
from connectors.connectMongo import ConectaMongoDB
from repositories.mongoRepository import UserMongoRepository, PetMongoRepository
from services.mongoService import UserMongoService, PetMongoService
from repositories.postgresRepository import UserPostgresRepository

# Id para a planilha do google docs
file_id = '1CvfQISaVMObNajt_WmOJxFgTE0X2zhi_avX2wSFfl4g'
output_file = 'data.xlsx'

# Create an instance of the DataReader class
data_reader = DataReader(file_id, output_file)

# # Instantiate the MongoDBConnector
mongo_connector = ConectaMongoDB(connection_string='mongodb+srv://admin:password@192.168.0.10', database='petMatch')

# # Connect to MongoDB
mongo_connector.connect()
userMongoRepository = UserMongoRepository(mongo_connector)
petMongoRepository = PetMongoRepository(mongo_connector)
userMongoService = UserMongoService(userMongoRepository)
petMongoService = PetMongoService(petMongoRepository)

data_reader.df_pets = data_reader.getPets()
petMongoIds = petMongoService.addPetsFromDF(data_reader.df_pets)
data_reader.dfPets, data_reader.dfUserPets = data_reader.updatePetIds(petMongoIds)

data_reader.df_users = data_reader.getUsersWithAddress()
data_reader.df_users = data_reader.mergeUsersWithPets()

print(data_reader.df_users.head(8))
print(data_reader.df_pets.head())
userMongoService.addUsersFromDF(data_reader.df_users)

userMongoService.findUsersFromCountry("BR")
userMongoService.findUsersWithPets()
petMongoService.findPetOwners()
petMongoService.findPetTypes('cat')

postgres_connector = ConectaPostgreSQL('postgresql+psycopg2://postgres://admin:password@192.168.0.11/petMatch')

postgres_connector.connect()
userPostgresRepository = UserPostgresRepository(postgres_connector)
# petPostgresRepository = PetPostgresRepository(postgres_connector)
# userPostgresService = UserPostgresService(userPostgresRepository)
# petPostgresService = PetPostgresService(petPostgresRepository)

mongo_connector.disconnect()
postgres_connector.disconnect()