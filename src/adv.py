from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [ Item("Stick", "Seriously, a stick.") ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player("Logan", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    current_room = new_player.current_room
    print(current_room.name)
    print(current_room.description)
    print("Items Visible: ")
    for item in current_room.items:
        print(" - " + item.name + " -> " + item.description)

    x = input("Specify an action: ")

    x = x.split()

    if x.__len__() == 1:
        x = x[0]
        if x is "q":
            quit("Bye!")
        elif x is "n":
            if "n_to" not in vars(current_room):
                print("Invalid direction")
                continue

            new_player.current_room = current_room.n_to
        elif x is "s":
            if "s_to" not in vars(current_room):
                print("Invalid direction")
                continue

            new_player.current_room = current_room.s_to
        elif x is "e":
            if "e_to" not in vars(current_room):
                print("Invalid direction")
                continue

            new_player.current_room = current_room.e_to
        elif x is "w":
            if "w_to" not in vars(current_room):
                print("Invalid direction")
                continue

            new_player.current_room = current_room.w_to
        
        elif x in ["i", "inventory"]:
            for item in new_player.items:
                print(f"INV ITEM: {item.name}, {item.description}")
    else:
        if x[0] in ["get", "take"]:
            found = False
            for item in current_room.items:
                if item.name == x[1]:
                    current_room.items.remove(item)
                    new_player.pickup(item)
                    item.on_take()
                    found = True

            if found:
                continue

            print("Couldn't find that item...")
        elif x[0] in ["drop"]:
            targetItem = False
            for item in new_player.items:
                if item.name == x[1]:
                    targetItem = item

            if not targetItem:
                continue
                
            current_room.items.append(targetItem)
            new_player.items.remove(targetItem)