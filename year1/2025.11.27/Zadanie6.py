i = int(input("Podaj liczbe "))
while True:
    if i<0 or i-5>=100:
        print(f"Liczba {i} nie jest w przedziale <0,100)\nPodaj liczbe i ponownie")
        i = int(input("Podaj liczbe "))
    else:
        print(f"Liczba {i} jest w przedziale <0,100)")
        break
