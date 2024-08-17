import random
import string

length = int(input("Введите длину пароля: "))

lwr_letters = string.ascii_lowercase
uppr_letters = string.ascii_uppercase
digits = string.digits
special_characters = ",.*^_()[]{}?!@"

all_characters = lwr_letters + uppr_letters + digits + special_characters

password = (
    random.choice(lwr_letters)
    + random.choice(uppr_letters)
    + random.choice(digits)
    + random.choice(special_characters)
)
password += "".join(random.choice(all_characters) for _ in range(length - 4))

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print(f"Сгенерированный пароль: {password}")
