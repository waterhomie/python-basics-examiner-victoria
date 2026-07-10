question = "Describe a city you want to visit."
user_answer = "I want to visit Paris because of its rich history, beautiful architecture, and world-famous cuisine. I have always been fascinated by the Eiffel Tower and the Louvre Museum. Additionally, I would love to experience the local culture, try authentic French pastries, and take a stroll along the Seine River."

print("Question:")
print(question)

print("User Answer:")
print(user_answer)

min_length = 10

if not user_answer:
    print("Please enter your answer first.")
elif len(user_answer) < 10:
    print("Your answer is too short. Please add more details.")
else:
    print("Answer received. Now we can generate feedback.")
    feedback = "Your answer is clear, but you can add one specific example."
    print(feedback)
    
