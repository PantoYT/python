x1,y1=map(int,input("Podaj koordynaty punktu 1 (x y) ").split())
x2,y2=map(int,input("Podaj koordynaty punktu 2 (x y) ").split())

dx=x2-x1
dy=y2-y1
d=(dx**2+dy**2)**(1/2)

print("Odleglosc miedyz punktami to ",d)