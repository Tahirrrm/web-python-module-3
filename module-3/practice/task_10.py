str = input("Введите целые числа от 0 до 100 ")
str_to_number=list(map(int, str.split()))
numbers_sum= sum(str_to_number)
users_number_count=len(str_to_number)
arithmetic_mean= numbers_sum/users_number_count
print(numbers_sum)
print(arithmetic_mean)