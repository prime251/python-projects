import random

# 강화 확률 리스트
success_chances = [
    100, 99, 95, 90, 88, 86, 82, 80, 76, 74,
    71, 70, 62, 58, 50, 43, 40, 32, 28, 21,
    18, 15, 12, 10, 5, 3, 2, 1, 1  # +28까지
]

# 판매 가격 리스트 (레벨 0 ~ 28)
sell_prices = [
    0, 0, 0, 0, 0, 5, 8, 10, 12, 15,
    20, 20, 25, 30, 70, 100, 130, 150, 190, 280,
    330, 370, 410, 490, 590, 720, 950, 999, 100000000
]

level = 0
total_coins = 0

print("💎 Sword Upgrade Simulator 💎")
print("목표: 강화하고, 적절할 때 팔아서 코인을 최대한 많이 모으세요!\n")

while True:
    print(f"현재 검: +{level} | 총 보유 코인: {total_coins}")
    action = input("👉 강화하려면 [Enter], 팔려면 [sell], 종료하려면 [q]: ").strip().lower()

    if action == "q":
        print("게임을 종료합니다.")
        break
    elif action == "sell":
        coins_earned = sell_prices[level]
        total_coins += coins_earned
        print(f"💰 +{level} 검을 {coins_earned} 코인에 판매했습니다!")
        print("🔁 새로운 검으로 다시 시작합니다.\n")
        level = 0
    else:
        if level >= len(success_chances) - 1:
            print("🔥 이미 최고 강화 단계입니다!")
            continue

        chance = success_chances[level]
        roll = random.randint(1, 100)

        print(f"🛠️ +{level} → +{level+1} 강화 시도... 확률 {chance}%, 뽑기: {roll}")

        if roll <= chance:
            level += 1
            print(f"✅ 성공! 검이 +{level}로 강화되었습니다!\n")
        else:
            print(f"❌ 실패... 검은 +{level} 상태를 유지합니다.\n")
