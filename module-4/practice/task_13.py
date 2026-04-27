import random
nums = [random.randint (-50,50) for _ in range (100)]
def min_innterval_pos(i,best_position=0, best_sum = None):

    if i +10 >len(nums):
        return best_position
    summa = sum (nums [i:i+10])
    if best_sum == None or summa < best_sum:
        best_sum = summa
        best_position = i

    return min_innterval_pos(i+1,best_position,best_sum)
best_position= min_innterval_pos(0)

print(f"минимальная последовательность:{nums [best_position:best_position + 10]}")
