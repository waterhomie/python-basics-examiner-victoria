def submit_answer_api(request_body):
    user_answer = request_body["user_answer"]
    required_answer_length = 10

    if not user_answer:
        return {
            "status": "error",
            "message": "Please enter your answer first.",
            "next_action": "ask_user_to_input"
        }

    elif len(user_answer) < required_answer_length:
        return {
            "status": "too_short",
            "message": "Your answer is too short. Please add more details.",
            "next_action": "ask_user_to_expand"
        }

    else:
        return {
            "status": "ok",
            "score": 6.5,
            "feedback": "Your answer is clear, but you can add one specific example.",
            "next_action": "show_feedback"
        }


request_body = {
    "session_id": "practice_001",
    "question": "Describe a city you want to visit.",
    "user_answer": "I want to visit Paris because it has beautiful architecture."
}

response_body = submit_answer_api(request_body)

print("Status:")
print(response_body["status"])

print("Next Action:")
print(response_body["next_action"])

if response_body["status"] == "ok":
    print("Score:")
    print(response_body["score"])

    print("Feedback:")
    print(response_body["feedback"])
else:
    print("Message:")
    print(response_body["message"])