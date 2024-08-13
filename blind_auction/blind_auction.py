from auction_art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bidders = []


def add_bidders(name, bid):
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bidders.append(bidder)


auction_continue = True
while auction_continue:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    add_bidders(name, bid)

    result = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if result == "no":
        auction_continue = False
    os.system("clear")

winner = {}
max_bid = 0
for bidder in bidders:
    bid = int(bidder["bid"])
    if bid > max_bid:
        winner["name"] = bidder["name"]
        winner["bid"] = bidder["bid"]

print(f"Winner is {winner['name']} with bid {winner['bid']}")
