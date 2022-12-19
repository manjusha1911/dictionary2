# subjects=["telugu","english","maths","science","social"]
# marks=[65,74,62,84]
# a=zip(subjects,marks)
# result=dict(a)
# print(result)


my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip (*([key]+(value)
    for key ,value in sorted (my_dict.items()))):
    print(*row)
    
    
    
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 2, 'CS' : 2}
print("The original dictionary : " +  str(test_dict))
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("Frequency of K is : " + str(res))