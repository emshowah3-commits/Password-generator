import random

# password key components
special_char = "!@#$%^&*"
numbers = "123456789"
lower_letters = "qwertyuiopasdfghjklzxcvbnm"
upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

# password creation interactive part
def user_char():

    user_char = int(input("how many special characters do you want?: "))
    if user_char == "1":
        user_char_gen = random.sample(special_char, 1)

    elif user_char == "2":
        user_char_gen = random.sample(special_char, 2)

    elif user_char == "3":
        user_char_gen = random.sample(special_char, 3)

    numbers_input = int(input("how many numbers do you want in your password?: "))
    if numbers_input == "1":
        numbers_give = random.sample(numbers, 1)

    print(user_char_gen)
