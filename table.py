# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)

# dict1 = {}
# dict1 = {1: ["Samuel", 21, 'Data Structures'],
#          2: ["Richie", 20, 'Machine Learning'],
#          3: ["Lauren", 21, 'OOPS with java'],
#          }
# print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
# for key, value in dict1.items():
#     name, age, course = value
#     print("{:<10} {:<10} {:<10}".format(name, age, course))

# ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
# flipped = {} 
# for key, value in ini_dict.items():
#     if value not in flipped:
#         flipped[value] = [key]
#     else:
#         flipped[value].append(key)
# print("final_dictionary", str(flipped))

