from question_list import Question_list
from questions import questions

class ChatEngine():
    def __init__(self, questions):
        self.questionlist:Question_list = questions
        
    def ask(self, query):
        q = self.questionlist.search(query)
        return q.get_answer(query)
    
    
    
engine:ChatEngine = ChatEngine(questions)