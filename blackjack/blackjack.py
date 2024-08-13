import random

from art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def display_logo():
    print(logo)


def calculate_score(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum


def select_cards(quantity):
    selected_cards = []
    for _ in range(0, quantity):
        selected_cards.append(CARDS[random.randint(0, len(CARDS) - 1)])
    return selected_cards


def diff_with_21(final_score):
    if final_score > 21:
        return final_score - 21
    else:
        return 21 - final_score


def blackjack(player_scores):
    player_scores["player"].extend(select_cards(2))
    player_scores["computer"].extend(select_cards(2))
    final_player_score = calculate_score(player_scores["player"])
    final_computer_score = calculate_score(player_scores["computer"])
    print(f"Your cards: {player_scores['player']}, current score: {final_player_score}")
    print(f"Computer's first card: {player_scores['computer'][0]}")
    if final_computer_score == 21:
        print("Your opponent won with a Blackjack. You loose 😭")
        should_continue = False
    elif final_player_score == 21:
        print("Win with a Blackjack 😎")
        should_continue = False
    else:
        should_continue = True

    while should_continue:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if "y" == draw_card:
            player_card = select_cards(1)
            if player_card[0] == 11 and final_player_score + player_card[0] > 21:
                player_card[0] = 1

            player_scores["player"].append(player_card[0])
            final_player_score = calculate_score(player_scores["player"])
            if final_player_score > 21:
                print(
                    f"Your final hand: {player_scores['player']}, final score: {final_player_score}"
                )
                print(
                    f"Computer's final hand: [{player_scores['computer'][0]}], final score: {player_scores['computer'][0]}"
                )
                print("You went over. You loose 😭")
                should_continue = False
            elif final_player_score == 21:
                print(
                    f"Your final hand: {player_scores['player']}, final score: {final_player_score}"
                )
                print(
                    f"Computer's final hand: [{player_scores['computer'][0]}], final score: {player_scores['computer'][0]}"
                )
                print("You won. Congratulation 😎")
                should_continue = False
            else:
                print(
                    f"Your cards: {player_scores['player']}, current score: {final_player_score}"
                )
                print(f"Computer's first card: {player_scores['computer'][0]}")
        else:
            while final_computer_score <= 16:
                computer_card = select_cards(1)
                if (
                    computer_card[0] == 11
                    and final_computer_score + computer_card[0] > 21
                ):
                    computer_card[0] = 1

                player_scores["computer"].append(computer_card[0])
                final_computer_score = calculate_score(player_scores["computer"])

            print(
                f"Your final hand: {player_scores['player']}, final score: {final_player_score}"
            )
            print(
                f"Computer's final hand: {player_scores['computer']}, final score: {final_computer_score}"
            )
            if final_player_score == final_computer_score:
                print("It's a draw. 🤯")
            elif final_player_score == 21 or final_computer_score > 21:
                print("You won. Congratulation 😎")
            else:
                player_diff_wining_score = diff_with_21(final_player_score)
                computer_diff_wining_score = diff_with_21(final_computer_score)
                if player_diff_wining_score < computer_diff_wining_score:
                    print("You won. Congratulation 😎")
                else:
                    print("Your opponent won. You loose 😭")
            should_continue = False
    main()


def main():
    if (
        input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        == "y"
    ):
        player_scores = {"player": [], "computer": []}
        display_logo()
        blackjack(player_scores)
    else:
        print("Exiting Game !")


if __name__ == "__main__":
    main()
