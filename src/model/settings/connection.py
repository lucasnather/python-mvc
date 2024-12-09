from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnection():
    
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connection(self): 
        self.__engine = create_engine(self.__connection_string)

        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection = DbConnection()