'''Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
# import itertools      
# d ={'1':['a','b'], '2':['c','d']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))
    
# my_dict= {'1':['a', 'b'], '2':['c', 'd'],"3":["e","f"]}
# my_list= list(my_dict.values())
# for i in my_list[0]:
#     for j in my_list[1]:
#         print(i+j)
        
        
        # for l in my_list[2]:
        #     print(i+j+l)
        
a= {'1':['a', 'b'], '2':['c', 'd'],"3":["e","f"]}
l=list(a.values())
for i in l[0]:
    for j in l[1]:
        print(i+j)