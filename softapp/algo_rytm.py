import random
import string


# def genereting_pass(num):
#     alphabet = string.ascii_letters
#     symbols = "!@#$%^&*()_+"
#     numbers = string.digits
#     all_characters = alphabet + symbols + numbers
#
#     password = ''.join(random.choice(all_characters) for _ in range(num))
#
#     # Добавить хотя бы одну цифру, если она отсутствует
#     if not any(char.isdigit() for char in password):
#         index = random.randint(0, len(numbers) - 1)
#         password = password[:index] + random.choice(numbers) + password[index + 1:]
#
#     return password


def genereting_pass(length=12, uppers=None, numbers=None, special=None):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    if uppers:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if numbers:
        characters.extend(list('0123456789'))
    if special:
        characters.extend(list('!@#$%^&*()_+'))
    for i in range(length):
        password += random.choice(characters)
    return password

if __name__ == '__main__':
    print(genereting_pass(10))