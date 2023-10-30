import collections

group_a = {
    "Brazil": 7,
    "Mexico": 7,
    "Croatia": 3,
    "Cameroon": 0
}
group_b = {
    "Germany": 7,
    "USA": 4,
    "Portugal": 4,
    "Ghana": 1
}

groups = collections.ChainMap(group_a, group_b)
print(groups)
print(groups.maps)
print(groups.maps[0])
groups.maps[1]["Moldova"] = 10
print(groups.maps[1])
print(groups)
print(groups.get("Moldova"))
print(group_a, group_b)