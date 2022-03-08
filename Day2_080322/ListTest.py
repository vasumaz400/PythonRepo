#Expected Work1,Work2,Work3,Work4.

lst = [1,2,3,4]
strvar = "Work"

lst1 = []

for temp in lst:
    lst1.append(strvar + str(temp))
print(lst1)