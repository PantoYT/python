a=-1
suma=0
while a < 0:
    try:
        a=int(input("Podaj liczbe nieujemną: "))
    except:
        pass
string_a=str(a)
for i in range (len(string_a)):
    suma+=int(string_a[i])
print(f"Suma cyfr liczby {a} to {suma}")