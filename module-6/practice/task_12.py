dictionary = {}


def add_word():
    english = input("Введите английское слово: ")
    if not english:
        print("Ошибка")
        return
    french = input("Введите французский перевод: ")
    if not french:
        print("Ошибка")
        return
    if english in dictionary:
        print(f"Cлово {english} уже есть в словаре .")
        if input("Заменить? (да/нет): ") != 'да':
            return
    dictionary[english] = french
    print(f"добавлено {english} - {french}")


def delete_word():
    english = input("Введите английское слово для удаления: ")
    if english in dictionary:
        del dictionary[english]
        print(f"Слово {english} удалено из словаря.")
    else:
        print(f"Слово {english} не найдено в словаре.")


def search_word():
    english = input("Введите английское слово для поиска: ")
    if english in dictionary:
        print(f"{english} → {dictionary[english]}")
    else:
        print(f"Слово {english} не найдено в словаре.")


def replace_translation():
    english = input("Введите английское слово для изменения перевода: ")
    if english not in dictionary:
        print(f"Слово {english} не найдено в словаре.")
        return
    new_french = input(f"Введите новый перевод для {english}: ")
    if not new_french:
        print("Ошибка: перевод не может быть пустым.")
        return
    dictionary[english] = new_french
    print(f"Перевод для {english} обновлён: {new_french}")


def show_all():
    if not dictionary:
        print("Словарь пуст.")
        return
   
    print("\nАнгло‑французский словарь:")
    
    for eng, fr in sorted(dictionary.items()):
        print(f"{eng:20} → {fr}")

        
def main():
    print(" Англо‑французский словарь")
    while True:
        print("\nМеню:")
        print("1. Добавить слово")
        print("2. Удалить слово")
        print("3. Найти перевод")
        print("4. Изменить перевод")
        print("5. Показать весь словарь")
        print("6. Выход")
        choice = input("\nВыберите действие (1–6): ")
        if choice == '1':
            add_word()
        elif choice == '2':
            delete_word()
        elif choice == '3':
            search_word()
        elif choice == '4':
            replace_translation()
        elif choice == '5':
            show_all()
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Введите число от 1 до 6.")
if __name__ == "__main__":
    main()