def student_grades(grades):
    print("Оценки студента:", grades)


def retake_exam(grades):
    try:
        index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Введите новую оценку (1-12): "))
            if 1 <= new_grade <= 12:
                grades[index] = new_grade
                print(f"Оценка под номером {index + 1} изменена на {new_grade}")
            else:
                print("Ошибка")
        else:
            print("Ошибка")
    except ValueError:
        print("Ошибка")


def check_scholarship(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print(f"Стипендия выходит, Средний балл: {average:.2f}")
    else:
        print(f"Стипендия не выходит. Средний балл: {average:.2f}")


def sort_grades(grades):
    choice = input("Сортировать по возрастанию или убыванию ? Введите:  `1` - ('по возрастанию ')  или `2` - ('по убыванию')").lower()
    if choice == '1':
        sorted_grades = sorted(grades)
        print("Оценки по возрастанию:", sorted_grades)
    elif choice == '2':
        sorted_grades = sorted(grades, reverse=True)
        print("Оценки по убыванию:", sorted_grades)
    else:
        print("Ошибка")


def main():
    print('╔' + '═' * 30 + '╗')
    print("    Программа «Успеваемость»  ")
    print('╚' + '═' * 30 + '╝')
    print("Введите 10 оценок студента (от 1 до 12):")
    
    grades = []
    for i in range(10):
        while True:
            try:
                grade = int(input(f"Оценка {i + 1}: "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Оценка должна быть от 1 до 12. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите целое число.")
  
    while True:
        print('•' * 15 + ' MENU ' + '•' * 15)
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")
        print("•"*36)
        
        choice = input("Выберите пункт меню (1-5): ")
        
        if choice == '1':
           student_grades(grades)
        elif choice == '2':
            retake_exam(grades)
        elif choice == '3':

            check_scholarship(grades)
        elif choice == '4':
            sort_grades(grades)
        elif choice == '5':
            import time
            import sys
            print("Завершение программы", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\nДо встречи!")
            
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.")

if __name__ == "__main__":
    main()


