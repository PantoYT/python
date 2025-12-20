import random
while True:
    rzut = "t"
    wynik = 0
    while rzut == "t":
        liczba = random.randint(1, 6)
        print("Wylosowałeś liczbę", liczba)
        wynik += liczba
        print("Suma rzutów to", wynik)
        rzut = input("Czy chcesz dalej rzucać? t/n ").lower()
    print("Koniec kolejki. Wynik:", wynik)
    if input("Czy chcesz rozpocząć nową kolejkę? t/n ").lower() != "t":
        break
