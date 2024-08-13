from art import logo, vs
from gamer_data import data
import random
import os


def calculate_score(item1, item2):
    if int(item1["follower_count"]) > int(item2["follower_count"]):
        return False
    else:
        return True


def show_result(is_game_over, score):
    if not is_game_over:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

    return score


def play_game():
    score = 0
    is_game_over = False
    account_B = random.choice(data)

    while not is_game_over:
        account_A = account_B
        account_B = random.choice(data)

        if account_A == account_B:
            account_B = random.choice(data)

        print(
            f"Compare A: {account_A["name"]}, {account_A["description"]}, from {account_A["country"]}"
        )
        print(vs)
        print(
            f"Against B: {account_B["name"]}, {account_B["description"]}, from {account_B["country"]}"
        )
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == "A":
            is_game_over = calculate_score(account_A, account_B)
        else:
            is_game_over = calculate_score(account_B, account_A)
        os.system("clear")
        print(logo)
        score = show_result(is_game_over, score)


def main():
    print(logo)
    play_game()


if __name__ == "__main__":
    main()
