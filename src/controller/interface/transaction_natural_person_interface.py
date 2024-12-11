from typing import Dict
from abc import abstractmethod, ABC

class TransactionNaturalPersonInterface(ABC):

    @abstractmethod
    def transaction(self, natural_person_id, money) -> Dict:
        pass