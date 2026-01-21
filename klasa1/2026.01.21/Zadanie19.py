n=-1
while n < 1:
    try:
        n=int(input("Podaj liczbe liczb: "))
        if n < 0: print("Liczba musi być nieujemna")
    except:
        pass

wynik=1
for _ in range (n):
    x=int(input("Podaj liczbe do mnożenia: "))
    wynik*=x
print(f"Iloczyn tych liczb to {wynik}")