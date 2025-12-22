num_str = input  ("Введите четырехзначное число  : ")
num = int (num_str)
a = num % 10
b = num // 1000
c = num // 100 % 10
d = num // 10 % 10
print (f"результат: {a * b * c * d}")