# text = "  o"
# print (text.upper())
# print (text.lower())
# print (text.capitalize())
# print(text.swapcase())
# print (text.find("p"))  #поиск элемента если не найдет то вернет -1 
# print(text.replace("Hello", "Hi", 2)) #заменяет два найденых элемента
# print("Только цифры:", text.isdigit())
# print("Только буквы:", text.isalpha())
# print ("Только буквы и цифры:", text.isalnum())
# print ("Пробелы: ", text.isspace())
# print ("заглавные :" ,text.isupper())
# print ("прописные :" ,text.islower())


# text  =" яблоко, апельсин, банан"
# text = "row_1\nrow_2\nrow_3"
# #очистка
# # print(text.strip("*")) #очистка левой  и правой части
# # print(text.lstrip()) #очистка левой части
# # print(text.rstrip()) # очистка правой части
# sl= text.splitlines()
# print(sl)
# f = text.split(",") #если пусто то разбиение по пробелам

# u = ", " .join(f)  #обьединение элментов в строку
# print (f,u)

# tuple_1 = (1,2,3)
# tuple_2 = tuple ([1,2,3])  #создает кортеж
# tuple_3 = 1,2,3
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

# tuple_1 = tuple(range (0,11))
# print (tuple_1[0])
# print (tuple_1[2:5])

# num1, *other,last_el = tuple (range (0,11))
# print(num1, other, last_el)

# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print (result)

# pattern = ("a", "b")
# repeated = pattern * 2
# print (repeated)
# f = ("apple", "banana")
# print ("apple" in f)

#Методы кортежей
numbers = (1,2,3,2,4,5,2)
# print (numbers.count (2))
# print (numbers.index (2))

num_tuple = tuple(range (0,5))
for index, num in enumerate(num_tuple):
    print(index,num)