question = "Describe a city you want to visit."
user_answer = "I want to visit Paris because it has beautiful architecture."
feedback = "Your answer is clear, but you can add one specific example."

def save_practice_record(question, user_answer, feedback):
    record = f"""
--------------------
Question:
{question}

User Answer:
{user_answer}

Feedback:
{feedback}
"""

    with open("practice_record.txt", "a", encoding="utf-8") as file:
        file.write(record)

    print("Practice record saved.")

save_practice_record(question, user_answer, feedback)

