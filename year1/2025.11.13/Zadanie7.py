#Pobieranie koordynatów trójkąta od użytkownika
x1,y1,x2,y2,x3,y3=map(int,input("Podaj koordynaty punktu 1 w formacie x1 y1 x2 y2 x3 y3 ").split())
#Obliczanie dystanu pomiędzy puntami
dxy=((x2-x1)**2+(y2-y1)**2)**0.5
dxz=((x3-x1)**2+(y3-y1)**2)**0.5
dyz=((x3-x2)**2+(y3-y2)**2)**0.5
#Czy trójkąt
najbok = dxy
if dxz > najbok: najbok = dxz
if dyz > najbok: najbok = dyz
if najbok == dxy:
    if dxz+dyz<=najbok: print("Trójką nie powstanie")
if najbok == dxz:
    if dxy+dyz<=najbok: print("Trójką nie powstanie")
if najbok == dyz:
    if dxz+dxy<=najbok: print("Trójką nie powstanie")
#Pole i obwód
obw=dxy+dxz+dyz
pobw=obw/2
pole=(pobw*(pobw-dxy)*(pobw-dxz)*(pobw-dyz))**0.5
print(f"Dystanse między punktami to: {dxy}, {dxz}, {dyz}\nObwód tego trójkąta wynosi: {obw}\nPole tego trójkąta to: {pole}")

