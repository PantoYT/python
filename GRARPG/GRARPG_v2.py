import random

lvl = 1
maxhp = 100
hp = maxhp
strength = 5
agility = 30

inventory = {
    "weapon": None,
    "armour": None,
}

items = {
    "training_sord": {"atk_mul": 1.1},
    "sturdy_sword": {"atk_mul": 1.25},
    "sharpened_sword": {"atk_mul": 1.5},
    "ranger_armour": {"hp_mul": 1.05, "agi_mul": 1.8},
    "heavy_armour": {"hp_mul": 1.5, "agi_mul": 0.6},
}

enemies = [
    {"name": "Wolf", "hp": 20, "strength": 10, "agility": 10},
    {"name": "Slime", "hp": 5, "strength": 5, "agility": 3},
    {"name": "Zombie", "hp": 25, "strength": 10, "agility": 5},
    {"name": "Skeleton", "hp": 15, "strength": 7, "agility": 7},
    {"name": "Orc", "hp": 35, "strength": 15, "agility": 0},
]

def apply_equipment():
    global maxhp, strength, agility, hp, lvl

    base_hp = 100
    base_strength = 5
    base_agility = 30

    hp_mul = 1.0
    agi_mul = 1.0
    atk_mul = 1.0

    if inventory["armour"] is not None:
        armour = inventory["armour"]
        hp_mul *= items[armour]["hp_mul"]
        agi_mul *= items[armour]["agi_mul"]

    if inventory["weapon"] is not None:
        weapon = inventory["weapon"]
        atk_mul *= items[weapon]["atk_mul"]

    strength = base_strength * atk_mul
    agility = base_agility * agi_mul

    maxhp = base_hp * hp_mul * (1.05 ** (lvl - 1))

    if hp > maxhp:
        hp = maxhp

def lvlup():
    global lvl, hp

    lvl += 1
    print("Awansowałeś na poziom", lvl)

    apply_equipment()
    hp = maxhp

def spawn_random():
    return dict(random.choice(enemies))

def choose_weapon():
    weapons = [name for name, stats in items.items() if "atk_mul" in stats]

    print("Wybierz broń:")
    for i, w in enumerate(weapons, start=1):
        print(f"{i}. {w} ({items[w]['atk_mul']})")

    choice = int(input("Twój wybór: ")) - 1

    if 0 <= choice < len(weapons):
        inventory["weapon"] = weapons[choice]
        print("Wybrano broń:", weapons[choice])
    else:
        print("Niepoprawny wybór.")

def choose_armour():
    armour = [name for name, stats in items.items() if "hp_mul" in stats]

    print("Wybierz zbroję:")
    for i, a in enumerate(armour, start=1):
        print(f"{i}. {a} ({items[a]['hp_mul']}, {items[a]['agi_mul']})")

    choice = int(input("Twój wybór: ")) - 1

    if 0 <= choice < len(armour):
        inventory["armour"] = armour[choice]
        print("Wybrano zbroję:", armour[choice])
    else:
        print("Niepoprawny wybór.")

def choose_enemy(enemy_list):
    print("Wybierz przeciwnika:")

    for i, enemy in enumerate(enemy_list, start=1):
        print(f"{i}. {enemy['name']} (HP: {enemy['hp']})")

    while True:
        try:
            choice = int(input("Numer: ")) - 1
            if 0 <= choice < len(enemy_list):
                return enemy_list[choice]
            print("Niepoprawny numer.")
        except:
            print("Podaj liczbę.")

choose_weapon()
choose_armour()
apply_equipment()

while True:

    enemy_amount = random.randint(1, lvl + 1)
    enemy_list = []

    for i in range(enemy_amount):
        e = spawn_random()
        e["id"] = i
        enemy_list.append(e)

    print("Rozpoczyna się walka.")
    print("Liczba przeciwników:", enemy_amount)

    runda = 1

    while True:

        print(f"\n--- Runda {runda} ---")

        target = choose_enemy(enemy_list)

        if random.randint(0, 100) < target["agility"]:
            print(target["name"], "unika Twojego ataku.")
        else:
            dmg = strength * (1 + random.uniform(-0.1, 0.1))
            target["hp"] -= dmg
            print(f"Zadajesz {dmg:.1f} obrażeń.")

            if target["hp"] <= 0:
                print(target["name"], "został pokonany.")
                enemy_list.remove(target)

        if len(enemy_list) == 0:
            print("Wszyscy przeciwnicy pokonani.")
            lvlup()
            apply_equipment()
            break

        for enemy in enemy_list:

            print(enemy["name"], "atakuje.")

            if random.randint(0, 100) < agility:
                print("Unikasz ataku.")
                continue

            dmg_e = enemy["strength"] * (1 + random.uniform(-0.1, 0.1))
            hp -= dmg_e

            print(f"Otrzymujesz {dmg_e:.1f} obrażeń. HP: {hp:.1f}")

            if hp <= 0:
                print("Zostałeś pokonany.")
                exit()

        runda += 1
