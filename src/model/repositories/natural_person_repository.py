from src.model.interfaces.natural_person_interface import NaturalPersonInterface

class NaturalPersonRepository:
    def __init__(self, db_connection: NaturalPersonInterface) -> None:
        self.db_connetion = db_connection