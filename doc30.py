'''Q30.Write a Python program to remove spaces from dictionary keys.
Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
'''

d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
nd={}
for i in d:
    k={i.replace(" ","")}
    for j in k:
        nd[j]=d[i]
print(nd)



