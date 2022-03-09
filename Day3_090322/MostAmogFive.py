dict1 = {"item1": 45.50,"item2": 35,"item3": 41.30,"item4": 55,"item5": 24}
# Sorted_List = [55, 45.5, 41.3, 35, 24]
lst = list(dict1.values())
lst.sort(reverse=True)
print(lst)
sorted_tup = sorted(dict1.items(),key=lambda item: item[1],reverse=True)
print(sorted_tup)

for key in range(3):
    for key2 in dict1:
        if lst[key] == dict1[key2]:
            print(key2,lst[key])

