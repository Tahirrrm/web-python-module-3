def func(num):
    digits= []
    for arr in num:
       for item_child in arr:
           digits.append(item_child)
    return digits
   
print(func([[1,2,3],[4,5],[6]]))