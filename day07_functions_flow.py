def build_feedback_prompt(question, user_answer):
    prompt = f"""
You are an IELTS speaking examiner.

Part:
{question["part"]}

Topic:
{question["topic"]}

Question:
{question["text"]}

Student Answer:
{user_answer}

Please give feedback on:
1. Fluency
2. Vocabulary
3. Grammar
4. One suggestion for improvement
5. A better version of the student's answer
"""
    return prompt

current_question = {
    "part": "Part 2",
    "topic": "City",
    "text": "Describe a city you want to visit."
}

user_answer = "I want to visit Paris because it has beautiful architecture."

prompt = build_feedback_prompt(current_question, user_answer)

print(prompt)