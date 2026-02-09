logs = [
    ("ivan","d1","login"),
    ("ivan","d1","view"),
    ("ivan","d2","login"),
    ("olga","d1","login"),
    ("petr","d2","error"),
    ("anna","d1","login"),
    ("anna","d2","view"),
]


user_actions_count= {}
user_actions = {}
user_days= {}
min_activity_day={}
for user,day,action in logs:
    user_actions_count[user]= user_actions_count.get(user,0) +1

    if user not in user_actions:
        user_actions[user] = set()
        user_actions[user].add(action)
    if user not in user_days:
        user_days[user]= set()
    user_days[user].add(day)
    error_user = set()
    
    if user not in min_activity_day:
    min_activity_day[user]= set()
    min_activity_day[user].add()

for user,actions in user_actions.items():
    if "error" in actions and "login" not in actions:
        error_user.add(user)
user_days_more_one= set()
for user,day in user_days.items():
      if len(day)  > 1 :
          user_days_more_one.add(user)
          
          
print(error_user)
print(user_actions)
print(user_actions_count)
print(user_days_more_one)

