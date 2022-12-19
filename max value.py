dict={'a':189,'b':10,'c':2,'d':7}
value=dict.values()
l=list(value)
i=0
min=1000
max=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    if  l[i]<min:
        min=l[i]
    i+=1
print("max:",max) 
print("min:",min)  