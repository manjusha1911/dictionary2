'''Q45.
Write a Python program to remove a specified dictionary from a given list. 
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
'''


def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors
colors = [{"id":"#FF0000","color":"Red"},{"id":"#800000","color":"Maroon"},{"id":"#FFFF00","color":"Yellow"},{"id":"#808000","color":"Olive"}] 
r_id = "#FF0000"
print("Remove id",r_id,"from the said list of dictionary:")
print(remove_dictionary(colors, r_id))
