class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

        def add_exit(self, direction, room):
            self.exits[direction] = room

        def add_item(self, item):
            self.items.append(item)

        def __repr__(self):
            return self.description

outside_start = Room("Melanat Shore","You find yourself on the sands of Melanat's peninsula. The shore is washed in moonlight. You see a cave entrance to the north, a spire to the east and a wharf to the west.")
# melanat_wharf
