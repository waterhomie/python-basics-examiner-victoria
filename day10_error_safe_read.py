import json


def load_records_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            records = json.load(file)
        return records
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("JSON format is broken.")
        return []


records = load_records_safely("practice_records.json")

if not records:
    print("No practice records yet.")
else:
    for record in records:
        print(record["question"])
        print(record["score"])