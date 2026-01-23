def func(num):
    numbers= [int(d) for d in str(num)]
    a= sum(numbers[:3])
    b= sum(numbers[3:])
    if a == b:
        print("счастливое")
    else:
        print("несчастливое")
func(123420)

   