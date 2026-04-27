numbers=(222,11,2,4,5555,6,7,8,9,22,11111)
result= {}
for i in numbers:
    digits_length= len(str(abs(i)))
    result[digits_length] = result.setdefault(digits_length,0) +1
for item in sorted(result):
    print(item,result[item])

