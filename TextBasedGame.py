# Randy Marcelino

# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Star Wars Text Adventure Game")
    print("Collect 6 items to win the game, or be defeated by the Emperor Palpatine.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# A function to display room information and get next command
def show_room_information():
    # Checks if game needs to be ended by checking if player has met end criteria.
    if end_game() == 0:
        return 0
    else:
        print()
        # Displays current room, item, and inventory.
        print("You are in the {room}".format(room=current_room))
        print("Inventory: {}".format(inventory))
        if "item" in rooms[current_room]:
            print("You see {}".format(rooms[current_room]["item"]))
        # Print line for cleanliness.
        print("----------------------")
        # Gets next user command.
        user_command = input("Enter a command: ")
        return user_command


# Validates user input.
def check_user_input(user_input):
    # Validates if player put in directional command.
    # Then executes move function to move player.
    if "go South" in user_input:
        return move_player("South")
    elif "go North" in user_input:
        return move_player("North")
    elif "go East" in user_input:
        return move_player("East")
    elif "go West" in user_input:
        return move_player("West")
    # Validates if user put in get item command.
    elif "get" in user_input:
        # If item is in room it will proceed to add it to inventory.
        if "get {}".format(rooms[current_room]["item"]) in user_input:
            return get_items()
        else:
            # Presents error message if item is not in room.
            print("Can't get {}".format(user_input[4:]))
            return show_room_information()
    # Presents error message if user put in invalid command.
    else:
        print("Invalid input!")
        return show_room_information()


# This function moves players from room to room.
def move_player(direction):
    global current_room
    # Validates that direction exist.
    if direction in rooms[current_room]:
        # If it does exist then player location will be updated and new room info will be displayed.
        current_room = rooms[current_room][direction]
        return show_room_information()
    else:
        # If room does not exist displays error message.
        print("You can’t go that way!")
        return show_room_information()


# This function gets items and adds them to the inventory then removes them from the world.
def get_items():
    global inventory
    # Adds to inventory item in current room and removes it from the world.
    inventory.append(rooms[current_room]["item"])
    del rooms[current_room]["item"]
    return show_room_information()


# Function checks if game needs to be ended.
def end_game():
    # Checks current player room if it is final boss room.
    if "Death Star" in current_room:
        # If player has all items show victory message else shows failure message.
        if len(inventory) < 6:
            print("Oh No! You were defeated by {}!".format(rooms[current_room]["item"]))
            print("Thank you for playing better luck next time young Padawan!")
            return 0
        else:
            print("Congratulation! You managed to gather all the materials needed to fight back {}!".format(
                rooms[current_room]["item"]))
            print("Thank you for playing! Good job Jedi Knight!")
            return 0


# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (Main Hall) and the room containing the villain
rooms = {
    'Main Hall': {'South': 'Tech Room', 'North': 'Storage', 'West': 'Council Room'},
    'Council Room': {'East': 'Main Hall', 'item': 'Yoda'},
    'Tech Room': {'North': 'Main Hall', 'East': 'Armory', 'item': 'Droids'},
    'Storage': {'South': 'Main Hall', 'East': 'War Room', 'item': 'Jet Packs'},
    'Armory': {'North': 'Hangar', 'West': 'Tech Room', 'item': 'Beskar Armor'},
    'War Room': {'South': 'Hangar', 'West': 'Storage', 'item': 'Lightsabers'},
    'Hangar': {'North': 'War Room', 'South': 'Armory', 'East': 'Death Star', 'item': 'Millennium Falcon'},
    'Death Star': {'West': 'Hangar', 'item': 'Emperor Palpatine'}  # villain
}

# Displays instructions on how to play.
show_instructions()

# Establish starting room and empty inventory.
current_room = 'Main Hall'
inventory = []

# Starts out the game!
command = show_room_information()

# Loop will continue until end criteria are met shown in function end_game.
while command != 0:
    command = check_user_input(command)
