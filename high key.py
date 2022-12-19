my_dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
x=list(my_dict.keys())
d=dict()
x.sort(reverse=True)
x=x[:3]
print(x)