# Задача:
# Есть (employee, hours).
# Нужно:
#     - посчитать часы по каждому
#     - найти переработку (> 40)
#     - найти недоработку (< 20)

# logs = [
#     ("ivan", 8), ("ivan", 10),
#     ("olga", 20),
#     ("petr", 45),
# ]

logs = [
    ("ivan", 8), ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]
total_hours= {}

for employee, hours in logs:
    if employee not in total_hours:
        total_hours[employee] = 0  
    total_hours[employee] += hours
print(" Часы по каждому сотруднику:")
for employee, hours in total_hours.items():
    print(f"  {employee}: {hours} часов")


print("\n Сотрудники с переработкой (> 40 часов):")
overtime = False
for employee, hours in total_hours.items():
    if hours > 40:
        print(f"  {employee}: {hours} часов")
        overtime = True
if not overtime:
    print(" Нет сотрудников с переработкой")

print("\n Сотрудники с недоработкой (< 20 часов):")
underwork = False
for employee, hours in total_hours.items():
    if hours < 20:
        print(f"  {employee}: {hours} часов")
        underwork = True
if not underwork:
    print(" Нет сотрудников с недоработкой")