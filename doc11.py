'''Q11.Write a Python script to merge two Python dictionaries
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
d=dic1.copy()
d.update(dic2)
print(d)
