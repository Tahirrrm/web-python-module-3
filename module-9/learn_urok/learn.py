# class Stack:
#     def __init__(self):
#         self.__stackList = []
#     def push(self, val):
#         self.__stackList.append(val)
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
# stackObject1 = Stack()
# stackObject2 = Stack()
# stackObject1.push(3)
# stackObject2.push(stackObject1.pop())
# print(stackObject2.pop())


# class Stack:
#     def __init__(self):
#         self.__stackList = []
#     def push(self, val):
#         self.__stackList.append(val)
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
# littleStack = Stack()
# anotherStack = Stack()
# funnyStack = Stack()
# littleStack.push(1)

# anotherStack.push(littleStack.pop() + 1)
# funnyStack.push(anotherStack.pop() - 2)

# print(funnyStack.pop())

# class Stack:
#     def __init__(self):
#         self.__stackList = []

#     def push(self, val):
#         self.__stackList.append(val)

#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val



# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def getSum(self):
#         return self.__sum

#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)

#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val



# # Тестирование
# stackObject = AddingStack()
# for i in range(5):
#     stackObject.push(i)
# print(stackObject.getSum())  # Вывод: 10

# for i in range(5):
#     print(stackObject.pop())  # Вывод: 4, 3, 2, 1, 0

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val
#     def setSecond(self, val):
#         self.second = val
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject2.setSecond(3)
# exampleObject3 = ExampleClass(4)
# exampleObject3.third = 5
# print(exampleObject1.__dict__)
# print(exampleObject2.__dict__)
# print(exampleObject3.__dict__)

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#     def setSecond(self, val = 2):
#         self.__second = val
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject2.setSecond(3)
# exampleObject3 = ExampleClass(4)
# exampleObject3.__third = 5
# print(exampleObject1._ExampleClass__first)
# print(exampleObject1.__dict__)
# print(exampleObject2.__dict__)
# print(exampleObject3.__dict__)

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
# print(exampleObject1.__dict__, exampleObject1.counter)
# print(exampleObject2.__dict__, exampleObject2.counter)
# print(exampleObject3.__dict__, exampleObject3.counter)

# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
# print(exampleObject1.__dict__,
# exampleObject1._ExampleClass__counter)
# print(exampleObject2.__dict__,
# exampleObject2._ExampleClass__counter)
# print(exampleObject3.__dict__,
# exampleObject3._ExampleClass__counter)

# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val
# print(ExampleClass.__dict__)
# exampleObject = ExampleClass(2)
# print(ExampleClass.__dict__)
# print(exampleObject.__dict__)

# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2
#     def method(self):
#         pass
#     def __hidden(self):
#         pass
# obj = Classy()
# print(obj.__dict__)
# print(Classy.__dict__)
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' in ' + self.galaxy
sun = Star("Sun", "Milky Way")
print(sun)