'''Q4. Write a Python script to print a dictionary where the keys are numbers    between 1 and 15 (both included) and the values are square of keys.
Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}.
'''

n=int(input("input a number:"))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)

# n=int(input("input a number:"))
# d = dict()
# i=1
# while i<=n:
#     d[i]=i*i
#     i+=1
# print(d)