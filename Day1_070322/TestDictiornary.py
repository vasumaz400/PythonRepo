dist1 = {"name":"Vasu","age":"26","city":"pune"}

#print(type(dist1))

print(dist1["name"])

print(list(dist1.keys()))
print(list(dist1.values()))

dist1["name"] = "Anjali"

print(dist1)

for key in dist1.keys():
    print(key,dist1[key])

tup1 = (1,2,3,4,5,2,2,2,2,4,4,4)

dist2 = {}
for temp in tup1:
    dist2[temp] = tup1.count(temp)
print(dist2)