def process_list(list):
    if not list:
        return []
  
    avg = sum(list) / len(list)
    n = len(list)
    
    if avg > 0:
      
        split_index = (2 * n) // 3
        sorted_part = sorted(list[:split_index])
        remaining_part = list[split_index:][::-1]
    else:
        split_index = n // 3
        sorted_part = sorted(list[:split_index])
        remaining_part = list[split_index:][::-1]
    
    return sorted_part + remaining_part

test_cases = [
    [10,5,6,1,9,7,2,8,4,3],  
    [-6,-4,5,-1,-15,3],         
    [],                                  
    [35],                             
    [0, 0, 0]                      
]

for i, test in enumerate(test_cases, 1):
    result = process_list(test)
    avg = sum(test) / len(test) if test else 0
    print(f"Тест {i}: {test} → {result} (среднее: {avg:.2f})")