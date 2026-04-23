a = float(input  ("Введите число 1 : "))
b = float(input  ("Введите число 2 : "))
c = input  ("Выберите нужную операцию:  + - * / ")
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("на ноль делить нельзя")
else:
    print("Неверная операция")



import random
random_list = [random.randint(-10, 100) for _ in range(20)]
print(random_list)
print(min(random_list))
print(max(random_list))
positive_num = 0
negative_num = 0
zero_num = 0
for num in random_list:
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1
    else:
        zero_num += 1
print(positive_num)
print(negative_num)
print(zero_num)
