import random
# 초기 상태 변경
coins = random.randint(50, 80)
health = 150
max_health = 150
healing_potions = 2

weapon = {"name": "Fist", "min_dam": 20, "max_dam": 50}  # 강화된 기본 무기

accessory = None
armor = None
aqua_curse_active = False
critical_rate = 0
protection = (0, 0)

# 상점 아이템
weapons_store = {
    "1": {"name": "Battle Axe", "min_dam": 20, "max_dam": 50, "price": 70},
    "2": {"name": "Diamond Sword", "min_dam": 25, "max_dam": 65, "price": 122},
    "3": {"name": "Stick", "min_dam": 10, "max_dam": 55, "price": 26},
    "4": {"name": "Platinum Axe", "min_dam": 30, "max_dam": 87, "price": 231},
    "5": {"name": "Obsidian Spear", "min_dam": 27, "max_dam": 68, "price": 145}
}

accessory_store = {
    "6": {"name": "Aquamarine Necklace", "min_dam": 10, "max_dam": 40, "critical": 42, "curse": True, "protection": 10, "price": 357},
    "7": {"name": "Sapphire Watch", "critical": 46, "price": 156}
}

armor_store = {
    "8": {"name": "Metal Armor", "min_prot": 10, "max_prot": 30, "price": 175}
}

def choose_enemy():
    roll = random.randint(1, 100)
    if roll <= 46:
        return "Easy"
    elif roll <= 90:
        return "Medium"
    else:
        return "Hard"

def fight(enemy_type):
    global health, coins, aqua_curse_active, protection, healing_potions

    print(f"\n⚔️ You encountered a {enemy_type} enemy!")

    # ✅ 반드시 함수 안에 있어야 함!
    enemy_stats = {
        "Easy": {"hp": random.randint(30, 55), "min_dam": 3, "max_dam": 12},
        "Medium": {"hp": random.randint(50, 86), "min_dam": 12, "max_dam": 28},
        "Hard": {"hp": random.randint(55, 96), "min_dam": 20, "max_dam": 40}
    }

    enemy = enemy_stats[enemy_type]
    enemy_hp = enemy["hp"]
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

            # enemy only attacks if you attacked
            if enemy_hp > 0:
                enemy_dam = random.randint(enemy["min_dam"], enemy["max_dam"])
                block = random.randint(protection[0], protection[1]) if protection != (0, 0) else 0
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
                # enemy does not attack after healing
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

def shop():
    global coins, weapon, accessory, armor, healing_potions, critical_rate, protection, aqua_curse_active

    while True:
        print(f"\n🛒 --- Shop --- (Coins: {coins})")
        for key, item in weapons_store.items():
            print(f"{key}. {item['name']} ({item['min_dam']}-{item['max_dam']}) - {item['price']} coins")
        for key, item in accessory_store.items():
            effects = f"{item.get('critical', 0)}% crit"
            if item.get("curse"): effects += ", Aqua Curse"
            if item.get("protection"): effects += f", Protection {item['protection']}"
            print(f"{key}. {item['name']} ({effects}) - {item['price']} coins")
        for key, item in armor_store.items():
            print(f"{key}. {item['name']} (Protection {item['min_prot']}-{item['max_prot']}) - {item['price']} coins")
        print("9. Healing Potion (30 coins)")
        print("0. Exit")

        choice = input("Choose item: ")

        if choice in weapons_store and coins >= weapons_store[choice]["price"]:
            weapon = weapons_store[choice]
            coins -= weapon["price"]
            print(f"> You equipped {weapon['name']}.")

        elif choice in accessory_store and coins >= accessory_store[choice]["price"]:
            accessory = accessory_store[choice]
            coins -= accessory["price"]
            critical_rate = accessory.get("critical", 0)
            aqua_curse_active = accessory.get("curse", False)
            prot = accessory.get("protection", 0)
            protection = (protection[0] + prot, protection[1] + prot)
            print(f"> You equipped {accessory['name']}.")

        elif choice in armor_store and coins >= armor_store[choice]["price"]:
            armor = armor_store[choice]
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

# 메인 루프
print("=== Welcome to Epic Battle Game ===")
while coins < 1000:
    print("\n📊 --- Player Status ---")
    print(f"💰 Coins: {coins}")
    print(f"❤️ HP: {health}")
    print(f"🧪 Healing Potions: {healing_potions}")
    print(f"🗡 Weapon: {weapon['name']} ({weapon['min_dam']}-{weapon['max_dam']} dmg)")
    
    # Accessory 표시
    if accessory:
        extra = []
        if "critical" in accessory:
            extra.append(f"{accessory['critical']}% crit")
        if "curse" in accessory and accessory["curse"]:
            extra.append("Aqua Curse")
        if "protection" in accessory:
            extra.append(f"Protection {accessory['protection']}")
        print(f"💍 Accessory: {accessory['name']} ({', '.join(extra)})")
    else:
        print("💍 Accessory: None")
    
    # Armor 표시
    if armor:
        print(f"🛡 Armor: {armor['name']} (Protection {protection[0]}–{protection[1]})")
    else:
        print("🛡 Armor: None")

    # 행동 선택
    action = input("Choose action: (F)ight, (S)hop, (Q)uit: ").lower()

    if action == "f":
        enemy = choose_enemy()
        fight(enemy)
    elif action == "s":
        shop()
    elif action == "q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input.")

if coins >= 1000:
    print("\n🎉 You collected 1000 coins and opened the gate! YOU WIN!! 🎉")
