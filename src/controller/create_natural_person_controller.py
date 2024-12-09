import re
from typing import Dict
from src.model.entities.natural_person import NaturalPerson
from src.controller.interface.create_natural_person_interface import CreateNaturalPersonInterface
from src.model.interfaces.natural_person_interface import NaturalPersonInterface

class CreateNaturalPersonController(CreateNaturalPersonInterface):
    def __init__(self, natural_person_repository: NaturalPersonInterface) -> None:
        self.natural_person_repository = natural_person_repository

    def create(self, natural_person: Dict) -> NaturalPerson:
        monthly_income = natural_person["monthly_income"]
        age = natural_person["age"]
        fullname = natural_person["fullname"]
        phone = natural_person["phone"]
        email = natural_person["email"]
        category = natural_person["category"]
        balance = natural_person["balance"]

        validate_age = self.__validation__age(age)
        validate_email = self.__validation_email(email)
        validate_phone= self.__validation_phone(phone)
        validate_balance= self.__validation__balance(balance)

        insert_into = self.__insert_into_database(
            monthly_income=monthly_income,
            age=validate_age,
            fullname=fullname,
            phone=validate_phone,
            email=validate_email,
            category=category,
            balance=validate_balance
        )

        formatted_response = self.__format_response(insert_into)

        return formatted_response
    
    def __validation__age(self, age) -> float:
        if age < 18:
            raise Exception("Age Not Valid")
        
        return age
    
    def __validation__balance(self, balance) -> float:
        if balance <= 0:
            raise Exception("Balance Not Valid")
        
        return balance
    
    
    def __validation_email(self, email):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$"

        if re.match(email_regex, email):
            return True
        return False
    
    def __validation_phone(self, phone):
        phone_regex = r"^\+\d{11}$"

        if re.match(phone_regex, phone):
            return True
        return False

    def __insert_into_database(self,monthly_income, age, fullname, phone, email, category, balance):
        natural_person = self.natural_person_repository.create(
            monthly_income, age, fullname, phone, email, category, balance
        )
        return natural_person
    
    def __format_response(self, natural_person: Dict):
        return {
            "monthly_income": natural_person["monthly_income"],
            "age": natural_person["age"],
            "fullname": natural_person["fullname"],
            "phone": natural_person["phone"],
            "email": natural_person["email"],
            "category": natural_person["category"],
            "balance": natural_person["balance"],
        }