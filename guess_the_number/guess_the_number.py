from art import logo
from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TUNRS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TUNRS


def guess_the_number(attempts):
    number = randint(1, 100)
    is_game_over = False
    while not is_game_over:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess 🤔: "))
            if guess == number:
                print(f"You got it 😎 ! The answer was {number}.")
                is_game_over = True
            elif guess > number:
                print("Too high.😥")
            else:
                print("Too low.😥")
            attempts -= 1
            if attempts > 0 and not is_game_over:
                print("Guess again. 🤔")

        else:
            print("You've run out of the guesses, you lose. 😭")
            is_game_over = True


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    guess_the_number(attempts)


if __name__ == "__main__":
    main()
