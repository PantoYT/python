x1,y1=map(int,input("Podaj koordynaty punktu 1 (x y) ").split())
x2,y2=map(int,input("Podaj koordynaty punktu 2 (x y) ").split())
if x1 == x2 and y1 == y2:
    print("Punkty się nakrywają")
else:
    długość=((y2-y1)**2+(x2-x1)**2)**(1/2)
    print(długość)
