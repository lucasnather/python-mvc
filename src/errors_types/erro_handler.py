from .age_exception import AgeException
from .balance_exception import BalanceException
from .email_exception import EmailException
from .invalid_id_exception import InvalidIdException
from .phone_exception import PhoneException

def erro_handler(exception: Exception):
    if isinstance(exception, (AgeException, BalanceException, EmailException, InvalidIdException, PhoneException)):
        return {
            "message": exception.message,
            "status_code": exception.status_code,
            "name": exception.name
        }
    
    return {
        "message": "Server Internal Error",
        "status_code": 500,
        "name": "Server Error"
    }
