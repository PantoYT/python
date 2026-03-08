import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ============ TXT ============

print("=== Czytanie TXT ===")

print("Cały plik naraz:")
with open('dane.txt', 'r', encoding='utf-8') as f:
    zawartosc = f.read()
print(zawartosc)

print("Linia po linii:")
with open('dane.txt', 'r', encoding='utf-8') as f:
    for linia in f:
        print(linia.strip())

print("Lista linii:")
with open('dane.txt', 'r', encoding='utf-8') as f:
    linie = f.readlines()
print(linie)

print("\n=== Pisanie TXT ===")

print("Nadpisuje plik:")
with open('wynik.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')

print("Dopisuje do istniejącego:")
with open('wynik.txt', 'a', encoding='utf-8') as f:
    f.write('Nowa linia\n')

print("\n=== Schemat maturalny ===")

with open('dane.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    dane = []
    for _ in range(n):
        dane.append(int(f.readline().strip()))

wynik = sum(dane)
print(f"Suma: {wynik}")

with open('wynik.txt', 'w', encoding='utf-8') as f:
    f.write(str(wynik) + '\n')

# ============ JSON ============

print("\n=== Czytanie JSON ===")

with open('dane.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Klasa: {data['klasa']}")
print(f"Pierwszy uczeń: {data['uczniowie'][0]['imie']}")

for uczen in data['uczniowie']:
    srednia = sum(uczen['oceny']) / len(uczen['oceny'])
    print(f"{uczen['imie']} {uczen['nazwisko']}: {srednia:.2f}")

print("\n=== Pisanie JSON ===")

with open('wynik.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Zapisano wynik.json")