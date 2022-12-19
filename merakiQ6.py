# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sum=0
# for i in dict1.values():
#   for item in i:
#     sum+=1
# print(sum)

# my_dict = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# x=list(my_dict.values())
# d=dict()
# x.sort(reverse=True)
# x=x[:3]
# print(x)

# d=dict()
# for x in range(1,16): 
#     d[x]=x**2 
# print(d)

# my_dict = {
# 'a':50, 
# 'b':58,
# 'c': 56,
# 'd':40,
# 'e':100, 
# 'f':20
# }
# x=list(my_dict.keys())
# d=dict()
# x.sort(reverse=True)
# x=x[:3]
# print(x)

# a = {(1,2,3):1,(2,3):2}
# print(a[2,3])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# a = {'a':1,'b':2,'c':3}
# print(a)

fruit = {}
def addone(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')
addone('Banana')
print(len(fruit))
print(fruit)