# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, items = []):
        self.name = name
        self.current_room = room
        self.items = items
    
    def pickup(self, item):
        self.items.append(item)