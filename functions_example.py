def formant_name(f_name, l_name):
    """
    Take a first and last name and format it to
    return the title case verson of the name.
    """
    if f_name == "" or l_name == "":
        return "You didn't provided any inputs."
    full_name = f_name + " " + l_name
    return full_name.title()


formated_name = formant_name(
    input("What is your first name? "), input("What is your last name? ")
)

print(f"result: {formated_name}")
