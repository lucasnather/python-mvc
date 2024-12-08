from abc import abstractmethod, ABC

class NaturalPersonInterface(ABC):

    @abstractmethod
    def create(self,monthly_income, age, fullname, phone, email, category, balance) -> None:
        pass

    @abstractmethod
    def list_persons(self) -> None:
        pass

    @abstractmethod
    def list_person_by_id(self,person_id) -> None:
        pass

    @abstractmethod
    def withdraw(self,person_id, another_person_id, balance ) -> None:
        pass