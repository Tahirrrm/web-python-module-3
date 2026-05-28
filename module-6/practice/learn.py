
# my_set = {1,1,2,2,3,3}
# print(my_set)
# my_set_1 = set([1,2,3,3,4])
# print(my_set_1)
# my_set_2 =  set("привет")
# print(my_set_2)

# my_set_3 = set((1,2,3,3,4))    # через кортеж
# print(my_set_3)

# # генератор множеств
# my_set_4 = { x for x in range(5)}
# print(my_set_4)

# #добавление элементов
# fruits = {"яблоко","банан","апельсин"}
# fruits.add("груша")
# fruits.update(["смородина","клубника"])
# print(fruits)

# #удаление элементов
# fruits = {"яблоко","банан","апельсин"}
# fruits.remove("яблоко")  #если в списке нет то будет ошибка
# fruits.discard("груша")  # не будет ошибки если нет в списке
# fruits.pop() #удаляет рандомный элемент
# print(fruits)

# #операции над множествами

# #Обьединение
# set_a ={1,2,3,4}
# set_b = {4,5,6,7}
# result = set_a.union(set_b) #метод
# result_operator = set_a | set_b # оператор
# print(result,result_operator)
# set_a |= set_b #присвоение
# print(set_a)

#пересечение
# set_a ={1,2,3,4}
# set_b = {4,5,6,7}
# result = set_a.intersection(set_b) #метод
# result_operator = set_a & set_b # оператор
# set_a &= set_b
# print(set_a,result,result_operator)



#разность
# set_a ={1,2,3,4,5}
# set_b = {4,5,6,7,8}
# result= set_a.difference(set_b) #метод
# result_operator= set_a - set_b #оператор
# set_a -= set_b  #присваивание
# print (set_a,result,result_operator)

# симметрическая разность
set_a ={1,2,3,4}
set_b = {3,4,5,6}
result = set_a.symmetric_difference(set_b) #метод
result_operator = set_a ^ set_b
set_a ^= set_b
print(set_a,result,result_operator)


my_set = {1,2,3}
print (3 in my_set)
print(5 not in my_set)
print(len(my_set)) # длина множества
print (sum(my_set)) # сумма множеств
print (min(my_set), max(my_set)) #мин.макс число в множестве
for num in my_set:
    print(num)