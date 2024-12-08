from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnection():
    
    def __init__(self) -> None:
        self.connection_string = "sqlite:///storage.db"
        self.engine = None
        self.session = None

    def connection(self): 
        self.engine = create_engine(self.connection)

        return self.engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db = DbConnection()