ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

list_of_ids = []
for index in ids.values():
       for x in index:
              list_of_ids.append(x)

set_of_ids = set(list_of_ids)
filtered_list_of_ids = list(set_of_ids)
print(filtered_list_of_ids)
