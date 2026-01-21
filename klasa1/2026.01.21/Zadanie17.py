n=int(input("Podaj liczbe: "))
wynik=1
for i in range (n,1,-1):
    wynik*=i
print(f"Śilnia liczby {n} to {wynik}")