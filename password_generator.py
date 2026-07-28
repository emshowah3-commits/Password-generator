import random

# password key components
special_char = "!@#$%^&*"
numbers = "123456789"
lower_letters = "qwertyuiopasdfghjklzxcvbnm"
upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

# password creation interactive part
user_char = int(input("how many special characters do you want?: "))
if user_char == 0:
    random.sample(special_char, k=1)
print(user_char)
