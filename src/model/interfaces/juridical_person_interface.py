from abc import abstractmethod, ABC
from typing import Dict
from src.model.entities.juridical_person import JuridicalPerson

class JuridicalPersonInterface(ABC):

    @abstractmethod
    def create(self,revenue,age,dba, phone, corporative_email, category, balance) -> Dict:
        pass

    @abstractmethod
    def list_person_by_id(self,juridical_person_id) -> JuridicalPerson:
        pass

    @abstractmethod
    def transaction(self,juridical_person_id, money) -> JuridicalPerson:
        pass
        