from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Examiner Victoria API is running."
    }

@app.get("/api/health")
def health_check():
    return {
        "status": "ok"
    }

@app.post("/api/answer")
def submit_answer(request_body: dict):
    user_answer = request_body["user_answer"]

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

# Request Body:
# session_id: 当前练习会话 ID
# question: 当前题目
# user_answer: 用户回答

# Response Body:
# status: 回答状态
# score: 分数
# feedback: 反馈内容
# next_action: 前端下一步动作