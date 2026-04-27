# Написать программу «книги». Создать два списка с данными.Один список хранит названия книг, второй -
# годы выпуска. Реализовать меню для пользователя:
# Отсортировать по названию книг;
# Отсортировать по годам выпуска;
# Вывести список книг с названиями и годами выпуска;
# Выход;


def sort_by_title(titles, years):
    n = len(titles)
    index = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if titles[index[i]] > titles[index[j]]:
                index[i], index[j] = index[j], index[i]
    sorted_titles = [titles[i] for i in index]
    sorted_years = [years[i] for i in index]
    return sorted_titles, sorted_years


def sort_by_year(titles, years):
    n = len(years)
    index = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if years[index[i]] > years[index[j]]:
                index[i], index[j] = index[j], index[i]
    sorted_titles = [titles[i] for i in index]
    sorted_years = [years[i] for i in index]
    return sorted_titles, sorted_years


def print_books(titles, years):
    if not titles:
        print("Ошибка.\n")
        return
    print("\n" + "=" * 52)
    print(f"{'Название книги':<40} {'Год выпуска':<10}")
    print("-" * 52)
    for i in range(len(titles)):
        print(f"{titles[i]:<40} {years[i]:<10}")
    print("=" * 52 + "\n")

def main():
    titles = [
        "Властелин колец",
        "Гордость и предубеждение",
        "Тёмные начала",
        "Автостопом по галактике",
        "Гарри Поттер и философский камень"
    ]
    years = [1954,  1813, 1995, 1979, 1997]
    print("Программа «Книги»")
    while True:
        print("Меню:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")
        choice = input("\nВыберите пункт меню (1-4): ").strip()
        if choice == '1':
            titles, years = sort_by_title(titles, years)
            print("Список отсортирован по названиям книг.\n")
        elif choice == '2':
            titles, years = sort_by_year(titles, years)
            print("Список отсортирован по годам выпуска.\n")
        elif choice == '3':
            print_books(titles, years)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Ошибка. Пожалуйста, введите число от 1 до 4.\n")

if __name__ == "__main__":
    main()