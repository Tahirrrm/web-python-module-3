import random
tasks = []
for i in range(10):
    tasks.append({
        "id" : f"t_{i}",
        "assignee": random.choice(["ivan","olga","petr","anna","oleg"]),
        "status" : random.choice([ "in_progress","blocked","in_review","waiting_vendor"]),
        "days_in_status": random.randint(0,10)
    })

asignees=set()
for j in tasks:
        if (j["status"] == "in_progress" 
            and j["days_in_status"] > 7):
            asignees.add (j["assignee"])
print(asignees)

status_asignees={}
for task in tasks:
    status=task["status"]
    asignees= task["assignee"]
    if status not in status_asignees:
        status_asignees [status]= set()
    status_asignees[status].add(asignees)
result={}   
for status in status_asignees:
    if len (status_asignees[status]) == 1:
        result[status]= list(status_asignees[status]) [0]
print(result)

max_debt = 0
assignee = 0

for task in tasks:
     if task["status"] == "in progress" or task["status"] == "blocked":
        if task ["days_in_status"] > max_debt:
            max_debt = task["days_in_status"]
            assignee = task["assignee"]
print(max_debt,assignee)


        



