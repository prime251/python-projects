# Epic Battle Game: Full Integration with Events, Monsters, Store, and Shop
import random

# Initial player status
coins = random.randint(50, 80)
health = 150
max_health = 150
healing_potions = 2

weapon = {"name": "Fist", "min_dam": 20, "max_dam": 50}
accessory = None
armor = None
critical_rate = 0
protection = (0, 0)
aqua_curse_active = False
brainrot_active = False

# Brainrot event names
brainrot_names = [
    "Tralalero Tralala", "Bombardiro Crocodilo", "Tung Tung Tung Sahur", "Lirilì Larilà",
    "Boneca Ambalabu", "Brr Brr Patapim", "Chimpanzini Bananini", "Bombombini Gusini",
    "Capuccino Assassino", "Trippi Troppi", "Frigo Camelo", "La Vaca Saturno Saturnita",
    "Ballerina Cappucina", "U Din Din Din Dun", "Trulimero Trulicina", "Girafa Celeste",
    "Bobrito Bandito", "Ta Ta Ta Sahur", "Frulli Frulla", "Brri Brri Bicus Dicus Bombicus",
    "Tric Trac Baraboom", "Cocofanto Elefanto", "Burbaloni Lulilolli", "Orangutini Ananasini"
]

# Monster categories
monsters = {
    "Easy": ["Skeleton", "Soul", "Bat", "Slime"],
    "Medium": ["Goblin", "Fire Wolf", "Zombie", "Ice Witch", "Soul Knight", "Bomber"],
    "Hard": ["Skeleton King", "Soul King", "Cave Beast", "Laser Gunner"],
    "Boss": ["Dragon", "Hydra", "Naga", "Ice Queen", "Yeti"],
    "Impossible": ["Lich", "Halbarus", "Minoshiroom", "Ur Ghast"]
}

# Gemstone mining setup
gemstone_pool = [
    {"name": "Gold", "prob": 13, "value": 31},
    {"name": "Aquamarine", "prob": 3, "value": 89},
    {"name": "Blue Diamond", "prob": 4, "value": 72},
    {"name": "Opal", "prob": 24, "value": 21},
    {"name": "Sapphire", "prob": 10, "value": 42},
    {"name": "Emerald", "prob": 16, "value": 36},
    {"name": "Ruby", "prob": 25, "value": 10},
    {"name": "Diamond", "prob": 5, "value": 56},
]

def check_for_event():
    roll = random.randint(1, 100)
    if roll <= 10:
        return "mining"
    elif roll <= 20:
        return "brainrot"
    return None

def mining_event():
    print("\n⛏️ You found a mining spot!")
    roll = random.randint(1, 100)
    cumulative = 0
    for gem in gemstone_pool:
        cumulative += gem["prob"]
        if roll <= cumulative:
            print(f"> You mined a {gem['name']} worth {gem['value']} coins!")
            return gem["value"]
    print("> You found nothing of value.")
    return 0

def brainrot_event(original_name):
    return random.choice(brainrot_names)

def choose_monster():
    roll = random.randint(1, 100)
    if roll <= 2:
        level = "Impossible"
        stats = {"hp": random.randint(70, 147), "min_dam": 50, "max_dam": 100}
    elif roll <= 10:
        level = "Boss"
        stats = {"hp": random.randint(100, 160), "min_dam": 35, "max_dam": 60}
    elif roll <= 24:
        level = "Hard"
        stats = {"hp": random.randint(55, 96), "min_dam": 20, "max_dam": 40}
    elif roll <= 70:
        level = "Medium"
        stats = {"hp": random.randint(50, 86), "min_dam": 12, "max_dam": 28}
    else:
        level = "Easy"
        stats = {"hp": random.randint(30, 55), "min_dam": 3, "max_dam": 12}
    name = random.choice(monsters[level])
    return name, stats

def fight():
    global health, coins, brainrot_active, healing_potions
    monster_name, stats = choose_monster()

    if brainrot_active:
        monster_name = brainrot_event(monster_name)
        print(f"😵 Brainrot event! Monster becomes: {monster_name}")

    print(f"\n⚔️ You encountered a {monster_name}!")
    enemy_hp = stats["hp"]
    potion_used = 0

    while enemy_hp > 0 and health > 0:
        print(f"\nYour HP: {health} | Enemy HP: {enemy_hp} | Potions: {healing_potions}")
        action = input("Choose (A)ttack, (H)eal, or (Q)uit (-30 coins): ").lower()

        if action == 'a':
            damage = random.randint(weapon["min_dam"], weapon["max_dam"])
            if accessory and "min_dam" in accessory:
                damage += random.randint(accessory["min_dam"], accessory["max_dam"])
            if random.randint(1, 100) <= critical_rate:
                crit = random.randint(10, 30)
                damage += crit
                print(f"> Critical hit! +{crit} damage")
            enemy_hp -= damage
            print(f"> You hit the enemy for {damage} damage.")

            if enemy_hp > 0:
                enemy_dam = random.randint(stats["min_dam"], stats["max_dam"])
                block = random.randint(protection[0], protection[1])
                final_dam = max(0, enemy_dam - block)
                health -= final_dam
                print(f"> Enemy hits for {final_dam} damage. (Blocked {block})")

        elif action == 'h':
            if healing_potions > 0 and potion_used < 2:
                heal = random.randint(20, 40)
                health = min(max_health, health + heal)
                healing_potions -= 1
                potion_used += 1
                print(f"> You healed {heal} HP. ({2 - potion_used} uses left)")
            elif healing_potions <= 0:
                print("> You have no healing potions.")
            else:
                print("> You can only use 2 potions per fight.")

        elif action == 'q':
            if coins >= 30:
                coins -= 30
                print("> You fled the battle and lost 30 coins.")
                return
            else:
                print("> Not enough coins to flee.")
        else:
            print("> Invalid action.")

        if aqua_curse_active and enemy_hp > 0:
            curse_dam = random.randint(5, 20)
            enemy_hp -= curse_dam
            print(f"> Aqua Curse deals {curse_dam} damage!")

    if health > 0:
        reward = random.randint(0, 30)
        coins += reward
        print(f"> You defeated the enemy and earned {reward} coins.")
    else:
        print("💀 You died... Game Over.")
        exit()

# Shop items
def weapons_store():
    return {
        "1": {"name": "Battle Axe", "min_dam": 20, "max_dam": 50, "price": 70},
        "2": {"name": "Diamond Sword", "min_dam": 25, "max_dam": 65, "price": 122},
        "3": {"name": "Stick", "min_dam": 10, "max_dam": 55, "price": 26},
        "4": {"name": "Platinum Axe", "min_dam": 30, "max_dam": 87, "price": 231},
        "5": {"name": "Obsidian Spear", "min_dam": 27, "max_dam": 68, "price": 145}
    }

def accessory_store():
    return {
        "6": {"name": "Aquamarine Necklace", "min_dam": 10, "max_dam": 40, "critical": 42, "curse": True, "protection": 10, "price": 357},
        "7": {"name": "Sapphire Watch", "critical": 46, "price": 156},
        "10": {"name": "Emerald Necklace", "critical": 80, "price": 366},
        "11": {"name": "Ruby Watch", "critical": 60, "price": 233},
        "12": {"name": "Blue Diamond Watch", "critical": 72, "price": 295},
        "13": {"name": "Golden Watch", "critical": 90, "price": 400}
    }

def armor_store():
    return {
        "8": {"name": "Metal Armor", "min_prot": 10, "max_prot": 30, "price": 175}
    }

def shop():
    global coins, weapon, accessory, armor, healing_potions, critical_rate, protection, aqua_curse_active
    weapons = weapons_store()
    accessories = accessory_store()
    armors = armor_store()

    while True:
        print(f"\n🛒 --- Shop --- (Coins: {coins})")
        for key, item in weapons.items():
            print(f"{key}. {item['name']} ({item['min_dam']}-{item['max_dam']}) - {item['price']} coins")
        for key, item in accessories.items():
            effects = f"{item.get('critical', 0)}% crit"
            if item.get("curse"): effects += ", Aqua Curse"
            if item.get("protection"): effects += f", Protection {item['protection']}"
            print(f"{key}. {item['name']} ({effects}) - {item['price']} coins")
        for key, item in armors.items():
            print(f"{key}. {item['name']} (Protection {item['min_prot']}-{item['max_prot']}) - {item['price']} coins")
        print("9. Healing Potion (30 coins)")
        print("0. Exit")

        choice = input("Choose item: ")

        if choice in weapons and coins >= weapons[choice]["price"]:
            weapon = weapons[choice]
            coins -= weapon["price"]
            print(f"> You equipped {weapon['name']}.")

        elif choice in accessories and coins >= accessories[choice]["price"]:
            accessory = accessories[choice]
            coins -= accessory["price"]
            critical_rate = accessory.get("critical", 0)
            aqua_curse_active = accessory.get("curse", False)
            prot = accessory.get("protection", 0)
            protection = (protection[0] + prot, protection[1] + prot)
            print(f"> You equipped {accessory['name']}.")

        elif choice in armors and coins >= armors[choice]["price"]:
            armor = armors[choice]
            coins -= armor["price"]
            protection = (armor["min_prot"], armor["max_prot"])
            print(f"> You equipped {armor['name']}.")

        elif choice == "9" and coins >= 30:
            healing_potions += 1
            coins -= 30
            print("> Bought 1 healing potion.")

        elif choice == "0":
            break
        else:
            print("> Invalid choice or not enough coins.")

# Main Game Loop
print("=== Welcome to Epic Battle Game ===")
while coins < 1000:
    print(f"\n💰 Coins: {coins} | ❤️ HP: {health} | 🧪 Potions: {healing_potions}")
    event = check_for_event()
    if event == "mining":
        coins += mining_event()
    elif event == "brainrot":
        brainrot_active = True
    else:
        brainrot_active = False

    action = input("Choose action: (F)ight, (S)hop, (Q)uit: ").lower()
    if action == 'f':
        fight()
    elif action == 's':
        shop()
    elif action == 'q':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input.")

if coins >= 1000:
    print("\n🎉 You collected 1000 coins and opened the gate! YOU WIN!! 🎉")
