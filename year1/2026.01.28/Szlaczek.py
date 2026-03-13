def szlaczek(c,n):
    return(f"\n {c*n} \n")

if __name__ == "__main__":
    c=str(input("Podaj znak: "))
    n=int(input("Podaj ilość: "))
    for _ in range (3):
        print(szlaczek(c,n))