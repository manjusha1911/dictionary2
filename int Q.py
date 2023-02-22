for i in range(100,200):
   if all(i%i=0 for i in range(2,i)):
      print(i) 