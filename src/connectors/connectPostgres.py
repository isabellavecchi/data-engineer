from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
from sqlalchemy.sql import text
from models.postgresTables import Base
import logging

# print(DATABASE_URL)

class ConectaPostgreSQL:
    #variaveis estaticas
    DATABASE_URL = 'postgresql+psycopg2://postgres:postgrespw@localhost:49153/peTinder'
    engine = create_engine(DATABASE_URL)
    # engine = create_engine("postgresql+psycopg2://postgres:postgrespw@localhost:49153/peTinder", echo=False)
        #esta ferramenta funciona para vários bancos!
        #"postgresql+driver://usuario:senha@computador/bd")
            #echo=True para mostrar as informações de log

    #constructor
    
    """ def __init__(self):
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=ConectaPostgreSQL.engine))
                                                
        Base.query = db_session.query_property()
         
        import models
        # try catch para:  criar a base de dados apenas se ela já n tiver sido criada
        # quando já foi criada, dá erro
        try:
            Base.metadata.create_all(bind=ConectaPostgreSQL.engine)
            logging.info('TABELAS CRIADAS COM SUCESSO!!')
        except Exception as e:
            logging.info(f'{e}')
            print('{e}')
            
    
    def getConnection(self):
        try:
            Session = sessionmaker(ConectaPostgreSQL.engine)
            session = Session()
            conn = ConectaPostgreSQL.engine.connect()
            return session, conn
        except Exception as e:
            logging.info(f'XABUUUUU ... {e}')
 """
    def __init__(self, db_url):
        try:
            self.db_url = db_url
            self.engine = create_engine(db_url)
            self.metadata = MetaData(bind=self.engine)
            self.session = None
            # try catch para:  criar a base de dados apenas se ela já n tiver sido criada
            # quando já foi criada, dá erro
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

    def create_tables(self, models):
        self.metadata.create_all()

    def execute_query(self, query):
        if self.session:
            result = self.session.execute(text(query))
            return result.fetchall()
        else:
            raise Exception('Not connected to a database.')