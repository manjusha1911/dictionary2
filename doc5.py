'''Q5.
Write a Python program to sort (ascending and descending) a dictionary by value.
Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
'''

# mydict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s=sorted(mydict.values())
# dict={}
# for i in s:
#     dict[i]=mydict[i]
# print(dict)

# ascending order :

# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s=sorted(a,key=a.get)
# b=[]
# for i in s:
#     l=(i,a[i])
#     b.append(l)
# print(dict(b))


# descending order:
# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# p=sorted(d.values())
# a={}
# for i in reversed(p):
#     for j in reversed(d.keys()):
#         if d[j]==i:
#             a[j]=i                                                                                                                                                                                                                                                                                                                                                                                                                                         
# print(a)

d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=sorted(d.values())
b={}
for i in reversed (s):
    for j in reversed (d.keys()):
        if d[j]==i:
            b[j]=i
print(b)





