from castle import Castle, Room

castle = Castle(2, 2)

my_cool_room = Room('The foyer')

castle[1, 1] = my_cool_room

print(castle)
print(castle[1, 1])

