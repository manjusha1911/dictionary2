from collections import Counter
a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
k = Counter(a)
high = k.most_common(3)
for i in high:
    print(i[0]," :",i[1]," ")