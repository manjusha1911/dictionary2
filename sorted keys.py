mydict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=sorted(mydict.keys())
dict={}
for i in s:
    dict[i]=mydict[i]
print(dict)