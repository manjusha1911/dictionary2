'''Q45.
Write a Python program to remove a specified dictionary from a given list. 
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
'''

test_list= [{"id":"#FF0000","color":"Red"},{"id":"#800000","color":"Maroon"},{"id":"#FFFF00","color":"Yellow"},{"id":"#808000","color":"Olive"}] 
for i in range(len(test_list)):
    if test_list[i]['id'] == "#FF0000":
        del test_list[i]
        break
print ("Remove id #FF0000 from the said list of dictionary:\n" +  str(test_list))