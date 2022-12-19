student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print("id count",sum(d['id'] for d in student))
print("success count",sum(d['success'] for d in student))

