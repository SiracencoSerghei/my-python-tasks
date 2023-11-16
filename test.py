users = [{'user_id': 134, 'user_name': 'Alice'},
         {'user_id': 831, 'user_name': 'Bob'},
         {'user_id': 898, 'user_name': 'Sergio'}]

print("len: ", len(users))
for user in users:
    print("User_ID: ", user['user_id'])
    print("User_Name: ", user['user_name'])
    if user['user_name'] == 'Sergio':
        user['user_name'] = 'Pietro'
        print("User_Name: ", user['user_name'])
print(users)
