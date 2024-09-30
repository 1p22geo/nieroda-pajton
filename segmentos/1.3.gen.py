import random
with open("dane1_3.txt", "w+") as f:
    for n in range(1000):
        a = random.randrange(-100, 100)
        f.write(f"{a:d}\n")
