dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sum=0
for i in dict1.values():
  for item in i:
    sum+=1
print(sum)