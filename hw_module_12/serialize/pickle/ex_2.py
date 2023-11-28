import pickle
FILENAME = "users.dat"
users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

with open(FILENAME, "rb") as file_1:
    users_from_file = pickle.load(file_1)
    for user in users_from_file:
        print('Name: ', user[0], "\tAge: ", user[1])

