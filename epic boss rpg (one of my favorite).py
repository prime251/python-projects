# === RPG GAME: COMPLETE VERSION ===
import random

# --- Player Setup ---
player = {
    "name": "Hero",
    "level": 1,
    "xp": 0.0,
    "hp": 100,
    "max_hp": 100,
    "coins": 50,
    "weapon": "Fist",
    "weapon_damage": 5,
    "inventory": {"Potion": 2},
    "artifacts": 0,
    "impossible_beaten": set()
}

gun_shop_items = {
    "Pistol": {"damage": 12, "price": 50},
    "Flare Gun": {"damage": 18, "price": 60},
    "Assault Rifle": {"damage": 28, "price": 100},
    "Bow": {"damage": 30, "price": 420, "crit_chance": 0.15, "crit_damage": 120},
    "Revolver": {"damage": 40, "price": 230},
    "Shotgun": {"damage": 47, "price": 210},
    "Grenade": {"damage": 50, "price": 100, "effect": "aoe"},
    "Crossbow": {"damage": 50, "price": 270},
    "Uzi": {"damage": 59, "price": 95},
    "Exogun": {"damage": 65, "price": 210},
    "Minigun": {"damage": 68, "price": 250},
    "Sniper": {"damage": 70, "price": 415, "headshot_chance": 0.10, "headshot_damage": 150},
    "Flame Thrower": {"damage": 75, "price": 340, "effect": "burn"},
    "RPG": {"damage": 84, "price": 325},
    "Burst Rifle": {"damage": 85, "price": 320},
    "Gunblade": {"damage": 90, "price": 405}
}

# --- Experience Values ---
xp_table = {
    "Easy": 0.1,
    "Medium": 0.8,
    "Hard": 2.2,
    "Boss": 7.9,
    "Impossible": 15.7,
    "Final Boss": 100.0
}

# --- Coin Rewards ---
coin_table = {
    "Easy": 5,
    "Medium": 15,
    "Hard": 30,
    "Boss": 55,
    "Impossible": 100,
    "Final Boss": 1000
}

# --- Level Up Logic ---
def level_up():
    while player["xp"] >= player["level"]:
        player["xp"] -= player["level"]
        player["level"] += 1
        player["weapon_damage"] += 1
        print(f"⭐ You leveled up! Now level {player['level']}. Weapon damage +1.")

# --- Battle System ---
def battle(enemy):
    print(f"⚔️ A wild {enemy['name']} appears! ({enemy['hp']} HP)")

    while enemy["hp"] > 0 and player["hp"] > 0:
        input("Press Enter to attack...")
        damage = player["weapon_damage"]
        enemy["hp"] -= damage
        print(f"You hit the {enemy['name']} for {damage} damage. Remaining HP: {max(enemy['hp'], 0)}")

        if enemy["hp"] <= 0:
            print(f"✅ You defeated the {enemy['name']}!")
            reward = coin_table.get(enemy["difficulty"], enemy["coin"])
            player["coins"] += reward
            print(f"💰 You earned {reward} coins.")
            if random.random() < enemy["artifact_rate"]:
                player["artifacts"] += 1
                print("🗿 You found an ancient artifact!")
            handle_post_battle_logic(enemy)
            break

        enemy_damage = random.randint(*enemy["attack"])
        player["hp"] -= enemy_damage
        print(f"💢 The {enemy['name']} hits you for {enemy_damage} damage. Your HP: {max(player['hp'], 0)}")

        if player["hp"] <= 0:
            print("💀 You died...")
            break

# --- Enemy Generator ---
def show_shop():
    print("\n🏪 Welcome to the Weapon Shop!")
    for name, info in gun_shop_items.items():
        desc = f"{name}: {info['damage']} dmg - ${info['price']}"
        if "crit_chance" in info:
            desc += f" | Crit: {int(info['crit_chance']*100)}% for {info['crit_damage']} dmg"
        if "headshot_chance" in info:
            desc += f" | Headshot: {int(info['headshot_chance']*100)}% for {info['headshot_damage']} dmg"
        if info.get("effect") == "aoe":
            desc += " | Effect: Area Damage (1 use)"
        if info.get("effect") == "burn":
            desc += " | Effect: Burn (15 dmg for 3 turns)"
        print(desc)

    choice = input("\nWhich weapon would you like to buy? (or type 'exit')\n> ")
    if choice in gun_shop_items:
        item = gun_shop_items[choice]
        if player["coins"] >= item["price"]:
            player["coins"] -= item["price"]
            player["weapon"] = choice
            player["weapon_damage"] = item["damage"]
            print(f"✅ You bought the {choice}!")
        else:
            print("❌ Not enough coins!")
    elif choice.lower() != "exit":
        print("❓ Weapon not found.")

def explore_area():
    print("\n🌍 Where would you like to go?")
    for area in area_difficulties:
        print(f"- {area}")
    choice = input("\n> ")
    if choice in area_difficulties:
        difficulty = area_difficulties[choice]
        if isinstance(difficulty, tuple):
            battle(generate_enemy(*difficulty))
        else:
            battle(generate_enemy(difficulty))
    else:
        print("❌ Unknown area.")

def main_menu():
    print("🎮 Welcome to the RPG World!")
    while True:
        print("\n🏘️ You're in the Town.\nWhat do you want to do?")
        print("1. 🛒 Visit Weapon Shop")
        print("2. 🗺️ Explore Area")
        print("3. 🧾 View Status")
        print("4. ❌ Exit Game")
        choice = input("> ")

        if choice == "1":
            show_shop()
        elif choice == "2":
            explore_area()
        elif choice == "3":
            print(f"\n{name}'s Status:\nLevel: {player['level']}  XP: {player['xp']:.1f}")
            print(f"HP: {player['hp']}/{player['max_hp']}  Coins: {player['coins']}")
            print(f"Weapon: {player['weapon']} ({player['weapon_damage']} dmg)")
            print(f"Artifacts: {player['artifacts']} | Impossible Bosses Defeated: {len(player['impossible_beaten'])}/4")
        elif choice == "4":
            print("👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid choice.")

def generate_enemy(difficulty="Medium", specific_name=None):
    MONSTERS = {
        "Easy": ["Skeleton", "Soul", "Bat", "Slime"],
        "Medium": ["Goblin", "Fire Wolf", "Zombie", "Ice Witch", "Soul Knight", "Bomber"],
        "Hard": ["Skeleton King", "Soul King", "Cave Beast", "Laser Gunner"],
        "Boss": ["Dragon", "Hydra", "Naga", "Ice Queen", "Yeti"],
        "Impossible": ["Lich", "Halbarus", "Minoshiroom", "Ur Ghast"]
    }
    base_stats = {
        "Easy": {"hp": (30, 50), "atk": (5, 10), "coin": 5, "artifact": 0.02},
        "Medium": {"hp": (60, 90), "atk": (10, 20), "coin": 10, "artifact": 0.03},
        "Hard": {"hp": (100, 130), "atk": (15, 30), "coin": 15, "artifact": 0.10},
        "Boss": {"hp": (150, 200), "atk": (20, 35), "coin": 20, "artifact": 0.30},
        "Impossible": {"hp": (200, 300), "atk": (30, 50), "coin": 25, "artifact": 0.80},
        "Final Boss": {"hp": (250, 250), "atk": (25, 50), "coin": 50, "artifact": 1.0}
    }
    name = specific_name if specific_name else random.choice(MONSTERS[difficulty])
    stat = base_stats[difficulty]
    return {
        "name": name,
        "hp": random.randint(*stat["hp"]),
        "attack": stat["atk"],
        "coin": stat["coin"],
        "artifact_rate": stat["artifact"],
        "difficulty": difficulty
    }

# --- Area Definitions ---
area_difficulties = {
    "Forest": "Easy",
    "Cave": "Medium",
    "Volcano": "Hard",
    "Underground Dungeon": "Boss",
    "Water Tower": ("Impossible", "Minoshiroom"),
    "Nether Tower": ("Impossible", "Ur Ghast"),
    "Wind Tower": ("Impossible", "Lich"),
    "Night Tower": ("Impossible", "Halbarus")
}

# --- Post Battle ---
def handle_post_battle_logic(enemy):
    player["xp"] += xp_table.get(enemy["difficulty"], 0)
    level_up()

    if enemy['name'] in ["Lich", "Halbarus", "Minoshiroom", "Ur Ghast"]:
        player['impossible_beaten'].add(enemy['name'])
        if len(player['impossible_beaten']) == 4:
            print("🗝️ All Impossible bosses defeated. The gate to the Castle is now open!")

    if enemy['name'] == "Blood Knight":
        if player['artifacts'] >= 3:
            print("👑 You restored the city using 3 artifacts. True ending unlocked!")
        else:
            print("🪦 You defeated the Blood Knight, but the city remains cursed...")
main_menu()
