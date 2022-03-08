lst1 = [{},{},{},{},{},{}]
is_emt = True

for temp in lst1:
    if temp:
        is_emt = False
        break

if is_emt == True:
    print("Dict is empty")
else:
    print("Dict is not empty")
