# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
#  Количество символов;
#  Количество строк;
#  Количество гласных букв;
#  Количество согласных букв;
#  Количество цифр.

def statistics(source_file, new_file):
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    consonants = set('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
  
    with open(source_file, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            char_count += len(line)     
            for char in line:
                if char.isdigit():
                    digit_count += 1
                elif char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1
        
    with open(new_file, 'w', encoding='utf-8') as file:
        file.write("СТАТИСТИКА ФАЙЛА: \n")
        file.write(f"Количество символов: {char_count}\n")
        file.write(f"Количество строк: {line_count}\n")
        file.write(f"Количество гласных букв: {vowel_count}\n")
        file.write(f"Количество согласных букв: {consonant_count}\n")
        file.write(f"Количество цифр: {digit_count}\n")
        
        print(f"Анализ завершён. Статистика записана в файл: {new_file}")
        

statistics('source_file.txt', 'new_file.txt')