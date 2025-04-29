import random

def mafia_game():
    players = {
        "Alice": {"gender": "Female", "height": "Short", "hair": "Blonde", "shoes": "Heels"},
        "Bob": {"gender": "Male", "height": "Tall", "hair": "Brown", "shoes": "Sneakers"},
        "Charlie": {"gender": "Male", "height": "Short", "hair": "Black", "shoes": "Boots"},
        "David": {"gender": "Male", "height": "Tall", "hair": "Blonde", "shoes": "Sneakers"},
        "Eve": {"gender": "Female", "height": "Tall", "hair": "Black", "shoes": "Sneakers"},
        "Frank": {"gender": "Male", "height": "Short", "hair": "Brown", "shoes": "Boots"},
        "Grace": {"gender": "Female", "height": "Short", "hair": "Brown", "shoes": "Sneakers"},
        "Heidi": {"gender": "Female", "height": "Tall", "hair": "Blonde", "shoes": "Heels"},
        "Ivan": {"gender": "Male", "height": "Tall", "hair": "Black", "shoes": "Boots"},
        "Judy": {"gender": "Female", "height": "Short", "hair": "Brown", "shoes": "Sneakers"}
    }

    traits = ['height', 'hair', 'shoes']
    alive_players = list(players.keys())
    mafia = random.sample(alive_players, 2)
    mafia_labels = {mafia[0]: "Mafia 1", mafia[1]: "Mafia 2"}  # Label them
    caught_mafia = []
    guesses_made = 0
    max_guesses = 6
    innocent_deaths = 0
    used_clues = []

    print("🔎 Welcome to Mafia Game: 2 Mafia, 1 Clue Per Round (Labelled) Edition 🔎")
    print("Catch both Mafia within 6 guesses!")
    print()

    round_num = 1
    while guesses_made < max_guesses and len(caught_mafia) < 2 and innocent_deaths < 6:
        print(f"\n🌙 Round {round_num}")
        round_num += 1

        # Mafia kills someone (random innocent)
        possible_victims = [p for p in alive_players if p not in mafia and p not in caught_mafia]
        if possible_victims:
            killed = random.choice(possible_victims)
            alive_players.remove(killed)
            innocent_deaths += 1
            print(f"💀 {killed} was eliminated by the Mafia.")
        else:
            print("⚠️ All innocents are dead. Mafia wins.")
            break

        # Give 1 hint about one mafia (random trait)
        current_mafia = random.choice(mafia)
        mafia_number = mafia_labels[current_mafia]  # Mafia 1 or Mafia 2
        info = players[current_mafia]
        available_clues = [t for t in traits if (current_mafia, t) not in used_clues]
        if available_clues:
            clue_type = random.choice(available_clues)
            used_clues.append((current_mafia, clue_type))
            value = info[clue_type]
            print(f"🧩 Clue about **{mafia_number}**: The suspect seems to have '{value}' {clue_type}.")
        else:
            print("🧩 No more new clues available for this Mafia.")

        print(f"🧍 Alive players: {alive_players}")
        print(f"🎯 Guesses used: {guesses_made} / {max_guesses}")
        print()

        # Forced guess
        guess = input("🕵️ Who do you think is Mafia? ").strip()

        if guess not in players:
            print("❌ Not a valid person. Try again.\n")
            continue
        if guess not in alive_players:
            print(f"⚠️ {guess} is already eliminated. Try again.\n")
            continue

        guesses_made += 1

        if guess in mafia:
            print(f"✅ {guess} was Mafia! Well done.")
            caught_mafia.append(guess)
            alive_players.remove(guess)
        else:
            print(f"❌ {guess} was innocent. Eliminated by mistake.")
            alive_players.remove(guess)
            innocent_deaths += 1

    # Final Result
    print("\n🏁 Game Over.")
    print(f"🕵️ Mafia were: {mafia[0]} (Mafia 1) and {mafia[1]} (Mafia 2)")
    print(f"🎯 You caught: {caught_mafia}")
    print(f"💀 Innocent deaths: {innocent_deaths}")

    if len(caught_mafia) == 2 and innocent_deaths < 6:
        score = len([p for p in alive_players if p not in mafia])
        print(f"🏆 You WIN! Score: {score} points (survivors)")
    else:
        print("❌ You LOSE. Score: 0")

while input("\nPlay again? (y/n): ").lower() == "y":
    mafia_game()
