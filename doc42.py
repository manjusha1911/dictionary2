'''Q42.
Write a Python program to check all values are same in a dictionary. Go to the editor
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False
'''


def value_check(students):
    result = all(x == n for x in students.values()) 
    return result
students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
n = 12
print("Check all are ",n,"in the dictionary.")
print(value_check(students))
# n = 10
# print("Check all are ",n,"in the dictionary.")
# print(value_check(students))

# mylist = [1, 1, 1]
# x = all(mylist)
# print(x)
