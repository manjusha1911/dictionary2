'''Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
  
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
#     if i in d1:
#         d1[i]+=d2[i]
# d1.update(d2)
# print(d2)
        
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = dict(d1) 
# d3.update(d2) 
# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)



# a=["one","two","three","four","five"]
# i=0
# d={}
# while i<len(a):
#     d[i+1]=a[i]  
#     i+=1
# print(d)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
    if i in d1:
        d2[i]+=d[i]
d1.update(d2)
print(d1)