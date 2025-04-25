import random

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input('Your Guess : '))

    if my_guess == number_to_guess:
        print(f'Conglatulation! You guessed in {guess_counter} attempt')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Wrong the number is {number_to_guess} ')

    elif my_guess > number_to_guess:
        print('LOWER')

    elif my_guess < number_to_guess:
        print('HIGHER')
