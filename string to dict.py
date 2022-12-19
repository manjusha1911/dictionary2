string = 'w3resource' 
# my_dict = {}
# for i in string:
#     my_dict[i] = my_dict.get(i, 0) + 1
# print(my_dict)


string = 'w3resource' 
i=0
d={}
while i<len(string):
    d[string[i]]=d.get(string[i],0)+1
    i+=1
print(d)