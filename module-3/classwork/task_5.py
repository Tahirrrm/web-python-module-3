str= ("fghgf234234")
letters = 0
digits = 0
for x in str :
    if x.isalpha():
        letters +=1
    elif x.isdigit():
        digits+=1
print (letters,digits)



