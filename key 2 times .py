mydict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=sorted(mydict,key=mydict.get)
b={}
for i in s:
    b[i]=(i,mydict[i])
print(b)