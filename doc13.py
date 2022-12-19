'''Q13.Write a Python program to sum all the items in a dictionary.
'''

# a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print(sum(a.values()))

def Sum(d):
    l= []
    for i in d:
        l.append(d[i])
    final = sum(l)
    return final
a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Sum :",Sum(a))


# print("Sum :",sum(a))