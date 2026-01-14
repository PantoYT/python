godzina = int(input("Podaj godzine "))
minuta = int(input("Podaj minute "))
if godzina >= 7 and minuta > 45 or godzina <= 11 and minuta < 30:
    print("Dostaniesz jedzenie")
else:
    print("Umrzesz z głodu")