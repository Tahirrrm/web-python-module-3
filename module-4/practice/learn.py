# def func_1():
#     print("функция")
# def func_2():
#     return "привет func2"
# def func_3():
#     pass
# func_1()
# print(func_2())

# def func_4(name,age,city):
#     print(f"{name}-{age}-{city}")
# func_4("Павел","24","Чебоксары")
# def func_6(*args):
#     total = 0
#     for num in args:
#         total += num
#         print(total)
#     print(args)
# func_6(1,2,3,4,5)

# def func_7 (**kwargs):
#     print(kwargs)
# func_7 (name=1,age =2)

# def  func_8(num1,num2,*args,**kwargs):
#     print(f"{num1},{num2}")
#     print(args)
#     print(kwargs)
# func_8(1,2,3,4,5, name=1)


# def func_9 (obj):
#     print(obj)
# func_9 ({"a":1,"b":2})

# def func_1():
#     result = []
#     for i in range (5):
#         result.append(i)
#     return result
# print (func_1())

# def func_2():
#   for i in range (5):
#    yield i
# gen =  func_2 ()
# print(gen)
# print(next(gen))
# print(next(gen))

# for i in func_2():
#    print(i)


def factorial(n=9):
    # базовый случай
    if n <=1:
        return 1
    # рукурсивный шаг
    # 9! = 9*8*7*6*5 ... 
    return n *  factorial(n-1)
print(factorial(9))