from abc import abstractmethod, ABC
from typing import Dict

class JuridicalPersonInterface(ABC):

    @abstractmethod
    def create(self,revenue,age,dba, phone, corporative_email, category, balance) -> Dict:
        pass
        