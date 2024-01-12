import time


while True:
    kolor = input("Jakiego kororu są światła? ")
    match kolor:
        case "zielone":
            print("Przechodzę przez jezdnię.")
            break
        case "czerwone":
            print("Czekam dalej")
            time.sleep(2)
        case "żółte":
            print("Zaraz przejdę...")
            time.sleep(1)
            print("Przechodzę.")
            break
        case _:
            print("Nie rozumiem.")