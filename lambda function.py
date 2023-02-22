# x = lambda a, b ,c: a * b*c
# print(x(5, 6,2))

x = lambda a ,b,c:a*b+c
print(x(5,2,2))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# rn lambda a : a * n

# def a(n):
#   return lambda a : a * n
# b = a(2)
# print(b(11))

# def myfunc(n):
#   return lambda a : a * n
# mytripler = myfunc(3)
# print(mytripler(11))

# def a(n):
#   return lambda a : a * n
# mydoubler = a(2)
# mytripler = a(3)
# myfour=a(5)
# print(mydoubler(11))
# print(mytripler(11))
# print(myfour(11))
# print(mydoubler(11))
# print(mytripler(11))
# print(myfour(11))

# a=lambda x,y:x*y
# print(a(10,2))


a=list(filter(lambda n:n%2==0,range(1,11)))
print(a)