from typing import Dict
from src.controller.interface.transaction_jurifical_person_interface import TransactionJuridicalPersonInterface
from src.model.interfaces.juridical_person_interface import JuridicalPersonInterface
from src.errors_types.balance_exception import BalanceException
from src.errors_types.invalid_id_exception import InvalidIdException

class TransactionNaturalPersonController(TransactionJuridicalPersonInterface):
    def __init__(self, juridical_person_repository: JuridicalPersonInterface) -> None:
        self.juridical_person_repository = juridical_person_repository

    def transaction(self, juridical_person_id, money) -> Dict: 

        balance = money["balance"]

        validate_id = self.__validation_id(juridical_person_id)
        validate_balance = self.__validation_balance(balance)

        juridical_person_actual_balance = self.__find_person_by_id(validate_id)

        new_balance = self.__calculate_transaction_balance(juridical_person_actual_balance, validate_balance)
        self.__transaction_database(validate_id, new_balance)

        formatted_response = self.__format_response(new_balance)
        
        return formatted_response


    def __validation_id(self, juridical_person_id):
        if not isinstance(juridical_person_id, int):  
            raise InvalidIdException("Id precisar ser do tipo Inteiro")
        
        return juridical_person_id
    
    def __validation_balance(self, balance):
        if balance <= 0:
            raise BalanceException("Saldo enviado menor que 0")
        if balance > 8000:
            raise BalanceException("O saldo máximo para Pessoas Físicas é de R$ 8000,00")
    
        return balance
    
    def __calculate_transaction_balance(self, actual_balance, balance):

        if actual_balance < balance:
            raise BalanceException("O dinheiro que você solicitou é maior que o saldo")

        new_balance = actual_balance - balance

        return new_balance
    
    def __transaction_database(self, juridical_person_id, balance):
        self.juridical_person_repository.transaction(juridical_person_id, balance)

    def __find_person_by_id(self, juridical_person_id):
        juridical_person = self.juridical_person_repository.list_person_by_id(juridical_person_id)

        if juridical_person.balance == 0:
            raise BalanceException("Seu saldo está vazio")

        return juridical_person.balance

    def __format_response(self, balance):
        return {
            "data": {
                "type": "Transaction",
                "count": 1,
                "balance": balance
            }
        }