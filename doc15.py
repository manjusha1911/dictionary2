'''Q15.Write a Python program to remove a key from a dictionary.
'''
# a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# print(a)
a={'a':1,'b':2,'c':3,'d':4}
user=input("enter the key:")
if user in a: 
    del a[user]
    print(a)
else:
    print(user,"is not exist")

