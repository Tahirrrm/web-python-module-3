import random
def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4]))
def count_bulls_and_cows(number, guess):
    cows = 0  
    bulls = 0  
    for i in range(4):
        if guess[i] == number[i]:
            cows += 1
    number_list = list(number)
    guess_list = list(guess)
    for i in range(4):
        if guess_list[i] == number_list[i]:
            number_list[i] = None
            guess_list[i] = None
    for digit in guess_list:
        if digit is not None and digit in number_list:
            bulls += 1
            number_list.remove(digit)
    return cows, bulls
def game_recursive(number, attempts=0):
    guess = input("Введите ваше четырёхзначное число: ").strip()
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        print("цифры не должны повторяться")
        return game_recursive(number, attempts)  
    attempts += 1
    if guess == number:
        print(f"Вы угадали число {number} за {attempts} попыток.")
        return 
    cows, bulls = count_bulls_and_cows(number, guess)
    print(f"Коровы: {cows}, Быки: {bulls}")
    game_recursive(number, attempts)
print("Угадайте четырёхзначное число (без повторяющихся цифр).")
print("«Коровы» — цифры на своих местах.")
print("«Быки» — цифры есть в числе, но не на своих местах.")
number = generate_number()
game_recursive(number)


