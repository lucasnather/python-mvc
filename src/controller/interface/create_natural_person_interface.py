from typing import Dict
from abc import abstractmethod, ABC

class CreateNaturalPersonInterface(ABC):

    @abstractmethod
    def create(self,natural_person: Dict) -> Dict:
        pass