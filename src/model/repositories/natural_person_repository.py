from typing import List
from src.model.interfaces.natural_person_interface import NaturalPersonInterface
from src.model.entities.natural_person import NaturalPerson
from src.model.settings.connection import db_connection as DbConnection

class NaturalPersonRepository(NaturalPersonInterface):

    def __init__(self, db_connection: DbConnection) -> None:
        self.db_connection = db_connection

    
    def create(self,monthly_income: float, age: int, fullname: str, phone: str, email: str, category: str, balance: float):
        with self.db_connection as database:
            try:
                natural_person = NaturalPerson(monthly_income, age, fullname, phone, email, category, balance)
                database.session.add(natural_person)
                database.sesstion.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_persons(self) -> List[NaturalPerson]:
        with self.db_connection as database:
            try:
                natural_person = database.session.query(NaturalPerson).all()
                return natural_person
            except Exception as exception:
                raise exception
        

    def list_person_by_id(self,person_id) -> NaturalPerson:
        with self.db_connection as database:
            try:
                natural_person_by_id = database.session.query(NaturalPerson).filter(id=person_id)
                return natural_person_by_id
            except Exception as exception:
                raise exception
        

    def withdraw(self,natural_person_id,money) -> NaturalPerson:
        with self.db_connection as database:
            try:
                natural_person = database.session.query(NaturalPerson).filter(id=natural_person_id)
                natural_person.balance = money
                return natural_person
            except Exception as exception:
                raise exception

        
