a=-1
while a < 0:
    try:
        a=int(input("Podaj liczbe nieujemną: "))
    except:
        pass
string_a=str(a)
len_a=len(string_a)
print(f"Długosc liczby to {len_a}")
