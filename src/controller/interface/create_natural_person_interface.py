from typing import Dict
from abc import abstractmethod, ABC
from src.model.entities.natural_person import NaturalPerson

class CreateNaturalPersonInterface(ABC):

    @abstractmethod
    def create(self,natural_person: Dict) -> NaturalPerson:
        pass