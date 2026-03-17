from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_service import diabetes_rag

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

@app.get("/health")
async def health_check():
    return {"status": "ok"}


