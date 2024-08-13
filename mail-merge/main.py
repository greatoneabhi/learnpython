# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

lines = []

with open("mail-merge/Input/Letters/starting_letter.txt", mode="r") as file:
    lines = file.readlines()

with open("mail-merge/Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    for name in names:
        name = name.strip()
        new_line = lines[0].replace("[name]", name)
        name = name.replace(" ", "_")
        with open(
            f"mail-merge/Output/ReadyToSend/letter_{name}.txt", mode="w"
        ) as letter:
            letter.write(new_line)
        for line in lines[1:]:
            with open(
                f"mail-merge/Output/ReadyToSend/letter_{name}.txt", mode="a"
            ) as letter:
                letter.write(line)
