# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# dict1={"name":"Raju","marks":56}
# a=input ("enter the value=")
# if (a=="name"):
#   print (dict1["name"])
# elif(a=="marks"):
#   print(dict1["marks"])
# else:
#   print ("invalid input")

# my_dict = {'data1':100,'data2': -54,'data3': 247}
# sum=0
# for i in my_dict.values():
#     sum=sum+i
# print(sum)

# a={1:"A",2:"B",3:"C"}
# for i in a:
#     print(i,end=" ")

# a={1:"A",2:"B",3:"C"}
# a.items()

# Dic=  {1: 'NAVGURUKUL',2: 'IN',  3:{ 'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del(Dic[3]['A'])
# print(Dic)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# dic={"ball":"red",  "bat":4, "wickets":8, "ball":"green", "bat":3}
# temp = []
# res = dict()
# for key, val in dic.items():
#     if val not in temp:
#       temp.append(val)
#       res[key] = val
# print(res)

# test_list=[
# {"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}
# ]
# res = list(set(val for dic in test_list for val in dic.values()))
# print("The unique values in list are : " + str(res))
details={}
for i in range(10):
   n=input("enter name:")
   m=input("enter marks:")
   details[n]=m
print(details)