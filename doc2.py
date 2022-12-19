'''Q2. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
'''
        

# name="w3resource"
# i=0
# b={}
# while i<len(name):
#     b[name[i]]=b.get(name[i],0)+1
#     i+=1
# print(b)
 
# a='w3resource'
# b={}
# for i in a:
#     b[i]=b.get(i,0)+1
# print(b)



a=["a","b","c","m","k","l","a","b","e"]
l=[]
for j in a:
    if j in l:
      l[j]+=1
    else:
      l[j] =1
    
print(l)