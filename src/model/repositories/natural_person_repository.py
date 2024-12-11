from typing import List
from src.model.interfaces.natural_person_interface import NaturalPersonInterface
from src.model.entities.natural_person import NaturalPerson
from src.model.settings.connection import db_connection as DbConnection

class NaturalPersonRepository(NaturalPersonInterface):

    def __init__(self, connection: DbConnection) -> None:
        self.connection = connection

    
    def create(self,monthly_income, age, fullname, phone, email, category, balance):
        with self.connection as database:
            try:
                natural_person = NaturalPerson(
                    monthly_income=monthly_income, 
                    age=age, 
                    fullname=fullname, 
                    phone=phone, 
                    email=email, 
                    category=category, 
                    balance=balance
                    )
                database.session.add(natural_person)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_persons(self) -> List[NaturalPerson]:
        with self.connection as database:
            try:
                natural_person = database.session.query(NaturalPerson).all()
                return natural_person
            except Exception as exception:
                raise exception
        

    def list_person_by_id(self,natural_person_id) -> NaturalPerson:
        with self.connection as database:
            try:
                natural_person_by_id = database.session.query(NaturalPerson).filter(NaturalPerson.id == natural_person_id).first()
                return natural_person_by_id
            except Exception as exception:
                raise exception
        

    def transaction(self,natural_person_id,money) -> NaturalPerson:
        with self.connection as database:
            try:
                natural_person = database.session.query(NaturalPerson).filter(NaturalPerson.id == natural_person_id).first()
                natural_person.balance = money
                database.session.add(natural_person)
                database.session.commit()
                return natural_person
            except Exception as exception:
                database.session.rollback()
                raise exception

        
