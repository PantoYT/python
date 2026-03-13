n=int(input("Podaj liczbe n "))
while n < 0:
    print(f"Liczba {n} jest mniejsza od 0 podaj ją ponownie ")
    n=int(input("Podaj liczbe n "))
a=int(input())
najw=a
najm=a
i = 0 
while i < n-1:
    a=int(input())
    if a > najw: najw = a
    if a < najm: najm = a
    i+=1
print(f"Największa liczba to {najw}, najmniejsza liczba to {najm}")
    