with open("file_handler/my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("file_handler/my_file.txt", mode="a") as file:
    file.write("new text 1.")


with open("file_handler/new_file.txt", mode="w") as file:
    file.write("new file created.")
