działania=["+","-","*","^","/","//","%"]
p="f"
def obliczanie():
    global liczba,p
    operacje = {
        "-": lambda a, b: a - b,
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "//": lambda a, b: a // b,
        "%": lambda a, b: a % b,
        "^": lambda a, b: a ** b
    }
    liczba=int(liczba)
    działanie=input()
    if działanie == "q":
        p="nie"
    else:
        while działanie not in (działania):
            print("Podane działanie jest nie prawidłowe")
            print("Oto lista dozwolonych operacji",działania)
            print("Podaj poprawne działanie")
            działanie=input()
        liczba2=int(input())
        wynik=operacje[działanie](liczba, liczba2)
        print("=")
        print(wynik)
        liczba=wynik
        p="t"
print("Oto kalkulator, dla instrukcji wpisz 'help'")
while True:
    if p == "t":
        obliczanie()
    else:
        liczba=input()
        while liczba == "help":
            print("Najpier podaj liczbe 1")
            print("Następnie podaj działanie z ",działania)
            print("Podaj liczbe 2")
            print("Jeżeli chcesz używać wyniku w kolejnych obliczeniach podaj następne działanie i liczbe 2")
            print("Jeżeli chcesz zacząć nowe działanie wpisz 'q'")
            liczba=input("Podaj liczbe 1: \n")
        obliczanie()