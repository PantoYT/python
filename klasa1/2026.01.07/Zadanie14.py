import math

def inputer(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x > 1:
                return x
            else:
                print("Liczba musi być większa 1. ")
        except ValueError:
            print("Liczba musi być większa 1, podaj ją ponownie")
        

def sito(max_n):
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_n)) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    wynik = [i for i in range(2, max_n + 1) if primes[i]]
    return wynik
    
def czynnikier(liczba):
    i=0
    output=[]
    while liczba > 1:
        if liczba % primes[i] != 0:
            i+=1
        else:
            liczba//=primes[i] 
            output.append(primes[i])
            i=0
    return output

def NWD(a, b):
    # lub można użyć:
    # math.gcd(a,b);
    # ale to skrypt bez niego
    multiply = []
    
    b_copy = b.copy()
    for x in a:
        if x in b_copy:
            multiply.append(x)
            b_copy.remove(x)
            
    if not multiply:
        return 1
    
    wynik = 1
    for x in multiply:
        wynik *= x
    
    return wynik
    
def NWW(a,b,NWD):
    NWW=(a*b)//NWD
    return NWW


if __name__ == "__main__":
    a = inputer("Podaj liczbę a: ")
    b = inputer("Podaj liczbę b: ")
    
    if a > b: primes = sito(a)
    else: primes = sito(b)
    
    czynniki_a = czynnikier(a)
    czynniki_b = czynnikier(b)

    O_NWD=NWD(czynniki_a,czynniki_b)
    O_NWW=NWW(a,b,O_NWD)
    print()
    print(f"NWD to {O_NWD}")
    print(f"NWW to {O_NWW}")