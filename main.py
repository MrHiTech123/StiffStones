from wilderness import Wilderness, Area

castle = Wilderness(2, 2)

my_cool_room = Area('The foyer')

castle[1, 1] = my_cool_room

print(castle)
print(castle[1, 1])

