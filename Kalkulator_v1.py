def działanie():
    global liczba
    operacja=input("Wybierz operacje z - + * / // % ^ ")
    while operacja not in ("-","+","*","/","//","%","^"):
        print("Nieprawidłowa operacja")
        operacja=input("Wybierz operacje z (- + * / // % ^) ")
    liczba2=int(input("Podaj liczbe 2 "))
    if operacja == "-":
        wynik=liczba-liczba2
    elif operacja  == "+":
        wynik=liczba+liczba2
    elif operacja == "*":
        wynik=liczba*liczba2
    elif operacja == "/":
        wynik=liczba/liczba2
    elif operacja  == "//":
        wynik=liczba//liczba2
    elif operacja == "%":
        wynik=liczba%liczba2
    elif operacja == "**":
        wynik=liczba^liczba2
    print(f"{liczba} {operacja} {liczba2} = {wynik}")
    liczba=wynik
while True:
    liczba=int(input("Podaj liczbe 1 "))
    działanie()
    nowe=str(input("Rozpocząć nowe działanie? y/n "))
    while nowe == "n":
        działanie()
        nowe=str(input("Zakończyć działanie? y/n "))
        
    
    