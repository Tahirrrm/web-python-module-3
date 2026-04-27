cars=("ford","ferrari","porshe","mersedes","bmw","ford")
cars_found=input ("Введите название ")
cars_change=input ("Введите название для замены")
new_list= list(cars)
for i in range(len(new_list)):
    if new_list[i].lower() == cars_found:
        new_list[i] = cars_change
new_cars = tuple(new_list)
print("Новый список:", new_cars)