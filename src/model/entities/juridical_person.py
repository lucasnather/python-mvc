from sqlalchemy import Column, Integer, Float, TEXT
from src.model.settings.base import Base

class JuridicalPerson(Base):
    
    __tablename__ = "juridical_person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    revenue = Column(Float)
    age = Column(Integer)
    dba = Column(TEXT)
    phone = Column(TEXT, unique=True)
    corporative_email = Column(TEXT, unique=True)
    category = Column(TEXT)
    balance = Column(Float)

    def __repr__(self) -> str:
        to_dict = {
            "revenue", self.revenue,
            "age", self.age,
            "dba", self.dba,
            "phone", self.phone,
            "corporative_email", self.corporative_email,
            "category", self.category,
            "balance", self.balance,
        }

        return str(to_dict)