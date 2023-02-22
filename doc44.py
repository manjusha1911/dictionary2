'''Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
Q45.
'''

def dicts(marks):
    k= marks.keys()
    v= zip(*[marks[k] for k in k])
    result = [dict(zip(k, v)) for v in v]
    return result        
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Split said dictionary of lists into list of dictionaries:")
print(dicts(marks))









