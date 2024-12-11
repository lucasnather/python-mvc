from typing import Dict
from src.model.interfaces.juridical_person_interface import JuridicalPersonInterface
from src.model.settings.connection import db_connection as DbConnection
from src.model.entities.juridical_person import JuridicalPerson

class JuridicalPersonRepository(JuridicalPersonInterface):
    def __init__(self, connection: DbConnection) -> None:
        self.connection = connection
    
    def create(self,revenue,age,dba, phone, corporative_email, category, balance) -> Dict:
        with self.connection as database:
            try:
                juridical_person = JuridicalPerson(
                    revenue=revenue,
                    age=age,
                    dba=dba,
                    phone=phone,
                    corporative_email=corporative_email,
                    category=category,
                    balance=balance
                )
                database.session.add(juridical_person)
                database.session.commit()
                return juridical_person
            except Exception as exception:
                raise exception
    
    def list_person_by_id(self,juridical_person_id) -> JuridicalPerson:
        with self.connection as database:
            try:
                juridical_person_by_id = database.session.query(JuridicalPerson).filter(JuridicalPerson.id == juridical_person_id).first()
                return juridical_person_by_id
            except Exception as exception:
                raise exception
            
    def transaction(self,juridical_person_id,money) -> JuridicalPerson:
        with self.connection as database:
            try:
                juridical_person = database.session.query(JuridicalPerson).filter(JuridicalPerson.id == juridical_person_id).first()
                juridical_person.balance = money
                database.session.add(juridical_person)
                database.session.commit()
                return juridical_person
            except Exception as exception:
                database.session.rollback()
                raise exception