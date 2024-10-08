import random

LETTERS = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

def generate():
    nr_letters = random.randint(8, 10) 
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_numbers = [random.choice(NUMBERS) for _ in range(nr_numbers)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    random_password = "".join(password_list)
    return random_password

