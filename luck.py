import random

GOAL = 16990
FLOOR_PER_BIOME = 3398
biomes = ["Forest 🌲", "Cave 🕳️", "Extreme 🏔️"]

current_floor = 0
turns = 0

def get_biome(floor):
    index = (floor // FLOOR_PER_BIOME) % len(biomes)
    return biomes[index]

print("🎲 Welcome to the Tower of Luck!")
print(f"Goal: Reach floor {GOAL}")
print("Choose wisely. Each option has risk and reward!\n")

while current_floor < GOAL:
    turns += 1
    biome = get_biome(current_floor)
    print(f"\n📍 Turn {turns} | Current floor: {current_floor} | Biome: {biome}")

    # === Option 1 ===
    floors = random.randint(1, 999)
    chance1 = random.randint(20, 80)

    # === Option 2 ===
    multiplier = random.randint(2, 5)
    chance2 = random.randint(30, 70)

    # === Option 3 ===
    biome_shift = random.choice([-1, 1])
    chance3 = random.randint(1, 99)

    # Show options
    print(f"1️⃣  Move ±{floors} floors  ({chance1}% success)")
    print(f"2️⃣  Multiply or divide current floor by {multiplier}  ({chance2}% success)")
    print(f"3️⃣  Move biome {'forward' if biome_shift > 0 else 'backward'}  ({chance3}% success)")

    # Get input
    while True:
        try:
            choice = int(input("Pick 1, 2, or 3: "))
            if choice in [1, 2, 3]:
                break
        except ValueError:
            pass
        print("❌ Invalid choice.")

    success = False
    if choice == 1:
        success = random.randint(1, 100) <= chance1
        delta = floors if success else -floors
        current_floor += delta
        print(f"{'✅ Success!' if success else '❌ Failed!'} You {'moved up' if delta > 0 else 'moved down'} {abs(delta)} floors.")

    elif choice == 2:
        success = random.randint(1, 100) <= chance2
        if current_floor == 0:
            print("🚫 You are on floor 0. Nothing happens.")
        else:
            if success:
                current_floor *= multiplier
                print(f"✅ Success! Multiplied floor by {multiplier}. New floor: {current_floor}")
            else:
                current_floor //= multiplier
                print(f"❌ Failed! Divided floor by {multiplier}. New floor: {current_floor}")

    elif choice == 3:
        success = random.randint(1, 100) <= chance3
        if success:
            current_biome_index = (current_floor // FLOOR_PER_BIOME)
            new_index = current_biome_index + biome_shift
            new_floor = max(0, new_index * FLOOR_PER_BIOME)
            print(f"✅ Biome jump! Moving to floor {new_floor} ({get_biome(new_floor)})")
            current_floor = new_floor
        else:
            print("❌ Biome jump failed. You stay on the same floor.")

    # Prevent negative floor
    if current_floor < 0:
        current_floor = 0

# 🎉 Game Over
print(f"\n🏆 You reached floor {current_floor} in {turns} turns! Congratulations!")
