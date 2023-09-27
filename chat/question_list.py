from question import Question


class Question_list():
    def __init__(self, q=[]):
        self.questions = q
        self.null_question = Question([], answer="Nie rozumiem pytania")

    def add(self, question:Question):
        self.questions.append(question)
        
    def search(self, query)->Question:
        for question in self.questions:
            if question.match(query):
                return question
        return self.null_question