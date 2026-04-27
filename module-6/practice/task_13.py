employees = {}


def add_employee():
    name = input("Введите ФИО: ")
    if not name:
        print("Ошибка: ФИО не может быть пустым!")
        return
    phone = input("Телефон: ")
    email = input("Email: ")
    post = input("Должность: ")
    cabinet = input("Кабинет: ")
    skype = input("Skype: ")
    employees[name] = {
        'phone': phone,
        'email': email,
        'post': post,
        'cabinet':cabinet,
        'skype': skype
    }
    print(f"Сотрудник {name} добавлен.")


def delete_employee():
    name = input("Введите ФИО для удаления: ")
    if name in employees:
        del employees[name]
        print(f"Сотрудник {name} удалён.")
    else:
        print("Сотрудник не найден.")


def search_employee():
    name = input("Введите ФИО для поиска: ")
    if name in employees:
        data = employees[name]
        print(f"\n--- {name} ---")
        print(f"Телефон: {data['phone']}")
        print(f"Email: {data['email']}")
        print(f"Должность: {data['post']}")
        print(f"Кабинет: {data['cabinet']}")
        print(f"Skype: {data['skype']}")
    else:
        print("Сотрудник не найден.")


def replace_employee():
    name = input("Введите ФИО для изменения: ")
    if name not in employees:
        print("Сотрудник не найден.")
        return
        print("Оставьте поле пустым, если не хотите его менять.")
    new_phone = input(f"Новый телефон ({employees[name]['phone']}): ")
    new_email = input(f"Новый email ({employees[name]['email']}): ")
    new_post = input(f"Новая должность ({employees[name]['post']}): ")
    new_cabinet = input(f"Новый кабинет ({employees[name]['cabinet']}): ")
    new_skype = input(f"Новый Skype ({employees[name]['skype']}): ")
    if new_phone:
        employees[name]['phone'] = new_phone
    if new_email:
        employees[name]['email'] = new_email
    if new_post:
        employees[name]['position'] = new_post
    if new_cabinet:
        employees[name]['office'] = new_cabinet
    if new_skype:
        employees[name]['skype'] = new_skype 
    print(f"Данные сотрудника {name} обновлены.")


def show_all():
    if not employees:
        print("Список сотрудников пуст.")
        return
    print("\nВсе сотрудники:")
    for name, data in employees.items():
        print(f"\n{name}")
        print(f"  Телефон: {data['phone']}")
        print(f"  Email: {data['email']}")
        print(f"  Должность: {data['post']}")
        print(f"  Кабинет: {data['cabinet']}")
        print(f"  Skype: {data['skype']}")
        
while True:
    print("\n--- Фирма ---")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Найти сотрудника")
    print("4. Изменить данные")
    print("5. Показать всех")
    print("6. Выход")
    choice = input("\nВыберите действие (1-6): ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        delete_employee()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        replace_employee()
    elif choice == '5':
        show_all()
    elif choice == '6':
        break
    else:
        print("Выберите действие (1-6): ")