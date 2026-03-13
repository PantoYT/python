a=int(input("Podaj liczbe całkowitą z przedziału 0-9999 "))
if a >= 0 and a <= 9999:
    print(f"Liczba tysięcy to {a%10000//1000}")
    print(f"Liczba setek to {a%1000//100}")
    print(f"Liczba dzieśiątek to {a%100//10}")
    print(f"Liczba jedności to {a%10}")
else:
    print(f"Liczba {a} nie mieści się w przedziale 0-9999")