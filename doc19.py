# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# print(dic)


# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# my_dict={}
# for i in dic:
#     if i not in my_dict:
#         my_dict[i]=dic[i]
# print(my_dict)


s={'id1' :
{'name': ['Sara'], 
'class': ['V'], 
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['David'], 
'class': ['V'], 
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'], 
'class': ['V'], 
'subject_integration': ['english, math, science']
},
'id4':
{'name': ['Surya'], 
'class': ['V'], 
'subject_integration': ['english, math, science']
},}
b= {}
for key,value in s.items():
    if value not in b.values():
        b[key] = value
print(b)

# temp = []
# res = dict()
# for key, val in s.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
  
# printing result 
# print("The dictionary after values removal : " + str(res)) 