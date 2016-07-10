__author__ = 'shahjalal'

import random

game_on = None

guesses = None

secret = None

def difficulty_level_easy():
    global secret
    secret = int(random.randrange(0, 100))

    while game_on:
        guess = int(raw_input("Guess a number: "))
        if guess > secret:
            print("Your guess is too high. Try again.")
        elif guess < secret:
            print("Your guess is too low. Try again.")
        elif guess == secret:
            print("You win!")
            play_again()

def difficulty_level_hard():
    global guesses
    global secret
    guesses = 3
    secret = int(random.randrange(0, 100))

    print("You will get three chances to win!")
    for i in range(guesses):
        guess = int(raw_input("Guess a number: "))
        if i == 2:
            print("Game over. Too many guesses.")
            play_again()
        elif guess > secret:
            print("Your guess is too high. Try again.")
        elif guess < secret:
            print("Your guess is too low. Try again.")
        elif guess == secret:
            print("you win!")
            play_again()

def start_game():
    global game_on
    game_on = True

    level = raw_input("Welcome. Type easy(e), hard(h) or quit(q) ")
    if level == "e":
        difficulty_level_easy()
    elif level == "h":
        difficulty_level_hard()
    elif level == "q":
        game_on = False
        print("Thanks for playing. Good Bye...")

def play_again():
    global game_on
    game_on = True
    play = raw_input("Play again? Yes(y) or No(n). ")

    if play == "y":
        start_game()
    else:
        game_on = False
        print("Thanks for playing. ")


if __name__ == '__main__':
    start_game()
