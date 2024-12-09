from abc import abstractmethod, ABC
from typing import Dict

class CreateJuridicalPersonInterface(ABC):

    @abstractmethod
    def create(self, juridical_person: Dict) -> Dict:
        pass