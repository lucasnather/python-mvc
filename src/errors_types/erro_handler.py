from src.view.http_types.http_response import HttpResponse
from .age_exception import AgeException
from .balance_exception import BalanceException
from .email_exception import EmailException
from .invalid_id_exception import InvalidIdException
from .phone_exception import PhoneException

def erro_handler(exception: Exception):
    if isinstance(exception, (AgeException, BalanceException, EmailException, InvalidIdException, PhoneException)):
        error = {
            "message": exception.message,
            "status_code": exception.status_code,
            "name": exception.name
        }

        return HttpResponse(error["status_code"], body=error)
    
    server_error = {
        "message": "Server Internal Error",
        "status_code": 500,
        "name": "Server Error"
    }

    return HttpResponse(server_error["status_code"], body=server_error)
