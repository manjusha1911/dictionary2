dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for i in dict:
    x=dict[i]
    j=0
    b=[]
    while j<len(x):
        if x[j]%2!=0:
            b.append(x[j])
        j+=1
    dict[i]=b
print(dict)