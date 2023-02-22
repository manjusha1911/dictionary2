# 1.Clear:................................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

#2.Copy:.....................................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.copy()
# print(x)

#3.Fromkeys:..........................
# x = ('key1', 'key2', 'key3')
# y = 2
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# dit = dict.fromkeys(x,1)
# print(dit)

#4.Get:..................................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model")
# print(x)
# print(car.get("model"))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("brand", 15000)
# print(x)

# 5.Items:..............................
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = a.items()
# a=set(x)
print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# car["year"] = 2018
# print(x)

# 6.keys:...................................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.keys()
# # print(car.keys())
# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "white"
# x = car.keys()
# print(x)

# 7.pop:...................................

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(car)
# print(car.pop("model"))
# print(car)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=car.pop("year")
# print(car)
# print(x)

# 8.poitems:..........................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=car.popitem()
# print(x)
# print(car)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.popitem()
# print(x)

# 9.setdefault:..........................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# } 
# x = car.setdefault("model", "Bronco")
# print(car.setdefault("model", "Bronco"))
# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault("color", "white")
# print(x)

# 10.update:..............................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.update({"color": "White"}))
# print(car)

# 11.Values:.................................
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["manjusha"]="sai"
# x=car.values()
# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values()
# print(x)
