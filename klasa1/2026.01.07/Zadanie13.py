a=-1
while a < 0:
    try:
        a=int(input("Podaj liczbe nieujemną: "))
        if a < 0: print("Liczba musi być nieujemna")
    except:
        pass
string_a=str(a)
najw=0
najw=int(string_a[0])
for i in range (len(string_a)):
    if int(string_a[i]) > int(najw) : najw = string_a[i]
print(f"Maksymalną cyfra występująca w {a} jest {najw}")