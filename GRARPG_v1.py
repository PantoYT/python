import random as rand
# Statystyki gracza
hp = 100
strength = 5
agility = 30
# Statystyki przeciwnika
hp_e = 500
strength_e = 40
agility_e = 90
runda = 1
#To do, dodać system inverntory, np. miecze i armor które mnożą twoje Statystyki
print("Walka rozpoczęta!\n")
while hp > 0 and hp_e > 0:
    print(f"--- Runda {runda} ---")
    # Tura gracza
    if rand.randint(0, 100) < agility_e:
        print("Przeciwnik unika ataku!")
    else:
        mnoznik = 1 + (rand.randint(-10, 10) / 100)
        obrazenia = strength * mnoznik
        hp_e -= obrazenia
        print(f"Trafiasz za {obrazenia:.1f} dmg (pozostałe HP wroga: {hp_e:.1f})")
    if hp_e <= 0:
        print("\nPrzeciwnik został pokonany!")
        break
    # Tura przeciwnika
    if rand.randint(0, 100) < agility:
        print(" Udało ci się uniknąć ataku!")
    else:
        mnoznik = 1 + (rand.randint(-10, 10) / 100)
        obrazenia = strength_e * mnoznik
        hp -= obrazenia
        print(f"Wróg trafia za {obrazenia:.1f} dmg (twoje HP: {hp:.1f})")
    if hp <= 0:
        print("\nPrzegrałeś walkę...")
        break
    runda += 1
    print()
print("\n--- Koniec walki ---")
