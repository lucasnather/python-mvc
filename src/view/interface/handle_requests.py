from abc import abstractmethod, ABC
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class HandleRequests(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass