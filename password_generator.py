import random
import csv

# password key components
special_char = "!@#$%^&*"
numbers = "123456789"
lower_letters = "qwertyuiopasdfghjklzxcvbnm"
upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

random_special_char = random.sample(special_char, 3)
random_numbers = random.sample(numbers, 7)
random_lletters =  random.sample(lower_letters, 6)
random_uletter = random.sample(upper_letters, 5)
result = random_special_char + random_numbers + random_lletters + random_uletter
random.shuffle(result)
clean = ''.join(result)
print(clean)

with open('password.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(clean)