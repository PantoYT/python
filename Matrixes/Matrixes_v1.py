#Biblioteka do działań na matrycach
import numpy
lrows = 0 
lcols = 0
lmatrix = 0
#Pobieranie matrycy od użytkownika o danym numerze
def matryca(nr):
    global lrows,lcols,lmatrix
    prozmiar = "n"
    pmatryca ="n"
    if nr == 1:
        rows = int(input(f"Podaj liczbe rzędów matrycy {nr}: "))
        cols = int(input(f"Podaj liczbe kolumn matrycy {nr}: "))
        lrows = rows
        lcols = cols
    else:
        prozmiar=input(f"Czy chcesz do matrycy numer {nr} użyć rozmiarów matrycy {nr-1} y/n? ")
        if prozmiar == "y":
            rows = lrows
            cols = lcols
        else:
            rows = int(input(f"Podaj liczbe rzędów matrycy {nr}: "))
            cols = int(input(f"Podaj liczbe kolumn matrycy {nr}: "))
            lrows = rows
            lcols = cols
    print()
    matrix = []
    if prozmiar == "y":
        pmatryca=input(f"Czy chcesz użyć wartości matrycy {nr-1} y/n? ")
        if pmatryca == "y":
            matrix = lmatrix
            return matrix
        else:
            for i in range (rows):
                row = []
                for j in range(cols):
                    row.append(int(input(f"Podaj wartości {j+1} w {i+1} rzędzie: ")))
                matrix.append(row)
                lmatrix = matrix
            return matrix
    else:
        for i in range (rows):
            row = []
            for j in range(cols):
                row.append(int(input(f"Podaj wartości {j+1} w {i+1} rzędzie: ")))
            matrix.append(row)
            lmatrix = matrix
        return matrix
def działania(A,B):
    global suma,róż,ilcz,ilr
    A = numpy.array(A)
    B = numpy.array(B)
    suma = A+B
    róż = A-B
    ilcz = A*B
    ilr = A/B
A = matryca(1)
print()
B = matryca(2)
działania(A,B)
print(f"Dla matryc a: \n{A} \ni b: \n{B} \nsuma to:\n{suma} \nróżnica to:\n{róż} \niloczyn to:\n{ilcz} \niloraz to:\n{ilr}")