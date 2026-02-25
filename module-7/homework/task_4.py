# Написать программу «справочник».Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# Отсортировать по идентификационным кодам;
# Отсортировать по номерам телефона;
# Вывести список пользователей с кодами и телефонами;
# Выход.

def sort_by_id(id, phones):
    n = len(id)
    index = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if id[index[i]] > id[index[j]]:
                index[i], index[j] = index[j], index[i]
    sorted_id = [id[i] for i in index]
    sorted_phones = [phones[i] for i in index] 
    return sorted_id, sorted_phones


def sort_by_phones(id, phones):
    n = len(phones)
    index = list(range(n))
  
    for i in range(n):
        for j in range(i + 1, n):
            if phones[index[i]] > phones[index[j]]:
                index[i], index[j] = index[j], index[i]
    sorted_id = [id[i] for i in index]
    sorted_phones = [phones[i] for i in index]  
    return sorted_id, sorted_phones


def print_users(id, phones):
    if not id:
        print("Ошибка.\n")
        return
    
    print("\n" + "=" * 50)
    print(f"{'ID':<10} {'Телефон':<15}")
    print("-" * 50)
    for i in range(len(id)):
        print(f"{id[i]:<10} {phones[i]:<15}")
    print("=" * 50 + "\n")

def main():
    id = [8352,8843,8495,8352]
    phones = [334567,776545,752233,986666,775577]
    
    print("Справочник пользователей.")
    
    while True:
        print("Меню:")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей с кодами и телефонами")
        print("4. Выход")
        
        choice = input("\nВыберите пункт меню (1-4): ").strip()
        
        if choice == '1':
            id, phones = sort_by_id(id, phones)
            print("Список отсортирован по идентификационным кодам.\n")
        
        elif choice == '2':
            id, phones = sort_by_phones(id, phones)
            print("Список отсортирован по телефонным номерам.\n")
        
        elif choice == '3':
            print_users(id, phones)
        
        elif choice == '4':
            print("Выход из программы.")
            break
        
        else:
            print("Ошибка. Пожалуйста, введите число от 1 до 4.\n")

if __name__ == "__main__":
    main()