def func(length,direction,symbol):
    if direction == "горизонтальная":
        print(symbol*length)
    elif direction == "вертикальная":
        for i in range (length):
            print(symbol)
func(5,"горизонтальная","*")
func(5,"вертикальная","*")
