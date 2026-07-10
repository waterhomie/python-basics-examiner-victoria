from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class AnswerRequest(BaseModel):
    session_id: str
    question: str
    user_answer: str
    target_score: float


class AnswerResponse(BaseModel):
    status: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    message: Optional[str] = None
    next_action: str


@app.get("/")
def home():
    return {
        "message": "Examiner Victoria Pydantic API is running."
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/api/answer", response_model=AnswerResponse)
def submit_answer(request_body: AnswerRequest):
    user_answer = request_body.user_answer

    if len(user_answer) < 10:
        return {
            "status": "too_short",
            "message": "Your answer is too short. Please add more details.",
            "next_action": "ask_user_to_expand"
        }

    return {
        "status": "ok",
        "score": 6.5,
        "feedback": "Your answer is clear, but you can add one specific example.",
        "next_action": "show_feedback"
    }