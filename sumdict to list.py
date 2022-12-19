d={"a":[1,2,3],"b":[4,5,6]}
a,b=d.keys()
l=x,y=d.values()
f=list(l)
i=0
b=[]
while i<len(f):
    j=0
    sum=0
    while j<len(f[i]):
        sum+=f[i][j]
        j+=1
    b.append(sum)
    i+=1
print(b)
    