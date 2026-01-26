def power(x,n):
    # базовый случай
    if n == 1:
        return x
    # рекурсивный шаг
    return x * power (x,n-1)
print(power(2,3))