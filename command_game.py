import random
import time

VALID_KEYS = [
    'space', 'm', 'n', 'b', 'v', 'c', 'x', 'z',
    'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a',
    'p', 'o', 'i', 'u', 'y', 't', 'r', 'e', 'w', 'q'
]

print("🎮 Do-It Game — Type the key exactly N times within 3 seconds!")

while True:
    key = random.choice(VALID_KEYS)
    count = random.randint(1, 9)
    display_key = 'SPACE' if key == 'space' else key.upper()
    expected = (' ' if key == 'space' else key) * count

    print(f"\n➡️ Type '{display_key}' exactly {count} times (no spaces).")
    print("⏳ You have 3 seconds!")

    start = time.time()
    try:
        user_input = input("> ")
    except:
        user_input = ""
    end = time.time()

    duration = end - start

    if duration > 3:
        print(f"❌ Time's up! You took {duration:.2f} seconds.")
    elif user_input == expected:
        print("✅ Correct! You win!")
    else:
        print(f"❌ Wrong! You typed: '{user_input}' (expected: '{expected}')")

    again = input("\n▶️ Play again? (y/n): ").lower()
    if again != 'y':
        break

print("👋 Thanks for playing!")
