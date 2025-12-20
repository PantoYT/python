import random
while True:
    ite=1
    lastdeco=0
    lastchain=0
    rows=int(input("Podaj wysokosc choinki: "))
    while rows < 5:
        print("Rozmiar choinki jest za mały, choinka może nie być poprawnie utworzona, zalecane jest podanie rozmiaru większego niz 5")
        print("Kontynuować? y/n")
        czyroz=input()
        if czyroz == "y":
            break
        else:
            rows=int(input("Podaj wysokosc choinki: "))
    blanks=rows-1
    stars=1
    for _ in range (rows):
        if ite==1:
            print(" " * blanks + "\033[1;33m@\x1B[0m")
            ite+=1
            stars+=2
            blanks-=1
        else:
            print(" " * blanks,end="")
            if lastchain > random.randint(1,10):
                print("\033[1;35m#\x1B[0m" * stars,end="")
                lastdeco=0
                lastchain=0
            else:
                for _ in range (stars):
                        if lastdeco == 1:
                            print("\033[0;32m*\x1B[0m",end="")
                            lastdeco=0
                        else:
                            ifdeco=random.randrange(0,100)
                            if ifdeco>20:
                                print("\033[0;32m*\x1B[0m",end="")
                                lastdeco=0
                            else:
                                deco=random.randint(0,2)
                                if deco == 0: print("\033[1;36mo\x1B[0m",end="")
                                elif deco == 1: print("\033[0;31m%\x1B[0m",end="")
                                elif deco == 2: print("\033[0;35m&\x1B[0m",end="")
                                lastdeco=1
            print()
            stars+=2
            blanks-=1
            lastchain+=1
    stemsize=1
    stemsizer=rows
    while stemsizer>5:
        stemsize+=1
        stemsizer-=5
    stem=rows-(stemsize-1)//2-2
    for _ in range (stemsize):    
        print(" " * stem + "\033[0;33m{\x1B[0m" + "\033[0;33m|\x1B[0m" * stemsize + "\033[0;33m}\x1B[0m")
    floorlen=stars-2
    print("\033[0;30m#\x1B[0m"*floorlen)
