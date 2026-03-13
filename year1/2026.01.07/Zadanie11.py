a=-1
iloczyn=1
while a < 0:
    try:
        a=int(input("Podaj liczbe nieujemną: "))
        if a < 0: print("Liczba musi być nieujemna")
    except:
        pass
string_a=str(a)
for i in range (len(string_a)):
    if int(string_a[i]) != 0: iloczyn*=int(string_a[i])
print(f"Iloczyn liczb niezerowych to {iloczyn}")