import random

CARDS = [
    {"name": "Fire Lizard", "attack": 5, "defense": 4},
    {"name": "Stone Golem", "attack": 3, "defense": 6},
    {"name": "Wind Hawk", "attack": 6, "defense": 3},
    {"name": "Water Spirit", "attack": 4, "defense": 5},
    {"name": "Thunder Wolf", "attack": 7, "defense": 2},
]

def create_card(base):
    hp = base["defense"] * 5
    return {
        "name": base["name"],
        "attack": base["attack"],
        "defense": base["defense"],
        "hp": hp,
        "max_hp": hp
    }

def show(card):
    return f"{card['name']} (ATK {card['attack']} / DEF {card['defense']} / HP {card['hp']})"

def battle(player, enemy):
    print("\n⚔️ Battle Start!")
    print("You:", show(player))
    print("Enemy:", show(enemy))

    turn = 1
    heal_used = 0
    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"\nTurn {turn}")
        print("1. Attack  2. Heal (Used: {}/2)".format(heal_used))
        choice = input("> ").strip()

        if choice == "1":
            enemy["hp"] -= player["attack"]
            print(f"You attack for {player['attack']} damage!")
        elif choice == "2":
            if heal_used < 2:
                player["hp"] = min(player["max_hp"], player["hp"] + 5)
                heal_used += 1
                print("💚 You heal 5 HP!")
            else:
                print("❌ No heals left!")

        if enemy["hp"] > 0:
            player["hp"] -= enemy["attack"]
            print(f"Enemy attacks for {enemy['attack']} damage!")

        print(f"Your HP: {player['hp']} / Enemy HP: {enemy['hp']}")
        turn += 1

    if player["hp"] > 0:
        print("🎉 You Win!")
    else:
        print("💀 You Lose.")

# Choose 1 card
print("Choose your card:")
for idx, c in enumerate(CARDS):
    print(f"{idx+1}. {c['name']} (ATK {c['attack']} / DEF {c['defense']})")
while True:
    pick = input("> ")
    if pick.isdigit() and 1 <= int(pick) <= len(CARDS):
        player = create_card(CARDS[int(pick)-1])
        break

enemy = create_card(random.choice(CARDS))
battle(player, enemy)
