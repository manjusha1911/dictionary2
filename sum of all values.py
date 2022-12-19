# a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d=a.values()
# l=list(d)
# i=0
# sum=0
# while i<len(l):
#     sum+=l[i]
#     i+=1
# print(sum)


def Sum(d):
    l= []
    for i in d:
        l.append(d[i])
    final = sum(l)
    return final
a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Sum :",Sum(a))
