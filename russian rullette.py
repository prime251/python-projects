import random

MAX_HP = 5
START_COINS = 20

weapons = {
    "Revolver": {"price": 0, "damage": 1, "hit_chance": 0.5},
    "Shotgun": {"price": 100, "damage": 1, "hit_chance": 0.6},
    "Sniper": {"price": 250, "damage": 1, "hit_chance": 0.7},
    "Hand Gun": {"price": 70, "damage": 1, "hit_chance": 0.55},
    "Railgun": {"price": 200, "damage": 1, "hit_chance": 0.65},
    "Energy Rifle": {"price": 300, "damage": 1, "hit_chance": 0.8},
}

items = {
    "Golden Watch": {"price": 100, "desc": "Block 1 hit (even if it misses)"},
    "Double Damage": {"price": 150, "desc": "Double your damage"},
    "100% Hit": {"price": 180, "desc": "Guarantee next hit"},
    "Heal Pack": {"price": 120, "desc": "Heal 2 HP"},
}

class Player:
    def __init__(self, name, is_computer=False):
        starting_items = random.sample(list(items.keys()), 2) if not is_computer else []
        self.name = name
        self.hp = MAX_HP
        self.coins = START_COINS if not is_computer else 999
        self.weapon = None
        self.items = starting_items
        self.double_damage_count = 0
        self.use_100_hit = False
        self.golden_watch = False
        self.is_computer = is_computer
        self.used_items = 0

    def choose_weapon(self):
        if self.weapon:
            return  # already selected
        if self.is_computer:
            affordable = [w for w in weapons if weapons[w]["price"] <= self.coins]
            self.weapon = sorted(affordable, key=lambda x: weapons[x]["hit_chance"], reverse=True)[0]
        else:
            print("\n무기 선택 (게임 중 1회만 선택 가능):")
            for i, w in enumerate(weapons):
                data = weapons[w]
                print(f"{i+1}. {w} - 가격: {data['price']}코인, 명중률: {int(data['hit_chance']*100)}%, 데미지: {data['damage']}")
            while True:
                try:
                    choice = int(input("무기 번호 선택: ")) - 1
                    selected = list(weapons.keys())[choice]
                    if weapons[selected]["price"] > self.coins:
                        print("코인이 부족합니다.")
                    else:
                        self.weapon = selected
                        break
                except:
                    print("잘못된 입력입니다.")

    def choose_items(self):
        if self.is_computer:
            possible = ["Double Damage", "100% Hit"]
            while self.used_items < 2 and random.random() < 0.5:
                item = random.choice(possible)
                if item == "Double Damage":
                    self.double_damage_count += 1
                elif item == "100% Hit":
                    self.use_100_hit = True
                self.used_items += 1
        else:
            print("\n아이템 사용:")
            print(f"인벤토리: {self.items}")
            print("아이템을 여러 개 조합해 사용할 수 있습니다. 사용하고 싶은 아이템 번호를 쉼표로 구분해 입력하세요 (예: 1,3):")
            print("1. Golden Watch    2. Double Damage    3. 100% Hit    4. Heal Pack    5. 안 씀")
            choices = input("선택: ").split(',')
            for choice in choices:
                choice = choice.strip()
                if choice == '1' and "Golden Watch" in self.items:
                    self.golden_watch = True
                    self.items.remove("Golden Watch")
                    print("🛡️ Golden Watch 활성화됨!")
                elif choice == '2' and "Double Damage" in self.items:
                    self.double_damage_count += 1
                    self.items.remove("Double Damage")
                    print("💥 데미지 2배 적용됨!")
                elif choice == '3' and "100% Hit" in self.items:
                    self.use_100_hit = True
                    self.items.remove("100% Hit")
                    print("🎯 100% 명중 적용됨!")
                elif choice == '4' and "Heal Pack" in self.items:
                    self.hp = min(MAX_HP, self.hp + 2)
                    self.items.remove("Heal Pack")
                    print("❤️ 체력 2 회복!")
                elif choice == '5':
                    print("아이템을 사용하지 않았습니다.")

    def attack(self, target):
        input(f"\n[{self.name}의 차례입니다] Enter를 눌러 공격하세요...")
        weapon_data = weapons[self.weapon]
        hit_chance = 1.0 if self.use_100_hit else weapon_data["hit_chance"]
        self.use_100_hit = False

        if random.random() < hit_chance:
            damage = weapon_data["damage"] * (2 ** self.double_damage_count)
            self.double_damage_count = 0  # reset only on hit
            if target.golden_watch:
                print(f"{target.name}의 Golden Watch가 공격을 막았습니다! 🛡️ (깨짐)")
                target.golden_watch = False
            else:
                target.hp -= damage
                print(f"{self.name}의 공격 성공! 🎯 {target.name}에게 {damage} 데미지!")
        else:
            print(f"{self.name}의 공격이 빗나갔습니다! ❌")
            self.double_damage_count = 0  # also reset on miss
            if target.golden_watch:
                print(f"{target.name}의 Golden Watch가 반응했지만 쓸모 없이 깨졌습니다... 😢")
                target.golden_watch = False

def shop(player):
    print("\n🛒 상점 입장:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item} - {items[item]['price']}코인: {items[item]['desc']}")
    print("0. 나가기")
    while True:
        choice = input("아이템 번호 입력: ")
        if choice == '0':
            break
        try:
            item_name = list(items.keys())[int(choice)-1]
            price = items[item_name]["price"]
            if player.coins >= price:
                player.coins -= price
                player.items.append(item_name)
                print(f"{item_name} 구매 완료! 남은 코인: {player.coins}")
            else:
                print("코인이 부족합니다.")
        except:
            print("잘못된 입력입니다.")

def battle():
    player = Player("당신")
    computer = Player("컴퓨터", is_computer=True)

    player.choose_weapon()
    shop(player)
    computer.choose_weapon()

    while player.hp > 0 and computer.hp > 0:
        print(f"\n당신 HP: {player.hp} | 컴퓨터 HP: {computer.hp}")
        print(f"당신 코인: {player.coins}")

        player.choose_items()
        computer.choose_items()

        print("\n🎯 전투!")
        player.attack(computer)
        if computer.hp <= 0:
            print("🎉 당신이 이겼습니다!")
            player.coins += 50
            break

        computer.attack(player)
        if player.hp <= 0:
            print("💀 컴퓨터가 승리했습니다... 게임 오버.")
            break

    print(f"\n🏁 최종 결과: 당신 코인 {player.coins} | 체력 {player.hp}")

if __name__ == "__main__":
    battle()
