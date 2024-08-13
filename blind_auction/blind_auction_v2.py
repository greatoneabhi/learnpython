from auction_art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bid = {}


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with bid ${highest_bid}")


bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bid[name] = price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bid)
    else:
        bidding_finished = False
        os.system("clear")
