question = "Describe a city you want to visit."
user_answer = "I want to visit Tokyo because it is modern, clean, and full of interesting places."

system_prompt = "You are an IELTS speaking examiner."

target_score = 7.0

user_prompt = f"""
Question:
{question}

Student Answer:
{user_answer}

The student's target IELTS speaking score is {target_score}.

Please give feedback on:
1. Fluency
2. Vocabulary
3. Grammar
4. One suggestion for improvement
5. A better version of the student's answer 
"""

print("System Prompt:")
print(system_prompt)

print("User Prompt:")
print(user_prompt)