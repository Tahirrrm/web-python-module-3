players_dict = {}


def add_player():
    full_name= input ("Введите ФИО баскетболиста: ")
    if not full_name:
        print ("Ошибка")
        return
    try:
        height = int(input("Введите рост баскетболиста в (см): "))
        if height <100 or height >280:
            print("Ошибка")
            return
        players_dict[full_name]=height
        print (f"Добавлен игрок: {full_name} - {height} см")
    except ValueError:
        print("Ошибка")


def delete_player():
    name= input ("Введите ФИО для удаления:")
    if name in players_dict:
        del players_dict[name]
        print (f"Удален игрок: {name}")
    else:
        print ("Игрока нет в списке")


def search_player():
    name= input ("Введите ФИО для поиска:")
    if name in players_dict:
        print (f"{name} - {players_dict[name]} см")
    else:
        print("Нет в списке")


def make_changes():
    name = input ("Введите ФИО игрока для изменения: ")
    if name not in players_dict:
        print ("Игрока нет в списке")
        return
    try:
        new_height= int(input("Введите новый рост(см): "))
        if new_height <100 or new_height> 280:
            print("Ошибка")
            return
        players_dict[name]=new_height
        print(f"Обновлено: {name} - {new_height} см")
    except ValueError:
        print("Ошибка")


def all_players():
    if not players_dict:
        print("Нет игроков")
        return
    print("Все баскетболисты:")
    for name,height in players_dict.items():
        print(f"{name} - {height} см")
        
while True:
    print("\n1.Добавить" )
    print("2.Удалить" )
    print("3.Найти" )
    print("4.Изменить рост")
    print("5.Показать всех")
    print("6.Выход" )
    choice=input("Выберите действие (1-6):")
    if choice == "1":
        add_player()
    elif choice == "2":
        delete_player()
    elif choice == "3":
        search_player()
    elif choice == "4":
        make_changes()
    elif choice == "5":
        all_players()
    elif choice == "6":
        break
    else:
        print("Введите от 1 до 6")




    
        


        