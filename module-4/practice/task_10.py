def power(a,b):
    if a==b:
        return a
    return a + power(a+1,b)
print(power(5,10))