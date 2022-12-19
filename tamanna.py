d={"a":[1,2,3],"b":[4,5,6]}
s=d.values()
l=list(s)
b=[]
l=[]
i=0
sum=0
while i<len(l):
    j=0
    while j<len(l[i]):
        sum+=(l[i][j])
        j+=1
    b.append(sum)
    i+=1
print(b)
