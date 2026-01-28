network = {
    "Me" : {"Alice","Bob"},
    "Alice": {"Me","Chalie","Bob"},
    "Bob": {"Me","David","Eve"},
    "Charlie" : {"Alice"},
    "David" : {"Alice","Bob"},
    "Eva": {"Bob"}
}
user= "Me"
my_friends= network[user]
friends_of_friends= set()
for friend in my_friends:
  friends_of_friends.update(network[friend])


result_operator = user  & network
print(result_operator)