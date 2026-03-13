import random as rnd
import hashlib as hl
długość=int(input("Podaj długość hasła: "))
def parametry():
    global małe,duże,cyfry,znaki,czyhash
    małe=input("Czy chcesz generować małe litery? t/f ").lower()
    duże=input("Czy chcesz generować duże litery? ").lower()
    cyfry=input("Czy chcesz generować cyfry? ").lower()
    znaki=input("Czy chcesz generować znaki specialne? ").lower()
parametry()
while małe == "f" and duże == "f" and cyfry == "f" and znaki == "f":
    print("Wszystkie parametry są wyłączone, hasło nie może być wygenerowane, podaj je ponownie")
    parametry()
pula = []
hasło = []
if małe == "t":
    pula.extend("abcdefghijklmnopqrstuvwxyz")
if duże == "t":
    pula.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if cyfry == "t":
    pula.extend("0123456789")
if znaki == "t":
    pula.extend("!@#$%^&*()-_=+[]{};:'\",.<>?/|")
hasło=[(rnd.choice(pula)) for i in range(długość)]
hasło="".join(hasło)
hash_hasło=hl.sha256(hasło.encode()).hexdigest()
print("Twoje hasło to: ",hasło)
print("Hash twojego hasła to: ",hash_hasło)
    

