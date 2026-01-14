a=int(input("Podaj liczbe a "))
b=int(input("Podaj liczbe b "))
if a==b:
    print(f"Liczby a ({a}) i b ({b}) są równe ")
elif a<b:
    print(f"Liczba a ({a}) jest mniejsza od liczby b ({b})")
else:
    print(f"Liczba b ({b}) jest mniejsza od liczby a ({a})")