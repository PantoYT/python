n=int(input("Podaj liczbe liczb: "))
wynik=1
for _ in range (n):
    x=int(input("Podaj liczbe do mnożenia: "))
    wynik*=x
print(f"Iloczyn tych liczb to {wynik}")