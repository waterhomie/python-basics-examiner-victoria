question_bank = [
    {
        "part": "Part 1",
        "topic": "Hometown",
        "text": "Where is your hometown?"
    },
    {
        "part": "Part 1",
        "topic": "Study",
        "text": "Do you prefer studying alone or with others?"
    },
    {
        "part": "Part 2",
        "topic": "City",
        "text": "Describe a city you want to visit."
    }
]

print("Part 1 Questions:")

part1_count = 0

for item in question_bank:
    if item["part"] == "Part 1":
        part1_count = part1_count + 1
        print(f"Question {part1_count}:")
        print(item["text"])