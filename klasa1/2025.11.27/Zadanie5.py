suma = 0
i = 0
while suma < 50:
    liczba = float(input("Podaj liczbe: "))
    suma+=liczba
    i+=1
print(f"Suma: {suma}, Ilość: {i}, Średnia: {suma/i}")