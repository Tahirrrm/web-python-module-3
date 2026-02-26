# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

def compare_files(file_1, file_2):

    with open(file_1, 'r', encoding='utf-8') as fl1:
        lines1 = [line.rstrip() for line in fl1]
        
    with open(file_2, 'r', encoding='utf-8') as fl2:
        lines2 = [line.rstrip() for line in fl2]
    if lines1 == lines2:
        print("Файлы идентичны")
        return

    print("Файлы различаются. Несовпадающие строки:")
    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):   
        line1 = lines1[i] if i < len(lines1) else None
        line2 = lines2[i] if i < len(lines2) else None
        if line1 != line2:
            print(f"Строка {i + 1}:")
            print(f"  Файл 1: {line1 if line1 is not None else '[отсутствует]'}")
            print(f"  Файл 2: {line2 if line2 is not None else '[отсутствует]'}")
compare_files('file_1.txt', 'file_2.txt')