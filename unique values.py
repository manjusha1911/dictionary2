l=[{"first":"1"}, {"second": "2"}, {"third": "1"}, 
{"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
a=[]
while i<len(l):
   for j in l[i]:
       if l[i][j] not in a:
          a.append (l[i][j])
       i+=1
print(a)