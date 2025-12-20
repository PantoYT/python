import random as rnd
while True:
    liczba=rnd.randint(0,101)
    print("Zgadnij liczbe!")
    i=1
    while True:
        zgadnięcie=int(input())
        if liczba == zgadnięcie:
            print(f"Gratulacje, zgadłeś liczbe w {i} próbach")
            break
        elif liczba < zgadnięcie:
            print("Twoja liczba jest zbyt duża")
        else:
            print("Twoja liczba jest zbyt mała")
        i+=1