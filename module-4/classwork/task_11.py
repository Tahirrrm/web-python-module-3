def  func(n):
     if n == 0:
        return ""
     return "*" + func(n-1)
print (func(5))