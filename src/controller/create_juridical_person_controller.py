from typing import Dict
import re
from src.controller.interface.create_juridical_person_interface import CreateJuridicalPersonInterface
from src.model.interfaces.juridical_person_interface import JuridicalPersonInterface

class CreateJuridicalPersonController(CreateJuridicalPersonInterface):
    def __init__(self, juridical_person_repository: JuridicalPersonInterface) -> None:
        self.juridical_person_repository = juridical_person_repository
    
    def create(self, juridical_person: Dict) -> Dict:
        revenue = juridical_person["revenue"]
        age = juridical_person["age"]
        dba = juridical_person["dba"]
        phone = juridical_person["phone"]
        corporative_email = juridical_person["corporative_email"]
        category = juridical_person["category"]
        balance = juridical_person["balance"]

        validate_age = self.__validation__age(age)
        validate_balance = self.__validation__balance(balance)
        validate_corporative_email = self.__validation_corporative_email(corporative_email)
        validate_phone = self.__validation_phone(phone)

        self.__insert_into_database(
            revenue,
            validate_age,
            dba,
            validate_phone,
            validate_corporative_email,
            category,
            validate_balance
        )

        formatted_response = self.format_response(juridical_person)

        return formatted_response

    def __validation__age(self, age) -> float:
        if age < 18:
            raise Exception("Age Not Valid")
        
        return age
    
    def __validation__balance(self, balance) -> float:
        if balance <= 0:
            raise Exception("Balance Not Valid")
        
        return balance
    
    
    def __validation_corporative_email(self, corporative_email):
        corporative_email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$"

        if re.match(corporative_email_regex, corporative_email):
            return corporative_email
        raise Exception("Corporative Email Not Valid")
    
    def __validation_phone(self, phone):

        phone_regex = r"^\+\d{11}$"

        if re.match(phone_regex, phone):
            return phone
        
        raise Exception("Phone Not Valid")
    
    def __insert_into_database(self, revenue, age, dba, phone, corporative_email, category, balance):
        self.juridical_person_repository.create(
            revenue=revenue,
            age=age,
            dba=dba,
            phone=phone,
            corporative_email=corporative_email,
            category=category,
            balance=balance
        )

    def format_response(self, juridical_person):
        return {
            "data": {
                "type": "Juridical Person",
                "count": 1,
                "attributes": juridical_person
            }
        }