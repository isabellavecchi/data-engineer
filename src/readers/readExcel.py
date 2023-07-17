import pandas as pd
import requests

class DataReader:
    def __init__(self, documentId, outputFile):
        self.fileUrl = 'https://docs.google.com/spreadsheets/d/' + documentId + '/gviz/tq?tqx=out:csv'
        self.outputFile = "./" + outputFile

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
    def getUsersWithAddressDF(self):
        dfUsers = self.readExcel("User")
        dfAddresses = self.readExcel("Address")

        dfUsers['date'] = pd.to_datetime(dfUsers['birthDate'], format='%d/%m/%Y')
        dfUsers = pd.merge(dfUsers, dfAddresses, 
                        left_on='id', right_on='idUser',
                        validate='1:1')
        dfUsers = dfUsers.drop('idUser', axis=1)
        return dfUsers

    # Funcao que retorna um Dataframe de Pets
    def getPetsDF(self):
        dfPets = self.readExcel("Pet")
        dfPets['type'] = dfPets['type'].astype('category')
        return dfPets