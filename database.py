class Database():
    def __init__(self):
        self.data = []
    def insert(self, obj, index=-1):
        if index == -1:
            self.data.append(obj)
            return len(self.data)
        else:
            self.data.insert(index, obj)
            return index
    def get(self, index=-1):
        if index == -1:
            return self.data
        else:
            return self.data[index]
    def len(self):
        return len(self.data)