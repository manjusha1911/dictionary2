"""Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
"""


a=[{"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"}]
print(sum(i["id"]for i in a))


# m=[{"manjusha":3,"honey":2,"nany":1},{"manjusha":2,"honey":1,"nany":2},{"manjusha":2,"honey":0,"nany":2}]
# print(sum(i["honey"]for i in m))