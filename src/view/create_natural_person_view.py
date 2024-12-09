from src.view.interface.handle_requests import HandleRequests
from src.controller.create_natural_person_controller import CreateNaturalPersonController
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class CreateNaturalPersonView(HandleRequests):

    def __init__(self, create_natural_person_controller: CreateNaturalPersonController) -> None:
        self.create_natural_person_controller = create_natural_person_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        natural_person = self.create_natural_person_controller.create(body)

        return HttpResponse(status_code=201, body=natural_person)