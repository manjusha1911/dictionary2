'''Q38.. Write a Python program to drop empty Items from a given Dictionary. 
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}
'''


dict={'c1':'red','c2':'green','c3':None}
new_dict={}
for i,j in dict.items():
    if j!=None:
        new_dict[i]=j
print(new_dict)