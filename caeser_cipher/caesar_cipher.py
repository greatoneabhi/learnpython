from caeser_cipher_art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)


def encrypt(message, shift):
    cipher_text = ""
    for n in message:
        position = alphabet.index(n)
        new_position = position + shift
        total_alphabets = len(alphabet)
        if new_position >= total_alphabets:
            new_position = new_position - total_alphabets
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(message, shift):
    plain_text = ""
    for n in message:
        position = alphabet.index(n)
        new_position = position - shift
        total_alphabets = len(alphabet)
        if new_position <= 0:
            new_position = new_position + total_alphabets
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


def caesar_cipher(text, shift, direction):
    end_text = ""
    while shift >= len(alphabet):
        shift = shift % len(alphabet)

    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position >= len(alphabet):
                new_position = new_position - len(alphabet)
            elif new_position < 0:
                new_position = new_position + len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}")


continue_cipher = True
while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text=text, shift=shift, direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() == "no":
        print("Goodbye")
        continue_cipher = False
