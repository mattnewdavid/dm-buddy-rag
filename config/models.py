# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    diabetes_type = Column(String)  # Type 1 / Type 2
    medications = Column(String)
    latest_glucose = Column(Float)
    hba1c = Column(Float)