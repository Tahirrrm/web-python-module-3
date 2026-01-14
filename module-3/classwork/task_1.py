# numbers = [1,2,3,4,5]
# total = sum (numbers)
# print (total)

# numbers = [1,2,3,4,5]
# maximum = max (numbers)
# minimum= min (numbers)
# print (minimum,maximum)

# numbers = [3,1,7,4,8,9,2]
# sorted_nums = sorted (numbers ,reverse = True)
# print (sorted_nums)
# rev = reversed (numbers)
# print (list(rev))

# fruits = [ "apple", "cherry", "banana"]
# for index, fruit in enumerate (fruits):
#     print (f"{index} : {fruit}")
# def double (num):
#     return num *2
# numbers = ["1","2","3"]
# s = list (map (int, numbers))
# list_double = list(map(double,s))
# print (list_double)

# def filter_func(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = list (filter(lambda x: x % 2 == 0, numbers))
# evens1 = list (filter (filter_func,numbers))
# print (evens)
# print (evens1)



# words = [ "paper", "apple", "car"]
# result = " ".join(words)
# print (result)

# my_list = ["apple", "banana" , 2]
# my_list_1= ["hleb",5,"a"]
# new_list = my_list + my_list_1
# my_list += my_list_1
# print (new_list,my_list)
# my_list.append (4)
# my_list.extend ("apple")
# print (my_list)

# my_list = ["apple",2, "ban"]
# my_list.insert (1,"code")
# my_list.remove("apple")
# my_list.pop()
# my_list.pop(1)
# my_list.clear()
# print(my_list)

# my_list = [5,2,4,4,5,6,7,8]
# count =  my_list.count (2)
# my_list.sort()
# my_list.sort(reverse = True)
# print (my_list)
# # print (count)
# my_list = [-1,2,3,4,5,6,7,8,9,10]
# # print( my_list [:6])
# # print( my_list [2:])
# # print( my_list [:])
# # print (my_list[0:5:2])
# # print( my_list [-1])
# # print( my_list [-5:])
# # print( my_list [:: -1])
# # res = [x**2 for x in my_list if x % 2 == 0]
# # result = []
# # print (res, result)
# res = [0 if x <0 else x for x in my_list]
# print (res)

# задача 1

# word = ["apple","banana", "car","python","cat"]
# res = [ x  for x in word if len(x) >=4]
# print (res)

# задача 2
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# n= int (input("Введите числа"))

# print(numbers [::n])

# задача 3
numbers = [0,1,2,3,4,5,6,7,8,9,10]
total = sum (numbers) / len(numbers)
res= [x  for x in numbers if x >total]
print (total,res)
