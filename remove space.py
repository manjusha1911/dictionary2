d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
nd={}
for i in d:
    k={i.replace(" ","")}
    for j in k:
        nd[j]=d[i]
print(nd)