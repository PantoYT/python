import math

def sito(max_n):
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_n)) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    wynik = [i for i in range(2, max_n + 1) if primes[i]]
    return wynik

if __name__ == "__main__":
    max=int(input("Podaj max "))
    wynik=sito(max)
    print(wynik)
