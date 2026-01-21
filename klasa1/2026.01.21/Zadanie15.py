len=int(input("Podaj liczbe: "))
for i in range (1,len+1):
    print(f"{i}",end="")
    if i != len:
        print(", ",end="")
