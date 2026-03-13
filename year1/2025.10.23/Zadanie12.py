a,b,c=map(int,input("Podaj 3 krawędzie prostopadłościanu w formacie (a b c) ").split())
#Przekątna
    # pp = przekątna podstawy do kwadratu
    # p = przekątna prostopadłościanu
    # Intsrukcja:
        # Najpierw liczymy przekątną podstawy ze wzoru pitagorasa (a²+b²=c²) -> a²+b²=pp,
        # Nie pierwiastkujemy pp ale używamy go razem z c² by zdobyć p², 
        # Potem pierwiastkujemy p² by dostać przekątną prostopadłościanu.
    # Ewentualie można użyć poprostu (a²+b²+c²)**1/2
pp=a**2+b**2
p=pp+c**2
p=p**(1/2)
#Pole całkowite i objętość
    #obj = objętość
    #polec = pole całkowite
obj=a*b*c
polec=(2*a*b)+(2*a*c)+(2*b*c)
print(f" Przekątna prostopadłościanu to {p}, \n Objętość to {obj}, \n Pole całkowite to {polec},")

