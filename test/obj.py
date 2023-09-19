class Car():
    def __init__(self, number:int):
        self.__number = number
    def getNumber(self):
        return self.__number
    def __str__(self):
        return f"A car of number {self.__number}"

f = Car(123456)
print(f.getNumber())
try:
    f.__number = 2
except:
    pass
print(f)