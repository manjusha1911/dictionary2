dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 4, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
val=dict.values()
l=list(val)
m1=l[0]
i=0
while i<len(l):
    if l[i]<m1:
        m1=l[i]
    i+=1
print("minimum value:",m1)
