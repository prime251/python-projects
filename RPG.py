from random import randint, choice

# ===== Character Base Class =====
class Character:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.health = 1
        self.health_max = 1

    def do_damage(self, enemy, attack_power=1):
        damage = min(max(attack_power, 1), enemy.health)
        enemy.health -= damage
        return damage

# ===== Enemy Class =====
class Enemy(Character):
    enemy_data = {
        'Rat': {'health': 3, 'attack': 1},
        'Slime': {'health': 5, 'attack': 2},
        'Imp': {'health': 7, 'attack': 3},
        'Goblin': {'health': 8, 'attack': 3},
        'Orc Warrior': {'health': 12, 'attack': 4},
        'Skeleton Soldier': {'health': 14, 'attack': 5},
        'Orc': {'health': 15, 'attack': 5},
        'Troll': {'health': 20, 'attack': 6},
        'Skeleton': {'health': 12, 'attack': 6},
        'Zombie': {'health': 18, 'attack': 5},
        'Bomber': {'health': 20, 'attack': 7},
        'Ninja': {'health': 15, 'attack': 8},
        'Minotaur': {'health': 25, 'attack': 9},
        'Dark Knight': {'health': 28, 'attack': 10},
        'Dragon': {'health': 50, 'attack': 12},
        'Lich': {'health': 45, 'attack': 14}
    }

    def __init__(self, player, difficulty_level):
        super().__init__()
        if difficulty_level < 10:
            choices = ['Rat', 'Slime']
        elif difficulty_level < 20:
            choices = ['Imp', 'Goblin', 'Orc Warrior', 'Skeleton Soldier']
        elif difficulty_level < 30:
            choices = ['Orc', 'Troll', 'Skeleton', 'Zombie', 'Bomber', 'Ninja']
        else:
            choices = list(Enemy.enemy_data.keys())
        self.name = choice(choices)
        self.health = Enemy.enemy_data[self.name]['health']
        self.attack_power = Enemy.enemy_data[self.name]['attack']
        self.is_boss = self.name in ['Dragon', 'Lich']
        self.is_elite = self.name in ['Orc', 'Troll', 'Skeleton', 'Zombie', 'Bomber', 'Ninja', 'Minotaur', 'Dark Knight']

# ===== Player Class =====
class Player(Character):
    shop_items = {
        'sword': 30,
        'axe': 50,
        'magic_wand': 70,
        'battle_axe': 100,
        'mystic_staff': 120,
        'shield': 30,
        'armor': 50,
        'heavy_armor': 70,
        'potion': 20,
    }

    def __init__(self):
        super().__init__()
        self.state = 'normal'
        self.health = 20
        self.health_max = 20
        self.attack_power = 2
        self.inventory_items = ['wooden_sword']
        self.equipped_weapon = 'wooden_sword'
        self.equipped_armor = None
        self.codex = {}
        self.skills = []
        self.explore_count = 0
        self.quest_kill_goal = 5
        self.quest_kill_progress = 0
        self.xp = 0
        self.gold = 0

    def help(self):
        print(list(Commands.keys()))

    def status(self):
        print(f"{self.name}'s Health: {self.health}/{self.health_max}, Attack: {self.attack_power:.1f}, Gold: {self.gold}")

    def inventory(self):
        print(f"Inventory: {', '.join(self.inventory_items)}")

    def equip(self, item=None):
        if not item:
            print("Please specify an item to equip.")
            return
        if item in self.inventory_items:
            self.equipped_weapon = item
            print(f"{self.name} equipped {item}.")
        else:
            print("You don't have that item.")

    def use(self, item=None):
        if not item:
            print("Please specify an item to use.")
            return
        if item == 'potion' and 'potion' in self.inventory_items:
            self.health = min(self.health + 7, self.health_max)
            self.inventory_items.remove('potion')
            print(f"{self.name} used a potion and recovered 7 health!")
        else:
            print(f"You can't use {item} now.")

    def codex_list(self):
        print("Codex:")
        for monster, info in self.codex.items():
            print(f" - {monster}: HP {info['health']}, Attack {info['attack']}")

    def rest(self):
        print(f"{self.name} rests.")
        if randint(1, 10) <= 3:
            self.shop()
        elif randint(0, 1):
            self.spawn_enemy()
        else:
            if self.health < self.health_max:
                self.health += 1
            print(f"{self.name} feels rested.")

    def shop(self):
        print("You found a shop!")
        for item, price in Player.shop_items.items():
            print(f"{item} ({price}g)")

    def buy(self, item=None):
        if not item:
            print("Please specify what to buy.")
            return
        if item in Player.shop_items:
            price = Player.shop_items[item]
            if self.gold >= price:
                self.gold -= price
                self.inventory_items.append(item)
                print(f"Bought {item} for {price} gold!")
            else:
                print("Not enough gold.")
        else:
            print("That item is not available in the shop.")

    def spawn_enemy(self):
        self.enemy = Enemy(self, self.explore_count)
        print(f"You encounter {self.enemy.name}!")
        self.state = 'fight'
        self.codex[self.enemy.name] = {'health': self.enemy.health, 'attack': self.enemy.attack_power}

    def explore(self):
        self.explore_count += 1
        print(f"{self.name} explores...")
        event = randint(1, 10)
        if event <= 3:
            self.shop()
        elif event == 4:
            self.random_chest()
        elif event == 5:
            self.secret_room()
        else:
            self.spawn_enemy()

    def random_chest(self):
        print("You found a random chest!")
        roll = randint(1, 100)
        if roll <= 30:
            gold = randint(50, 150)
            self.gold += gold
            print(f"Found {gold} gold!")
        elif roll <= 50:
            item = choice(['sword', 'axe', 'shield', 'armor'])
            self.inventory_items.append(item)
            print(f"Found a {item}!")
        elif roll <= 80:
            print("Found a potion!")
            self.inventory_items.append('potion')
        else:
            if 'fireball' not in self.skills:
                self.skills.append('fireball')
                print("Learned new skill: Fireball!")

    def secret_room(self):
        print("You discovered a secret room!")
        self.secret_monsters = [Enemy(self, 10) for _ in range(randint(2, 3))]
        for m in self.secret_monsters:
            print(f" - {m.name} appears!")

        if self.secret_monsters:
            self.enemy = self.secret_monsters.pop(0)
            self.state = 'fight'
            print(f"You engage {self.enemy.name} in battle!")

    def attack(self):
        if self.state != 'fight':
            print("You swing at the air... No enemy.")
            return

        base_attack = self.attack_power
        damage = self.do_damage(self.enemy, attack_power=base_attack)

        if damage > 0:
            print(f"You hit {self.enemy.name} for {damage:.1f} damage!")
        else:
            print(f"{self.enemy.name} dodged your attack!")

        if self.enemy.health <= 0:
            print(f"You defeated {self.enemy.name}!")
            self.gold += 20
            self.xp += 10
            self.quest_kill_progress += 1
            self.grow_after_kill(self.enemy)

            if hasattr(self, 'secret_monsters') and self.secret_monsters:
                self.enemy = self.secret_monsters.pop(0)
                print(f"Another monster {self.enemy.name} charges at you!")
            else:
                if hasattr(self, 'secret_monsters'):
                    del self.secret_monsters
                    self.secret_room_reward()
                self.enemy = None
                self.state = 'normal'
        else:
            self.enemy_attacks()

    def grow_after_kill(self, enemy):
        self.attack_power += 0.2
        if enemy.is_boss:
            self.health_max += 3
            print(f"Defeated Boss! Max health increased by 3!")
        elif enemy.is_elite:
            self.health_max += 1
            print(f"Defeated Elite! Max health increased by 1!")

    def secret_room_reward(self):
        print("You cleared the secret room!")
        reward_gold = randint(100, 300)
        self.gold += reward_gold
        print(f"You found {reward_gold} gold in a treasure chest!")
        if randint(0, 1):
            item = choice(['battle_axe', 'mystic_staff'])
            self.inventory_items.append(item)
            print(f"You also found a rare item: {item}!")

    def enemy_attacks(self):
        damage = max(1, self.enemy.attack_power)
        self.health -= damage
        print(f"{self.enemy.name} attacks you for {damage} damage!")
        if self.health <= 0:
            print("You died. GAME OVER.")

    def escape(self):
        if self.state != 'fight':
            print("There's nothing to escape from.")
            return
        chance = randint(1, 5)
        if chance > 2:
            print(f"{self.name} escaped successfully!")
            self.state = 'normal'
            self.enemy = None
        else:
            print(f"{self.name} failed to escape!")
            self.enemy_attacks()

    def quest(self):
        print("Quest Progress:")
        print(f" - Kill {self.quest_kill_goal}: {self.quest_kill_progress}/{self.quest_kill_goal}")

# ===== 명령어 등록 =====
Commands = {
    'help': Player.help,
    'status': Player.status,
    'inventory': Player.inventory,
    'equip': Player.equip,
    'use': Player.use,
    'buy': Player.buy,
    'codex': Player.codex_list,
    'rest': Player.rest,
    'explore': Player.explore,
    'attack': Player.attack,
    'escape': Player.escape,
    'quest': Player.quest,
}

# ===== 게임 시작 =====
p = Player()
p.name = input("What is your character's name? ")
p.gender = input(f"What is {p.name}'s gender? (he or her) ")

print("\n(type 'help' to see available commands)\n")
print(f"{p.name} enters a dark cave, ready for adventure...\n")

while p.health > 0:
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                if len(args) > 1:
                    Commands[c](p, args[1])
                else:
                    Commands[c](p)
                commandFound = True
                break
        if not commandFound:
            print(f"{p.name} doesn't understand the suggestion.")
