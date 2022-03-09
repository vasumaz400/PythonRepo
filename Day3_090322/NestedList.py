lst = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#Expected output lst1 = [1,2,3,4,5,6,7,8,9,10,11,12]

lst1 = []

for key in lst:
    lst1.extend(key)
    #lst1.append(key)
print(lst1)