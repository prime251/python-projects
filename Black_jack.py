import random


def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def calculate_score(hand):
    score = 0
    aces = 0
    for card, suit in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 11
            aces += 1
        else:
            score += int(card)
    
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def show_hand(hand):
    return ' '.join([f'{rank}{suit}' for rank, suit in hand])


def blackjack_game():
    money = 100
    deck = create_deck()

    print("🎲 Welcome to Blackjack! You start with $100.")

    while money > 0:
        if len(deck) < 10: 
            print("🔄 Reshuffling deck...")
            deck = create_deck()

        print(f"\n💵 You have ${money}.")
        bet = input("Place your bet (or 'q' to quit): ")
        if bet.lower() == 'q':
            print("Thanks for playing!")
            break
        if not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
            print("Invalid bet. Try again.")
            continue
        bet = int(bet)

        
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print(f"\n🧑 Your hand: {show_hand(player_hand)} (Score: {calculate_score(player_hand)})")
        print(f"🃏 Dealer shows: {dealer_hand[0][0]}{dealer_hand[0][1]}")

     
        while True:
            move = input("(h)it or (s)tand? ").lower()
            if move == 'h':
                player_hand.append(deck.pop())
                print(f"Your hand: {show_hand(player_hand)} (Score: {calculate_score(player_hand)})")
                if calculate_score(player_hand) > 21:
                    print("💥 Bust! You lose.")
                    money -= bet
                    break
            elif move == 's':
                break
            else:
                print("Invalid input.")

    
        if calculate_score(player_hand) <= 21:
            print(f"\n🃏 Dealer hand: {show_hand(dealer_hand)} (Score: {calculate_score(dealer_hand)})")
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                print(f"Dealer hits: {show_hand(dealer_hand)} (Score: {calculate_score(dealer_hand)})")
        
            dealer_score = calculate_score(dealer_hand)
            player_score = calculate_score(player_hand)

            if dealer_score > 21 or player_score > dealer_score:
                print("✅ You win!")
                money += bet
            elif dealer_score > player_score:
                print("❌ Dealer wins!")
                money -= bet
            else:
                print("🤝 It's a tie!")

        if money == 0:
            print("\n💸 You're out of money! Game over.")

blackjack_game()
