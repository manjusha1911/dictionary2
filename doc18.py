'''Q18.Write a Python program to get the maximum and minimum value in a dictionary.
'''
# dict={'a':5,'b':10,'c':2,'d':7}
# val=dict.values()
# print(max(val))
# print(min(val))

dict={'a':189,'b':10,'c':2,'d':7}
value=dict.values()
l=list(value)
max=0
min=1000
i=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
    i+=1
print("maximum value:",max)
print("minimum value:",min)