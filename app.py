from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_service import diabetes_rag
from config.schemas import PatientCreate, PatientResponse
from services.patient_service import (create_patient, get_all_patients, get_patient, update_patient, delete_patient)

class Question(BaseModel):
    question: str

app = FastAPI(
    title="DM Buddy RAG API",
    description="AI Assistant for diabetes patient questions",
    version="1.0"
)

@app.post("/chat")
def ask_diabetes_question(data: Question):

    result = diabetes_rag(data.question)

    return {
        "question": data.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }

@app.post("/patients", response_model=PatientResponse)
def create_patient_endpoint(data: PatientCreate):
    return create_patient(data)

@app.get("/health")
async def health_check():
    return {"status": "ok"}


