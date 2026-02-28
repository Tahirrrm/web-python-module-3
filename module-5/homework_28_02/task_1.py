# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.


employees = [] 
source_file = "source_file_6.txt" 


def source_file_load():

    with open(source_file, 'r', encoding='utf-8') as f:
        for line in f:
            index = line.strip().split(';')
            if len(index) == 6:
                employees.append({
                    'surname': index[0],
                    'name': index[1],
                    'age': int(index[2]),
                    'position': index[3],
                    'phone':(index[4]),
                    'e-mail':index[5]
            })
        print("Данные загружены")


def save_file():

    with open(source_file, 'w', encoding='utf-8') as f:
        for emp in employees:
            f.write(f"{emp['surname']};{emp['name']};{emp['age']};{emp['position']};{emp['phone']};{emp['e-mail']}\n")
    print("Данные сохранены")


def add_employee():
 
    emp = {
        'surname': input("Фамилия: "),
        'name': input("Имя: "),
        'age': int(input("Возраст: ")),
        'position': input("Должность: "),
        'phone': input("Телефон: "),
        'e-mail': input("Электронная почта: ")
    }
    employees.append(emp)
    print("Сотрудник добавлен!")


def edit_employee():

    surname = input("Введите фамилию для редактирования: ")
    for emp in employees:
        if emp['surname'].lower() == surname.lower():
            emp['name'] = input(f"Новое имя ({emp['name']}): ") or emp['name']
            emp['age'] = int(input(f"Новый возраст ({emp['age']}): ") or emp['age'])
            emp['position'] = input(f"Новая должность ({emp['position']}): ") or emp['position']
            emp['phone'] = input(f"Новый телефон ({emp['phone']}): ") or emp['phone']
            emp['e-mail'] = input(f"Новая почта ({emp['e-mail']}): ") or emp['e-mail']
            print("Данные обновлены!")
            return
    print("Сотрудник не найден!")


def delete_employee():
 
    surname = input("Введите фамилию для удаления: ")
    for i, emp in enumerate(employees):
        if emp['surname'].lower() == surname.lower():
            del employees[i]
            print("Сотрудник удалён!")
            return
    print("Сотрудник не найден!")


def search_by_surname():

    surname = input("Введите фамилию для поиска: ").lower()
    found = [emp for emp in employees if surname in emp['surname'].lower()]
    if found:
        print(f"\nНайдено: {len(found)}")
        for emp in found:
            print(f"{emp['surname']} {emp['name']}, {emp['age']} лет, {emp['position']},{emp['phone']},{emp['e-mail']}")
        
        with open("search_results_6.txt", 'w', encoding='utf-8') as f:
            for emp in found:
                f.write(f"{emp['surname']};{emp['name']};{emp['age']};{emp['position']}\n")
        print("Результаты поиска сохранены в search_results_6.txt")
    else:
        print("Не найдено!")


def filter_by_age():
    age = int(input("Введите возраст: "))
    filtered = [emp for emp in employees if emp['age'] == age]
    if filtered:
        print(f"\nСотрудники {age} лет: {len(filtered)}")
        for emp in filtered:
            print(f"{emp['surname']} {emp['name']}, {emp['position']},{emp['phone']},{emp['e-mail']}")
     
        with open(f"age_filtered_6.txt", 'w', encoding='utf-8') as f:
            for emp in filtered:
                f.write(f"{emp['surname']};{emp['name']};{emp['age']};{emp['position']},{emp['phone']},{emp['e-mail']}\n")
        print(f"Результаты сохранены в age_filtered_6.txt")
    else:
        print(f"Нет сотрудников {age} лет")


def filter_by_first_letter():

    letter = input("Введите первую букву фамилии: ").lower()
    filtered = [emp for emp in employees if emp['surname'].lower().startswith(letter)]
    if filtered:
        print(f"\nНа букву '{letter}': {len(filtered)}")
        for emp in filtered:
            print(f"{emp['surname']} {emp['name']}, {emp['age']} лет, {emp['position']},{emp['phone']},{emp['e-mail']}")
   
        with open(f"letter_filtered_6.txt", 'w', encoding='utf-8') as f:
            for emp in filtered:
                f.write(f"{emp['surname']};{emp['name']};{emp['age']};{emp['position']},{emp['phone']},{emp['e-mail']}\n")
        print(f"Результаты сохранены в letter_filtered_6.txt")
    else:
        print(f"Нет фамилий на букву '{letter}'")


def show_all():

    if employees:
        print("\nВсе сотрудники:")
        for i, emp in enumerate(employees, 1):
            print(f"{i}. {emp['surname']} {emp['name']}, {emp['age']} лет, {emp['position']},{emp['phone']},{emp['e-mail']}")
    else:
        print("Список пуст!")

print("-" * 30)
print("      | «Сотрудники» |")
print("-" * 30)
source_file_load()

while True:
    print("\nМеню:")
    print("1. Добавить сотрудника")
    print("2. Редактировать сотрудника")
    print("3. Удалить сотрудника")
    print("4. Поиск по фамилии")
    print("5. Фильтрация по возрасту")
    print("6. Фильтрация по букве фамилии")
    print("7. Показать всех")
    print("8. Сохранить данные")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        edit_employee()
    elif choice == '3':
        delete_employee()
    elif choice == '4':
        search_by_surname()
    elif choice == '5':
        filter_by_age()
    elif choice == '6':
        filter_by_first_letter()
    elif choice == '7':
        show_all()
    elif choice == '8':
        save_file()
    elif choice == '0':
        save_file()
        print("До свидания!")
        break
    else:
        print("Неверный выбор!")