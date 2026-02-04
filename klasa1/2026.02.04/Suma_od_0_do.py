def sumer(max):
    suma=0
    i=0
    while i <= max:
        suma+=i
        i+=1
    return suma

max=int(input("Podaj max liczbe: "))
print(f"Suma liczb od 0 do {max} to {sumer(max)}")