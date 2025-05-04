import random
import matplotlib.pyplot as plt

# 회사 목록 및 초기 설정
COMPANIES = ["APPLE", "TESLA", "AMAZON", "GOOGLE", "MICROSOFT"]
prices = {name: 100 + random.randint(-20, 20) for name in COMPANIES}
portfolio = {name: 0 for name in COMPANIES}
cash = 1000
day = 1

def update_prices():
    for name in COMPANIES:
        direction = random.choice(["up", "down"])  # 50:50 확률
        change = random.randint(1, 10)
        if direction == "up":
            prices[name] += change
        else:
            prices[name] = max(1, prices[name] - change)

def show_status():
    print(f"\n📅 Day {day}")
    print(f"💰 Cash: ${cash}")
    print("📊 Portfolio:")
    for i, name in enumerate(COMPANIES, 1):
        print(f"  {i}. {name}: {portfolio[name]} shares at ${prices[name]}")
    total = cash + sum(prices[n] * portfolio[n] for n in COMPANIES)
    print(f"💼 Total Assets: ${total}")

def buy_stock():
    print("Choose stock to buy:")
    for i, name in enumerate(COMPANIES, 1):
        print(f"  {i}. {name} (${prices[name]})")
    choice = input("> ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(COMPANIES)):
        print("❌ Invalid choice.")
        return
    stock = COMPANIES[int(choice) - 1]
    qty = input("How many shares? ")
    if not qty.isdigit():
        print("❌ Invalid number.")
        return
    qty = int(qty)
    cost = prices[stock] * qty
    global cash
    if cost > cash:
        print("❌ Not enough cash.")
    else:
        cash -= cost
        portfolio[stock] += qty
        print(f"✅ Bought {qty} shares of {stock}.")

def sell_stock():
    print("Choose stock to sell:")
    for i, name in enumerate(COMPANIES, 1):
        print(f"  {i}. {name} ({portfolio[name]} shares at ${prices[name]})")
    choice = input("> ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(COMPANIES)):
        print("❌ Invalid choice.")
        return
    stock = COMPANIES[int(choice) - 1]
    qty = input("How many shares? ")
    if not qty.isdigit():
        print("❌ Invalid number.")
        return
    qty = int(qty)
    if qty > portfolio[stock]:
        print("❌ Not enough shares.")
    else:
        global cash
        cash += prices[stock] * qty
        portfolio[stock] -= qty
        print(f"✅ Sold {qty} shares of {stock}.")

# 메인 루프
while True:
    update_prices()
    show_status()

    print("\nChoose action:")
    print("1. Buy")
    print("2. Sell")
    print("3. Next Day")
    print("4. Quit")
    choice = input("> ").strip()

    if choice == "1":
        buy_stock()
    elif choice == "2":
        sell_stock()
    elif choice == "3":
        day += 1
    elif choice == "4":
        print("🏁 Game Over.")
        show_status()
        break
    else:
        print("❌ Invalid choice.")
