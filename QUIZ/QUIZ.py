import random as rand
# pytanie / a / b / c / d / odpowiedź
import random as rand

pytania = [
    {
        "pytanie": "Czy ziemia jest płaska?",
        "odpowiedzi": {
            "A": "Tak",
            "B": "Może",
            "C": "Prawdopodobnie",
            "D": "Nie"
        },
        "poprawna": "D"
    },
    {
        "pytanie": "Ile to 10 + 9?",
        "odpowiedzi": {
            "A": "21",
            "B": "19",
            "C": "1",
            "D": "109"
        },
        "poprawna": "B"
    },
    {
        "pytanie": "Co jest lepsze: koty czy psy?",
        "odpowiedzi": {
            "A": "koty",
            "B": "psy",
            "C": "oba typy zwierząt są dobre",
            "D": "nie lubię zwierząt"
        },
        "poprawna": "A"
    }
]

punkty = 0
while True:
    pytanie = rand.choice(pytania)
    print("\n" + pytanie["pytanie"])
    for litera, odp in pytanie["odpowiedzi"].items():
        print(f"{litera}: {odp}")
    proby = 0
    maks_proby = 2
    while proby < maks_proby:
        odpowiedz = input("\nTwoja odpowiedź (A/B/C/D): ").strip().upper()
        if odpowiedz == pytanie["poprawna"]:
            print("Dobrze!")
            punkty += 100
            break
        else:
            proby += 1
            if proby < maks_proby:
                print("Źle, spróbuj ponownie!")
            else:
                print(f"Zła odpowiedź! Poprawna to: {pytanie['poprawna']} - {pytanie['odpowiedzi'][pytanie['poprawna']]}")
    
    print(f"\nTwój wynik: {punkty} punkt(ów)")