# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

def repeated_count(source_file_4, repeated_word):

    count = 0
    
    with open(source_file_4, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()  
            count += words.count(repeated_word)
    return count
  
word = input("Введите слово для поиска: ")
result = repeated_count('source_file_4.txt', word)
if result is not None:
    print(f"Слово '{word}' встречается {result} раз(а)")