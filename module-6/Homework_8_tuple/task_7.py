# """
# ЗАДАЧА: Анализ покупок в магазине

# Дан список покупок. Каждая покупка содержит:
# - user      : имя покупателя (строка)
# - items     : список купленных товаров (список строк)
# - price     : общая стоимость покупки (целое число)
# - timestamp : время покупки (целое число)

# НЕОБХОДИМО РЕАЛИЗОВАТЬ:

# 1. Посчитать общее количество покупок каждого пользователя.

# 2. Посчитать общую сумму потраченных денег каждым пользователем.

# 3. Для каждого пользователя:
#    - найти множество уникальных товаров, которые он покупал
#    - посчитать общее количество купленных товаров (с учётом повторов)

# 4. Найти товар, который покупали чаще всего
#    (если таких несколько — можно вернуть любой).

# 5. Найти пользователя, который:
#    - потратил больше всего денег
#    - купил больше всего товаров
#    (это могут быть разные пользователи)

# 6. Для каждого пользователя найти самый большой перерыв
#    между его покупками (по timestamp).
# """

# purchases = [
#     {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
#     {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
#     {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
#     {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
#     {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
#     {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
# ]
purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

user_purchase_total = {}  
user_total_spent = {}    
user_unique_items = {}   
user_item_count = {}      
item_frequency = {}        
user_timestamps = {}    

for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    price = purchase["price"]
    timestamp = purchase["timestamp"]
    if user not in user_purchase_total:
        user_purchase_total[user] = 0
    user_purchase_total[user] += 1 
    if user not in user_total_spent:
        user_total_spent[user] = 0
    user_total_spent[user] += price 
    if user not in user_unique_items:
        user_unique_items[user] = set()
    if user not in user_item_count:
        user_item_count[user] = 0
    
    for item in items:
        user_unique_items[user].add(item)
        user_item_count[user] += 1
        if item not in item_frequency:
            item_frequency[item] = 0
        item_frequency[item] += 1
    if user not in user_timestamps:
        user_timestamps[user] = []
    user_timestamps[user].append(timestamp)

most_frequent_item = max(item_frequency.items(), key=lambda x: x[1])[0]
max_spent_user = max(user_total_spent.items(), key=lambda x: x[1])[0]
max_items_user = max(user_item_count.items(), key=lambda x: x[1])[0]

user_max_gap = {}
for user, timestamps in user_timestamps.items():
    if len(timestamps) < 2:
        user_max_gap[user] = 0 
    else:
        sorted_timestamps = sorted(timestamps)
        max_gap = max(sorted_timestamps[i] - sorted_timestamps[i-1]
                   for i in range(1, len(sorted_timestamps)))
        user_max_gap[user] = max_gap


print("\n 1) Общее количество покупок каждого пользователя:")
for user, count in user_purchase_total.items():
    print(f"  {user}: {count}")


print("\n 2) Общая сумма потраченных денег каждым пользователем:")
for user, total in user_total_spent.items():
    print(f"  {user}: {total} руб.")


print("\n 3) Информация по  каждому пользователю:")
for user in user_unique_items.keys():
    unique_items = ", ".join(user_unique_items[user])
    total_items = user_item_count[user]
    print(f"  {user}:")
    print(f"   - Купленные товары: {unique_items}")
    print(f"   - Общее количество купленных товаров: {total_items}")


print(f"\n 4) Самый часто покупаемый товар: {most_frequent_item}")


print(f"\n 5) Кто больше всех потратил:")
print(f"  Больше всего потратил: {max_spent_user} ({user_total_spent[max_spent_user]} руб.)")
print(f"  Больше всего товаров купил: {max_items_user} ({user_item_count[max_items_user]} шт.)")


print("\n 6) Максимальный перерыв между покупками для каждого пользователя:")
for user, gap in user_max_gap.items():
    print(f"  {user}: {gap} минут")