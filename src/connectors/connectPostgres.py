from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
from sqlalchemy.sql import text
from models.postgresTables import Base
import logging

# print(DATABASE_URL)

class ConectaPostgreSQL:

    def __init__(self, databaseUrl):
        self.engine = create_engine(databaseUrl)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=self.engine))
                                                
        Base.query = self.session.query_property()
         
        # try catch para:  criar a base de dados apenas se ela já n tiver sido criada
        # quando já foi criada, dá erro
        try:
            Base.metadata.create_all(bind=ConectaPostgreSQL.engine)
            logging.info('TABELAS CRIADAS COM SUCESSO!!')
        except Exception as e:
            logging.info(f'{e}')
            print('{e}')

    def connect(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def disconnect(self):
        if self.session:
            self.session.close()
            self.session = None

    def execute_query(self, query):
        if self.session:
            result = self.session.execute(text(query))
            return result.fetchall()
        else:
            raise Exception('Not connected to a database.')