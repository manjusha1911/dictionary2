
'''Q29.Write a Python program to sort a list alphabetically in a dictionary.
'''

# d = {'b': ["c", "a", "b"], 'c': ["z", "x", "y"], 'a': ["o", "n", "m"]}
# for i, j in d.items():
#     sd={i:sorted(j)}
#     print(sd)
    
    
    
    
    
    
    
    
d = {'b': ["c", "a", "b"], 'c': ["z", "x", "y"], 'a': ["o", "n", "m"]}
for i,j in  d.items():
    sd={i:sorted(j)}
    print(sd)