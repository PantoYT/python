import random as rand
word_list = ["kot","pies","ryba","ptak","matematyka","programowanie","fizyka","polski","angielski","klawiatura","chlor","azbest","arbuz"]
state = {"4":"('_')","3":"(+_+)","2":"(>_<)","1":"(@_@)","0":"(#_#)"}

def get_letter(word):
    print("Podaj litere lub zgaduj słowo")
    while True:
        try:
            letter=str(input())
            if letter == word:
                print("Wygrałeś!")
            else:
                if len(letter)==1 and letter.isalpha():
                    return letter
                else:
                    print("Nieprawidłowo!")
        except:
            ("Podaj litere")
while True:
    word = rand.choice(word_list)
    blank=["_"]*len(word)
    lives = 4
    print("Słowo:", " ".join(blank))
    while lives >= 0:
        print("Pozsotałe życia:",lives,state[str(lives)])
        letter = get_letter(word)
        if letter in word:
            for i, ch in enumerate(word):
                if ch == letter:
                    blank[i] = letter
        else:
            lives -= 1
        print("Słowo:", " ".join(blank))
        if "_" not in blank:
            print("Wygrałeś\n")
            break
    if lives < 0:
        print("Przegrałeś, słowem było ",word,"\n")
        break