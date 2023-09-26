from question import Question


class Question_list():
    def __init__(self, q=[]):
        self.questions = q

    def add(self, question:Question):
        self.questions.append(question)
        
    def search(self, query):
        for question in self.questions:
            if question.match(query):
                return question