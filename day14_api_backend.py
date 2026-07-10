from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS: Cross-Origin Resource Sharing
# 本地学习阶段先允许所有来源访问后端接口。
# 真实上线产品里不能长期这样开放。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnswerRequest(BaseModel):
    session_id: str
    question: str
    user_answer: str
    target_score: float


class AnswerResponse(BaseModel):
    status: str
    score: float | None = None
    feedback: str | None = None
    message: str | None = None
    next_action: str


@app.get("/")
def home():
    return {"message": "Examiner Victoria Frontend API is running."}


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/answer", response_model=AnswerResponse)
def submit_answer(request_body: AnswerRequest):
    user_answer = request_body.user_answer

    if len(user_answer) < 10:
        return {
            "status": "too_short",
            "score": None,
            "feedback": None,
            "message": "Your answer is too short. Please add more details.",
            "next_action": "ask_user_to_expand",
        }

    return {
        "status": "ok",
        "score": 6.5,
        "feedback": "Your answer is clear, but you can add one specific example.",
        "message": None,
        "next_action": "show_feedback",
    }