lst = [[1,3],[5,7],[1,3],[13,15,17],[5,7],[9,11]]

#Expected dict1 = {(1:3):2,(5:7):2,(13,15,17):1,(9,11):1}

dict1 = {}

for element in lst:
    cnt = lst.count(element)
    temp = tuple(element)
    dict1[temp] = cnt
print(dict1)