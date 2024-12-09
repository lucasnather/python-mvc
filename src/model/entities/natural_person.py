from sqlalchemy import Column, Integer, Float, TEXT
from src.model.settings.base import Base

class NaturalPerson(Base):
    __tablename__ = "natural_person"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    monthly_income = Column(Float)
    age = Column(Integer)
    fullname = Column(TEXT)
    phone = Column(TEXT, unique=True)
    email = Column(TEXT, unique=True)
    category = Column(TEXT)
    balance = Column(Float)

    def __repr__(self):
        return "Natural Person create"