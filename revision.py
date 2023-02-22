# d= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# for key ,values in d.items():
#     count+=1
#     print(key,values,count)
# user=int(input("enter length of dict:"))
# i=0
# mydict={}
# while i<user:
#     k=input("enter key:")
#     v=input("enter value:")
#     mydict[k]=v
#     i+=1
# print(mydict)
  
 
 
# n=int(input("enter the number:")) 
# i=1
# d={}
# while i<=n:
#     name=input("enter the name:")
#     i+=1
#     j=0
#     while j<3:
#         k=input("enter key:")
#         v=input("enter value:")
#         j+=1
#     d[k]=v
# print(d)

def m(s):
    d={}
    for k,v in s:
        d.setdefault(k,[]).append(v)
    return(d)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(m(s))