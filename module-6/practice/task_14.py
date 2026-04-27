book_collection = {}


def add_book():
    book_title = input("Введите название книги: ")
    if book_title in book_collection:
        print(f"Книга с названием '{book_title}' уже есть в коллекции")
        return
    author = input("Введите автора книги: ")
    genre = input("Введите жанр книги: ")
    release_year = input("Введите год выпуска книги: ")
    pages = input("Введите количество страниц книги: ")
    publisher = input("Введите издательство книги: ")
    book_collection[book_title] = {
        "author": author,
        "genre": genre,
        "release_year": release_year,
        "pages": pages,
        "publisher": publisher
    }
    print(f"Книга '{book_title}' успешно добавлена в коллекцию!\n")


def delete_book():
    print("Удаление книги")
    title = input("Введите название книги для удаления: ")
    if title in book_collection:
        del book_collection[title]
        print(f"Книга '{title}' удалена из коллекции!\n")
    else:
        print(f"Книга '{title}' не найдена в коллекции!\n")


def search_book():
    print("Поиск книги")
    title = input("Введите название книги для поиска: ")
    if title in book_collection:
        book = book_collection[title]
        print(f"\nКнига '{title}' найдена:")
        print(f"  Автор: {book['author']}")
        print(f"  Жанр: {book['genre']}")
        print(f"  Год выпуска: {book['release_year']}")
        print(f"  Количество страниц: {book['pages']}")
        print(f"  Издательство: {book['publisher']}\n")
    else:
        print(f"Книга '{title}' не найдена в коллекции!\n")


def replace_book():
    print("Замена информации о книге")
    title = input("Введите название книги для замены: ")
    if title in book_collection:
        print(f"Текущие данные книги '{title}':")
        current_book = book_collection[title]
        print(f"  Автор: {current_book['author']}")
        print(f"  Жанр: {current_book['genre']}")
        print(f"  Год выпуска: {current_book['release_year']}")
        print(f"  Количество страниц: {current_book['pages']}")
        print(f"  Издательство: {current_book['publisher']}")
        print("\nВведите новые данные (если не нужно менять — оставьте поле пустым):")
        new_author = input("Новый автор: ")
        new_genre = input("Новый жанр: ")
        new_release_year = input("Новый год выпуска: ")
        new_pages = input("Новое количество страниц: ")
        new_publisher = input("Новое издательство: ")
        if new_author:
            book_collection[title]['author'] = new_author
        if new_genre:
            book_collection[title]['genre'] = new_genre
        if new_release_year:
            book_collection[title]['year'] = new_release_year
        if new_pages:
            book_collection[title]['pages'] = new_pages
        if new_publisher:
            book_collection[title]['publisher'] = new_publisher
        print(f"Информация о книге '{title}' обновлена!\n")
    else:
        print(f"Книга '{title}' не найдена в коллекции!\n")


def print_books():
    print("\n--- Список книг в коллекции ---")
    if not book_collection:
        print("Коллекция пуста.\n")
        return
    for title, book in book_collection.items():
        print(f"\nНазвание: {title}")
        print(f"  Автор: {book['author']}")
        print(f"  Жанр: {book['genre']}")
        print(f"  Год выпуска: {book['release_year']}")
        print(f"  Количество страниц: {book['pages']}")
        print(f"  Издательство: {book['publisher']}")
    print()  

while True:
    print("«КНИЖНАЯ КОЛЛЕКЦИЯ»")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Заменить информацию о книге")
    print("5. Вывести список всех книг")
    print("6. Выход")
   

    try:
        choice = int(input("Выберите пункт меню (1–6): "))
    except ValueError:
        print("Пожалуйста, введите число от 1 до 6.\n")
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        delete_book()
    elif choice == 3:
        search_book()
    elif choice == 4:
        replace_book()
    elif choice == 5:
        print_books()
    elif choice == 6:
        break
    else:
        print("Пожалуйста, введите число от 1 до 6.\n")