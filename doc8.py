'''Q8.
Write a Python program to check whether a given key already exists in a dictionary.
'''
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def a(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
b=int(input("enter the number:"))
a(b)
