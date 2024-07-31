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
melanat_wharf = Room("Wharf", "You stand on weathered, crumbling boards, surrounded on either side by raging cold waters. In the pale light of the moon you see a fisherman at the end of the pier.")
melanat_spire = Room("Darkstone Spire","You ascend the stairs and find yourself atop the Darkstone Spire on the eastern shore of this side of Melanat.")
cave_entrance_f1 = Room("First cave entrance","You walk into the opening of the sheer limestone cliffs of Melanat. Inside this cave you see a door to the north and east, and a doorway to the west.")
cave_f1_west_room = Room("Western Floor 1 Room","In this room you see a small chest, a fountain and a pale spot on the wall")
