from typing import Dict
from abc import abstractmethod, ABC

class TransactionJuridicalPersonInterface(ABC):

    @abstractmethod
    def transaction(self, juridical_person_id, money) -> Dict:
        pass