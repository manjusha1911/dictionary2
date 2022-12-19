'''Q31.. Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
'''
# from collections import Counter
# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# k = Counter(a)
# high = k.most_common(3)
# for i in high:
#     print(i[0]," :",i[1]," ")

my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
x=list(my_dict.values())
d=dict()
x.sort(reverse=True)
x=x[:3]
for i in x:
    for j in my_dict.keys():
        if(my_dict[j]==i):
            print(str(j)+" : "+str(my_dict[j]))