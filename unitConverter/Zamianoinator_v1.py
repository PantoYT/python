#Podawanie liczby
typ = int(input("Wybierz typ liczby z 2, 10, 16 "))
while typ not in (2,10,16):
    print("Podany został niewłaściwy typ, spróbuj ponownie ")
    typ = int(input("Wybierz typ liczby z 2, 10, 16 "))
liczba = int(input("Podaj liczbe "))
#Zamiana liczb binarnych
if typ == 2:
    liczba_str = str(liczba)
    dzielnik = 1
    
    #Na dziesiętne
    wynik_dec = 0
    for i in range(len(liczba_str)):
        wynik_dec += ((liczba//dzielnik)%10)*(2**i)
        dzielnik *= 10
    print(f"Liczba binarna {liczba} w systemie dziesiętnym to {wynik_dec}")
    
    #Na heksadecymalne
    wynik_hex=""
    trans = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while (len(liczba_str))%4!=0:
        liczba_str="0"+liczba_str
    for i in range (0,len(liczba_str),4):
        grupa = liczba_str[i:i+4]
        dec = 0
        dzielnik = 1
        dec = int(grupa, 2)
        if dec >= 10:
            wynik_hex += trans[dec]
        else:
            wynik_hex += str(dec)
    print(f"Liczba binarna {liczba} w systemie heksadecymalnym to {wynik_hex}")

#Zamiana liczb dziesiętnych
elif typ == 10:
    #Na binarne
    liczba_org=liczba
    wynik_bin=""
    while liczba>0:
        if liczba%2==1:
            wynik_bin="1"+wynik_bin
        else:
            wynik_bin="0"+wynik_bin
        liczba//=2
    print(f"Liczba dziesiętna {liczba_org} w systemie binarnym: {wynik_bin}")
    #Na heksadecymalne
    wynik_hex=""
    trans = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while (len(wynik_bin))%4!=0:
        wynik_bin="0"+wynik_bin
    for i in range (0,len(wynik_bin),4):
        grupa = wynik_bin[i:i+4]
        dec = 0
        dzielnik = 1
        dec = int(grupa, 2)
        if dec >= 10:
            wynik_hex += trans[dec]
        else:
            wynik_hex += str(dec)
    print(f"Liczba dzieśiętna {liczba_org} w systemie heksadecymalnym to {wynik_hex}")
#Zamiana liczb heksadecymalnych
if typ == 16:
    #Na binarne
    wynik_bin=""
    liczba_str=str(liczba)
    for cyfra in liczba_str:
        if "0" <= cyfra <= "9":
            val = ord(cyfra) - ord("0")
        else:
            val = ord(cyfra) - ord("A")+10
        bin_cyfra = ""
        for i in range (3,-1,-1):
            if val & (1<<i):
                bin_cyfra += "1"
            else:
                bin_cyfra += "0"
        wynik_bin += bin_cyfra
    print(f"Liczba heksadecymalna {liczba} w systemie binarnym to {wynik_bin}")
    #Na dziesiętne
    wynik_dec = 0
    wynik_bin_str=str(wynik_bin)
    for i in range(len( wynik_bin_str)):
        wynik_dec += ((wynik_bin//dzielnik)%10)*(2**i)
        dzielnik *= 10
    print(f"Liczba heksadecymalna {wynik_bin} w systemie dziesiętnym to {wynik_dec}")
    
    
        