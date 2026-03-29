from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    age: int
    diabetes_type: str
    medications: Optional[str] = None
    latest_glucose: Optional[float] = None
    hba1c: Optional[float] = None


class PatientUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    diabetes_type: Optional[str]
    medications: Optional[str]
    latest_glucose: Optional[float]
    hba1c: Optional[float]


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    diabetes_type: str
    medications: Optional[str]
    latest_glucose: Optional[float]
    hba1c: Optional[float]

    class Config:
        from_attributes = True 