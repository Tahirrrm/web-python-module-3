# Дан текстовый файл. Найти длину самой длинной
# строки

def find_longest_line_length(source_file_3):

    max_length = 0
    with open(source_file_3, 'r', encoding='utf-8') as file:
        for line in file:
            line_length = len(line.rstrip('\n')) 
            if line_length > max_length:
                 max_length = line_length
    return max_length
 
result = find_longest_line_length('source_file_3.txt')
if result is not None:
    print(f"Длина самой длинной строки: {result}")