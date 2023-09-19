a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))

while a != b:
    if a > b:
        a-=b
    else:
        b-=a

print(f"Wynik to {a}")