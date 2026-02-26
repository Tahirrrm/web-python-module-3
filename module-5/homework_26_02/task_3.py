
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

def remove_last_line(source_file_2, updated_file_2):

    with open(source_file_2, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if lines:
        lines = lines[:-1]

    with open(updated_file_2, 'w', encoding='utf-8') as file:
        file.writelines(lines)    
    print(f"Последняя строка удалена. Результат записан в файл: {updated_file_2}")
   
remove_last_line('source_file_2.txt', 'updated_file_2.txt')