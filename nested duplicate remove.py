s={"d1":{11:2,1:2},"d1":{1:100,2:"manjusha"},"d2":{1:3,1:4},"d3":{1:6,1:11}}
b= {}
for key,value in s.items():
    if value not in b.values():
        b[key] = value
print(b)
    