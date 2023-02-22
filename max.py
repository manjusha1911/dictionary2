dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 108, 'i': 100}
val=dict.values()
l=list(val)
m=l[0]
i=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print("maximum value:",m)
