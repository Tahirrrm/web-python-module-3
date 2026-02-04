logs = [
    ("ivan","day",1),
    ("ivan","night",23),
    ("olga","day",1),
    ("petr","night",7),
    ("anna","day",1),
    ("anna","day",1),

]
shift_hours= {}
employee_shift = {}
shift_long = {}

for log in logs:
    if log[0] not in shift_long:
        shift_long[log[1]] = 0
        shift_long[log[1]] += log[2]

    if log [1] not in shift_hours:
        shift_hours[log[1]] = 0
    shift_hours[log[1]] += log[2]

    if log [0] not in employee_shift:
        employee_shift [log[0]] = set()
    employee_shift[log[0]].add(log[1])
for employee in employee_shift:
    value= employee_shift[employee]
    if len(value)== 2:
        print(employee)
print(employee_shift)

# пункт 2
for shift in shift_hours:
    if shift_hours[shift] < 8 :
        print(f"на смене {shift} отработали меньше 8 часов")
print(shift_hours)
# пункт 3
long = []
for longs in shift_long:
    if shift_long[longs] >=12:
        long.append(longs)
print (f"на смене {long} отработали больше 12 часов")
