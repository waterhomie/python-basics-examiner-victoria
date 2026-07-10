question = {
    "part": "Part 1",
    "topic": "Hometown",
    "text": "Where is your hometown?",
    "difficulty": "easy"
}

print("Question Object:")
print(question)

print("Part:")
print(question["part"])

print("Topic:")
print(question["topic"])

print("Question Text:")
print(question["text"])

question["difficulty"] = "medium"

print("Updated Difficulty:")
print(question["difficulty"])

question["source"] = "practice demo"

print("Source:")
print(question["source"])

cue_card = {
    "part": "Part 2",
    "topic": "Helpful Person",
    "text": "Describe a person who helped you.",
    "prep_time": 60,
    "speaking_time": 120,
    "source": "demo question bank"
}

print(cue_card)

print("Cue Card Part:")
print(cue_card["part"])

print("Cue Card Topic:")
print(cue_card["topic"])

print("Cue Card Text:")
print(cue_card["text"])

print("Cue Card Source:")
print(cue_card["source"])

prompt = f"""
Part:
{cue_card["part"]}

Topic:
{cue_card["topic"]}

Question:
{cue_card["text"]}
"""

print(prompt)