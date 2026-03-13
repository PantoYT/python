while True:
    bok=int(input("Podaj bok kwadratu "))
    if bok > 0:
        obw=4*bok
        pole=bok**2
        print(f"Dla kwadratu o boku {bok}, pole to {pole}, a obw to {obw}")
    else:
        print("Podane dane są niepoprawne")