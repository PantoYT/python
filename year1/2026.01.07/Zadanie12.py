a=-1
str_a=""

while a < 0:
    try:
        a=int(input("Podaj liczbe nieujemną: "))
        if a < 0: print("Liczba musi być nieujemna")
    except:
        pass
    
list_a=list(map(int, str(a)))
leng=len(list_a)
temp=""

for i in range (leng//2):
    temp=list_a[i]
    list_a[i]=list_a[leng-i-1]
    list_a[leng-i-1]=temp
for i in range (leng):
    str_a+=str(list_a[i])
    
print(f"Lustrzane odbicje liczby {a} to {str_a}")

