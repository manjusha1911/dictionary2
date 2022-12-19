'''Q49.Python: Access dictionary key’s element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
physics
math
chemistry
'''

num = {'physics': 80, 'math': 90, 'chemistry': 86}
i=0
while i<len(num):
    print(list(num)[i])
    i+=1