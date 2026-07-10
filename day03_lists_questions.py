import random

questions = [
    "Where is your hometown?",
    "Do you like your hometown?",
    "Describe a city you want to visit.",
    "Describe a person who helped you.",
    "Describe a place you like.",
    "Do you prefer studying alone or with others?"
]

print("All Questions:")
print(questions)

print("First Question:")
print(questions[0])

print("Second Question:")
print(questions[1])

print("Third Question:")
print(questions[2])

question_count = len(questions)

print("Question Count:")
print(question_count)

random_question = random.choice(questions)

print("Random Question:")
print(random_question)

questions.append("Describe a useful app you often use.")
question_count = len(questions)

print("Updated Question Count:")
print(question_count)