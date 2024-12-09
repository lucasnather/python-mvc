from src.view.interface.handle_requests import HandleRequests
from src.controller.create_juridical_person_controller import CreateJuridicalPersonController
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class CreateJuridicalPersonView(HandleRequests):
    def __init__(self, create_juridical_person_controller: CreateJuridicalPersonController) -> None:
        self.create_juridical_person_controller = create_juridical_person_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        juridical_person = self.create_juridical_person_controller.create(body)

        return HttpResponse(status_code=201, body=juridical_person)