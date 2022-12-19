'''Q21.Write a Python program to print all unique values in a dictionary. 
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
# print("Original List: ",l)
# u_value = set( val for dic in l for val in dic.values())
# print("Unique Values: ",u_value) 

a=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
i=0
b=[]
while i<len(a):
    for j in a[i]:
        if a[i][j]not in b:
            b.append(a[i][j])
    i+=1
print(b)