'''Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c']
'''

dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
val=dict.values()
l=list(val)
m=l[0]
m1=l[0]
i=0
while i<len(l):
    a=[]
    if l[i]>m:
        m=l[i]
    a.append(m)
    b=[]
    if l[i]<m1:
        m1=l[i]
    b.append(m1)
    i+=1
print("maximum value:",a)
print("minimum value:",b)



