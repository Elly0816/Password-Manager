import string
from random import randint, choice, shuffle


def password_generator():
    # create list of letters, numbers and symbols
    letters = [item for item in string.ascii_letters]
    numbers = [i for i in range(0, 10)]
    symbols = [item for item in string.punctuation]

    # Assign random amounts to letters, numbers and symbols
    # Create password list
    # Append numbers, letters and symbols to the password list
    password_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    # Shuffle the password list
    shuffle(password_list)

    password_tuple = "".join(str(item) for item in password_list)

    return password_tuple


# print(password_generator())
