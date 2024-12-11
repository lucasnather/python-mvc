from abc import abstractmethod, ABC
from typing import List
from src.model.entities.natural_person import NaturalPerson

class NaturalPersonInterface(ABC):

    @abstractmethod
    def create(self,monthly_income, age, fullname, phone, email, category, balance) -> None:
        pass

    @abstractmethod
    def list_persons(self) -> List[NaturalPerson]:
        pass

    @abstractmethod
    def list_person_by_id(self,natural_person_id) -> NaturalPerson:
        pass

    @abstractmethod
    def transaction(self,natural_person_id,money) -> NaturalPerson:
        pass