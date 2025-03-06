class Room:

    def __init__(self, north, south, east, west, room_description):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_description = room_description


def main():
    room_list = []
    entry1 = Room(4, None, 2, 0,
                  "Estás en la entrada")
    room_list.append(entry1)
    entry0 = Room(3, None, 1, None,
                  "Estás en una esquina de la casa")
    room_list.append(entry0)
    entry2 = Room(5, None, None, 1,
                  "Estás en la entrada")
    room_list.append(entry2)
    entry3 = Room(6, 0, 4, None,
                  "Estás orientándote al medio de la casa")
    room_list.append(entry3)
    entry4 = Room(None, 1, 5, 3,
                  "Estás en centro de la casa")
    room_list.append(entry4)
    entry5 = Room(None, 2, None, 4,
                  "Estás orientándote al medio de la casa")
    room_list.append(entry5)
    entry6 = Room(None, 3, 7, None,
                  "Estás llegando a la salida sigue así")
    room_list.append(entry6)
    entry7 = Room(None, None, 8, 6,
                  "Vamos que estás todavía un poco más cerca")
    room_list.append(entry7)
    entry8 = Room(None, None, 9, 7,
                  "Estás al lado de la salida")
    room_list.append(entry8)
    entry9 = Room(None, None, 10, 8,
                  "Estás prácticamente al final de la casa")
    room_list.append(entry9)
    entry10 = Room(3, None, 11, 9,
                   "Cuidado no la líes que casi has terminado")
    room_list.append(entry10)
    entry11 = Room(0, 1, 12, 10,
                   "Lambo o ruina")
    room_list.append(entry11)

    current_room = 1

    done = False
    while again:
        while not (done):
            print()
            print(room_list[current_room].room_description)

            # Checks if button is pushed
            ans2 = ["y", "n", "yes", "no"]
            if current_room == 5  == False:

            # Checks if the door is locked
            if current_room == 6 and opened == False:
                print("Looks like the door is locked. You try pushing it, achieving nothing.")
            elif current_room == 6 and opened == True:
                print("You open it.")
                time.sleep(1)
                print("You find stairs. It´s a very long way down but, when you make it, you only find one door.")
                time.sleep(1)
                print("It´s the treasure room, you made it!")
                print()
                done = True

            # Player input
            action = ""
            ans = ["n", "s", "e", "w", "north", "south", "east", "west"]
            next_room = None
            while action.lower() not in ans or next_room is None:
                if not done and not game_over:
                    print()
                    action = input("What do you do?: ")
                    action = action.lower()

                    if action not in ans:
                        print()
                        print("Sorry, that's not a valid input.")

                    # Direction triggers
                    else:
                        if action == "n" or action == "north":
                            next_room = room_list[current_room].north
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "s" or action == "south":
                            next_room = room_list[current_room].south
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "e" or action == "east":
                            next_room = room_list[current_room].east
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "w" or action == "west":
                            next_room = room_list[current_room].west
                            if next_room is None:
                                print()
                                print("There's nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        else:
                            print()
                            print("That´s not a verb I understand.")

                        if room_counter > 10:
                            game_over = True
                else:
                    break

        if done:
            current_room = 1
        elif game_over:
            print()
            print("You starved to death.")
            print("Game over.")
            current_room = 1

        again_input = None
        while again_input != "y" and again_input != "n" and again_input != "yes" and again_input != "no":
            again_input = input("Play again?: ")
            again_input = again_input.lower()
            if again_input == "y" or again_input == "yes":
                again = True
                done = False
                game_over = False
                if mode == "normal":
                    room_counter = -100000000
                elif mode == "hard":
                    room_counter = 0
            elif again_input == "n" or again_input == "no":
                again = False
            else:
                print()
                print("Sorry, that's not a valid input.")

    main()
