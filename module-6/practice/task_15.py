# Задача:
# Есть (user, amount).
# Нужно:
#     - баланс по каждому
#     - пользователи с отрицательным балансом
#     - пользователи с более чем 2 операциями

payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]
balance = {}
operation_count = {}

for user, amount in payments:
    if user not in balance:
        balance[user] = 0
    if user not in operation_count:
        operation_count[user] = 0
    balance[user] += amount
    operation_count[user] += 1

print("Баланс по каждому пользователю:")
for user, bal in balance.items():
    print(f"  {user}: {bal}")


print("\nПользователи с отрицательным балансом:")
for user, bal in balance.items():
    if bal < 0:
        print(f"  {user}: {bal}")


print("\nПользователи с более чем 2 операциями:")
for user, count in operation_count.items():
    if count > 2:
        print(f"  {user}: {count} операций")