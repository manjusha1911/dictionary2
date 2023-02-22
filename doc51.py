'''Q51.Write a Python program to filter even numbers from a given dictionary values. 
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}
'''


dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for i in dict:
    x=dict[i]
    j=0
    b=[]
    while j<len(x):
        if x[j]%2==0:
            b.append(x[j])
        j+=1
    dict[i]=b
print(dict)