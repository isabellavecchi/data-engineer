import pandas as pd
import requests

class DataReader:
    def __init__(self, documentId, outputFile):
        self.fileUrl = 'https://docs.google.com/spreadsheets/d/' + documentId + '/gviz/tq?tqx=out:csv'
        self.outputFile = "./" + outputFile

        self.dfUsers = self.readExcel("User")
        self.dfUsers['birthDate'] = pd.to_datetime(self.dfUsers['birthDate'], format='%d/%m/%Y')

        self.dfAddresses = self.readExcel("Address")
        self.dfAddresses['state'] = self.dfAddresses['state'].astype('category')
        self.dfAddresses['country'] = self.dfAddresses['country'].astype('category')

        self.dfPets = self.readExcel("Pet")
        self.dfPets['type'] = self.dfPets['type'].astype('category')
        self.dfPets['birthDate'] = pd.to_datetime(self.dfPets['birthDate'], format='%d/%m/%Y')

        self.dfUserPets = self.readExcel("UserPet")


    def downloadExcel(self):
        response = requests.get(self.fileUrl)
        with open(self.outputFile, 'wb') as file:
            file.write(response.content)

    # Funcao para colocar uma folha do excel num dataframe do Pandas, uma por vez]
    def readExcel(self, sheetName):
        url = self.fileUrl + '&sheet=' + sheetName
        df = pd.read_csv(url)
        return df
    
    # Funcao para escrever um array de dataFrames num unico arquivo excel, separado por folhas  
    def writeExcel(self, dataframes):
        writer = pd.ExcelWriter(self.outputFile, engine='xlsxwriter')
        
        for sheetName, df in dataframes.items():
            df.to_excel(writer, sheetName=sheetName, index=False)

        writer.save()

    # Funcao que retorna um Dataframe de usuarios com seus respectivos enderecos
    def getUsersWithAddress(self):

        self.dfUsers = pd.merge(self.dfUsers, self.dfAddresses, 
                        left_on='id', right_on='idUser',
                        validate='1:1')
        self.dfUsers = self.dfUsers.drop('idUser', axis=1)
        return self.dfUsers
    
    def getPets(self):
        return self.dfPets
    
    def updatePetIds(self, petMongoIds):
        # self.dfPets['_id'] = petMongoIds
        # Create a dictionary mapping the old Person IDs to the new Person IDs
        pet_id_mapping = dict(zip(self.dfPets['id'], petMongoIds))

        # Update the idPet column in self.dfUserPets with the new Person IDs
        self.dfPets['id'] = self.dfPets['id'].map(pet_id_mapping)
        self.dfUserPets['idPet'] = self.dfUserPets['idPet'].map(pet_id_mapping)
        return self.dfPets, self.dfUserPets

    def mergeUsersWithPets(self):
        dfUserArrPetIds = pd.merge(self.dfUsers, self.dfUserPets,
                           left_on='id', right_on='idUser',
                           validate='m:m')
        self.dfUsers['pets'] = (dfUserArrPetIds.groupby('id')['idPet']
                            .apply(list)
                            .reset_index()['idPet'])
        return self.dfUsers