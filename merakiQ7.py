# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details["Student"]))
# print(Student) 

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box']))

# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
# "Name" : "Python", 
# "Age":"20", 
# "Addr" : "NJ", 
# "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)

details={
"name":"Shanti",
"age":12,
"email":"shanti@navgurukul.org"}
print(details["name"])
print(details["email"])
print(details["age"])