
def prep(x):
    return x.lower().replace("ą", "a").replace("ę", "e").replace("ó", "o").replace("ż", "z").replace("ń", "n").replace("ć", "c").replace("ń", "n")

class Question():
    def __init__(self, forms, answer=None, getAnswer=None):
        self.forms = forms
        if answer:
            self.get_answer = lambda :answer
        elif getAnswer:
            self.get_answer = getAnswer
        else:
            self.get_answer = lambda :"Oto jest pytanie..."
    
    def match(self, query):
        for form in self.forms:
            if prep(form) == prep(query):
                return True
        return False