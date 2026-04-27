def func(a,b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    else:
        return func(b,a % b)
num_1= int(input("Введите первое число:"))
num_2= int(input("Введите второе число:"))
result= func(num_1,num_2)
print(result)