len=int(input("Podaj liczbe: "))
for i in range (1,len+1):
    for j in range (1,i+1):
        print(f"{j}",end="")
        if j != i:
            print(", ",end="")
    print("\n")
