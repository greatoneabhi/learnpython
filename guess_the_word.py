# Step 1
import random


def create_blanks(word):
    character_list = []
    for _ in range(len(word)):
        character_list.append("_")
    return character_list


word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
display = create_blanks(chosen_word)
# print(blanks)

# guess_character = input("Guess a letter: ").lower()
remaining_guess = len(chosen_word)

while remaining_guess > 0:
    guess_character = input("Guess a letter: ").lower()
    characters_matched = 0
    for n in range(len(chosen_word)):
        if guess_character == chosen_word[n]:
            display[n] = guess_character
            characters_matched += 1
    if characters_matched != 0:
        remaining_guess -= characters_matched
    else:
        remaining_guess -= 1
    print(display)

success_count = 0
for n in range(len(chosen_word)):
    if display[n] == chosen_word[n]:
        success_count += 1

if success_count == len(chosen_word):
    print("You Won!")
else:
    print("You Loose!")
