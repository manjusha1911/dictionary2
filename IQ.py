# days=int(input("enter the number:"))
# if days<=5:
#     print("total charges",days*2)
# elif days>5 and days<=10:
#     charge2=(5*2)+(days-5)*3
# elif days>=10 and days<=15:
#     charge3=(5*2)+(5*3)+(days-10)*4
#     print("total charges:",charge3)
# else:
#     charge4=(5*2)+(5*3)+(5*4)+(days-15)*5
#     print("total charges:",charge4)

# a="my name is manjusha"
# b=a.replace("manjusha","swati")
# print(b)

# a=int(input("enter the a value:"))
# b=int(input("enter the b value:"))
# i=1
# m=0
# while i<=b:
#     m=m+a 
#     i+=1
# print(m)


# a=[1,2,4,2,7,1,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c=a.count(a[i])
#         if c==1:
#             print(a[i])
#     i=i+1
        

# a=["s","w","a","t","i"]
# i=0
# b=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b+=a[i][j]
#         j+=1
#     i+=1
# print(b)

# s="manjusha"
# b=[]
# for i in s:
#     b.append(i)
# print(b)

# a="mani"
# b=[]
# i=0
# while i<len(a):
#     b.append (a[i])
#     i=i+1
# print(b)

# a="Nagamani is singing very loudly"
# b=a.replace("is","was")
# print(b)
# c=b.replace("singing","")
# print(c)
# i=0
# while i<len(a):
#         d=a.replace("is","was")
#         i=i+1
# print(d)
# print(a[:12],a[20::],end="") 

# a=[8,5,6,7,3,2,4,9]
# i=0
# b=[]
# j=-1
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[j])
#         b.append(a[i])
#     i+=1
#     j-=1
# print(b)

# a=[8,5,6,7,3,2,4,9]
# i=0
# l=[]
# j=-1
# while i<len(a):
#     if a[i] not in l:
#         l.append(a[i])
#         l.append(a[j])    
#     i=i+1
#     j=j-1
# print(l)

# def manju(a):
#     i=0
#     max1=0
#     max2=0
#     max3=0
#     while i<len(a):
#         if a[i]>max1:
#             max1=a[i]
#         i+=1
#     print(max1)
#     j=0
#     while j<len(a):
#         if a[j]>max2 and a[j]<max1:
#             max2=a[j]
#         j+=1
#     k=0
#     print(max2)
#     while k<len(a):
#         if a[k]>max3 and a[k]<max2:
#             max3=a[k]
#         k+=1
#     print(max3)
# manju([15,29,600,92,2,1600,1234])

# units=int(input("enter the number:"))
# if units<=100:
#     print("no charges")
# elif units>100 and units <=200:
#     charges=(units-100)*5
#     print("totsl units:",charges)
# else:
#     charges2=(units-200)*10
#     print("total cost:",charges2+(100*5))


