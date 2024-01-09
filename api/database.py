class DatabaseIndexException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            try:
                return self.data[index]
            except:
                raise DatabaseIndexException(f"data has no index: {index}")
    def len(self):
        return len(self.data)