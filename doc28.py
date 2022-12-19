'''Q28.Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
Sample output:
{1: {2: {3: {4: {}}}}}
'''
d=[1, 2, 3, 4,5]
a=b={}
for i in d:
    b[i]={}
    b=b[i]
print(a)






        


