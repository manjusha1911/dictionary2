a={1: 2, 3: 4,5:6, 4: 3, 2: 1, 0: 0}
sort=sorted(a.keys())
b=[]
for i in sort:
    l=i,a[i]
    b.append(l)
    b[i]=a[i]
print(b)
