import math

def sito(max_n):
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_n)) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    wynik = [i for i in range(2, max_n + 1) if primes[i]]
    print("Liczby pierwsze:", wynik)


if __name__ == "__main__":
    max_n = int(input("Podaj max liczbę: "))
    sito(max_n)
