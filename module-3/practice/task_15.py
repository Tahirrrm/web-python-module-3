text= "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore etdolore magna aliqua.ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex eacommodo consequat.duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur.Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
print(text)
reserved_words = (input  ("Выберите слова для выделения в верхний регистр : "))
reserved_words=reserved_words.split()
for word in reserved_words:
    text = text.replace(word, word.upper())
print(text)
