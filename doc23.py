'''Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
'''


a= {'A': 67, 'B': 23, 'C': 45,
'D': 56, 'E': 122, 'F': 669}
x=list(a.values())
x.sort(reverse=True)
x=x[:3]
print(x)
for i in x:
    for j in a.keys():
        if(a[j]==i):
            print(str(j)+":"+str(a[j]))

