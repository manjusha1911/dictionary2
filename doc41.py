'''Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}
'''

def filter_data(students):
    result = dict(filter(lambda students: (students[1][0], students[1][1]) >=(6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Height> 6ft and Weight> 70kg:")
print(filter_data(students))
