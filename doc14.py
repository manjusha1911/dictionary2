'''Q14.Write a Python program to multiply all the items in a dictionary.
'''
# d={'value1': 2,'value2': 3,'value3': 4,'value4': 5,'value5': 6}
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a=1
for i in d:
    a*=d[i]
print(a)