dct = {"1":["a","b"],"2":["c","d"]}

"""
ac
ad
bc
bd
"""
lst = list(dct.values())
#print(lst)

for temp in lst[0]:
    for temp2 in lst[1]:
        print(temp + temp2)