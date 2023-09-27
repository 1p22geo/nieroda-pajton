import re


def prep(x: str):
    return x.lower().replace("ą", "a").replace("ę", "e").replace("ó", "o").replace("ż",
                                                                                   "z").replace("ń", "n").replace("ć", "c").replace("ń", "n").strip().rstrip('?! ')


class Question():
    def __init__(self, forms=None, matcher=None, answer=None, getAnswer=None):
        self.forms = forms
        self.matcher = matcher
        if answer:
            self.get_answer = lambda query: answer
        elif getAnswer:
            self.get_answer = lambda query:getAnswer(self,query)
        else:
            self.get_answer = lambda query: "Oto jest pytanie..."

    def match(self, query):
        if callable(self.matcher):
            return self.matcher(self, query)
        match self.matcher:
            case "regex":
                for form in self.forms:
                    if re.search(form, prep(query)):
                        return True
                return False
            case _:
                for form in self.forms:
                    if prep(form) == prep(query):
                        return True
                return False
