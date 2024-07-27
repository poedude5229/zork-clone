class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
        else:
            print("You can't go that way!")

    def take(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You picked up the {item_name}.")
                return
            print(f"There is no {item_name} here.")

    def __repr__(self):
        return f"You are in the {self.current_room.name}."
