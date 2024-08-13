import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = len(stages) - 1
# print(lives)

chosen_word = random.choice(word_list)
# print(chosen_word)

print(logo)

display = []
for _ in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("\n\nYou loose!")
            end_of_game = True

    # print(f"{''.join(display)}")
    print(display)

    if "_" not in display:
        print("\n\nYou won!")
        end_of_game = True

    print(stages[lives])
