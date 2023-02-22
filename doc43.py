'''Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
'''

# def grouping_dictionary(l):
#     result = {}
#     for k, v in l:
#          result.setdefault (k,[]).append(v)
#     return result
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print("Grouping a sequence of key-value pairs into a dictionary of lists:\n",grouping_dictionary(colors))



def g(a):
    d={}
    for key,value in a:
        d.setdefault(key,[]).append(value)
    return d
a = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(g(a))