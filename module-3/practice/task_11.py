str = input("Введите целые числа от 0 до 100 ")
str_to_number=list(map(int, str.split()))
negative_numbers =  [num for num in str_to_number if num < 0]
negative_numbers_sum=sum(negative_numbers)
print(negative_numbers_sum)
even_numbers = sum(x for x in str_to_number if x  % 2 == 0)
print(even_numbers)
odd_numbers= sum(x for x in str_to_number if x  % 2 != 0)
print(odd_numbers)
Multiples_numbers=[l for l in str_to_number if l  % 3 == 0]
result =1
for number in Multiples_numbers: result*= number
print(result)
min_el=