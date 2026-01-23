a =(1,2,3,3,4,5,6)
b =(6,7,9,3,8,9)
c = a+b
print(a,b,c)

No_repeats=set(a+b)
print(No_repeats)

common_elements=list(set(a) & set(b))
print(common_elements)


unique_elements=list(set(a) ^ set(b)) 
print (unique_elements)

min_max = [min(a), max(a), min(b), max(b)]
print(min_max)