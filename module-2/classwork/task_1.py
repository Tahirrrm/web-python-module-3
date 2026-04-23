str = input ("Введите слово")
d= {}
for word in str:
    d.setdefault (word,0)
    d[word] += 1
print(d)
for key, value in d.items():
    print (f"{key}={value}")