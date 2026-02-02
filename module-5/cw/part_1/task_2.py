def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # [5,2,0,1]
        # [2,5,0,1] 1 итерация
        # [2,5,5,1] 2 итерация
        # j = 1
        # arr[j] = 5
        # j = 0 
        # 2,0,5,1
        while j >=0 and arr[j] > key:
            
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
print(insertion_sort([5,2,0,1]))

