from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interface.handle_requests import HandleRequests
from src.controller.transaction_natural_person_controller import TransactionNaturalPersonController

class TransactionNaturalPersonView(HandleRequests):
    def __init__(self, transaction_controller: TransactionNaturalPersonController) -> None:
        self.transaction_controller = transaction_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person = http_request.param
        money = http_request.body

        body = self.transaction_controller.transaction(natural_person, money)

        return HttpResponse(status_code=201, body=body)