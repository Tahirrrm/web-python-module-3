str = input("Введите целые числа от 0 до 100 ")
str_to_number=list(map(int, str.split()))
str_count= int(input("Введите число для подсчета в списке"))
users_number_count=str_to_number.count(str_count)
print(users_number_count)

