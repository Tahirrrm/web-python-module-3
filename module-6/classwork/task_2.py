fruits = ("яблоко","банан","апельсин","банан","бананамама","банананана")
fruit_count= input ("Введите название фрукта")
counts= 0
for i in (fruits):
    if fruit_count in i:
        counts+=1
print(counts) 