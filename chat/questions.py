from question import Question
from question_list import Question_list
import json
from datetime import datetime

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

json_questions = data["questions"]

questions = Question_list([
    Question(forms=[
        "Która godzina",
        "Która jest godzina"
    ], getAnswer=lambda self,query:datetime.now().strftime("Jest godzina %H:%M:%S")),
    Question(forms=[
        "ile to .*"
    ], matcher="regex", getAnswer= lambda self,query:eval(query[6:].strip()))
])

for question in json_questions:
    forms = question["forms"]
    answer = question["answer"]
    questions.add(Question(forms=forms, answer=answer))
