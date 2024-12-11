from typing import Dict
from src.controller.interface.transaction_natural_person_interface import TransactionNaturalPersonInterface
from src.model.interfaces.natural_person_interface import NaturalPersonInterface

class TransactionNaturalPersonController(TransactionNaturalPersonInterface):
    def __init__(self, natural_person_repository: NaturalPersonInterface) -> None:
        self.natural_person_repository = natural_person_repository

    def transaction(self, natural_person_id, money) -> Dict: 

        balance = money["balance"]

        validate_id = self.__validation_id(natural_person_id)
        validate_balance = self.__validation_balance(balance)

        natural_person_actual_balance = self.__find_person_by_id(validate_id)

        new_balance = self.__calculate_transaction_balance(natural_person_actual_balance, validate_balance)
        self.__transaction_database(validate_id, new_balance)

        formatted_response = self.__format_response(new_balance)
        
        return formatted_response


    def __validation_id(self, natural_person_id):
        if not isinstance(natural_person_id, int):  
            raise Exception("Id Not Valid")
        
        return natural_person_id
    
    def __validation_balance(self, balance):
        if balance <= 0:
            raise Exception("Balance not Valid")
        
        if balance > 4000:
            raise Exception("Balance with more than 4000 Not Valid ")
        
        return balance
    
    def __calculate_transaction_balance(self, actual_balance, balance):

        if actual_balance < balance:
            raise Exception("Money bigger than your balance")

        new_balance = actual_balance - balance

        return new_balance
    
    def __transaction_database(self, natural_person_id, balance):
        self.natural_person_repository.transaction(natural_person_id, balance)

    def __find_person_by_id(self, natural_person_id):
        natural_person = self.natural_person_repository.list_person_by_id(natural_person_id)

        if natural_person.balance == 0:
            raise Exception("Your balance is empty")

        return natural_person.balance

    def __format_response(self, balance):
        return {
            "data": {
                "type": "Transaction",
                "count": 1,
                "balance": balance
            }
        }