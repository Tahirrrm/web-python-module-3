# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

def change_word(source_file_5, old_word, new_word):

    with open(source_file_5, 'r', encoding='utf-8') as file:
        x = file.read()  
        y = x.replace(old_word, new_word)
        
    with open(source_file_5, 'w', encoding='utf-8') as file:
        file.write(y)
        
    print(f"Слово '{old_word}' заменено на '{new_word}' во всём файле.")
   
old_word = input("Введите слово, которое нужно заменить ")
new_word = input("Введите слово на что заменяем: ")
change_word('source_file_5.txt', old_word, new_word)