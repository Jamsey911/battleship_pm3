from random import randrange


def check_ok(boat, taken):
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
    return boat


def check_boat(b, start, direct, taken):

    boat = []
    if direct == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat, taken)
    elif direct == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat, taken)
    elif direct == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_ok(boat, taken)
    elif direct == 4:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat, taken)
    return boat


def create_boats():
    taken = []
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            print(b, boat_start, boat_direction)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)

    return ships, taken


def show_board_c(taken):
    print("          Battleships")
    print("     A  B  C  D  E  F  G  H  I  J")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " o "
            row = row + ch
            place = place + 1
        print(x, " ", row)


boats, taken = create_boats()
show_board_c(taken)


# def get_shot(guesses):
#     ok = "n"
#     while ok == "n":
#         try:
#             shot = input("Please enter your guess: ")
#             shot = int(shot)
#             if shot < 0 or shot > 99:
#                 print("incorrect number, please try again")
#             elif shot in guesses:
#                 print("Number already guessed")
#             else:
#                 ok = "y"
#                 break
#         except Exception:
#             print("Incorrect entry, please select again")
#     return shot


# def show_board(hit, miss, sink):
#     print("          Battleships")
#     print("     A  B  C  D  E  F  G  H  I  J")

#     place = 0
#     for x in range(10):
#         row = ""
#         for y in range(10):
#             ch = " _ "
#             if place in miss:
#                 ch = " o "
#             elif place in hit:
#                 ch = " x "
#             elif place in sink:
#                 ch = " S "
#             row = row + ch
#             place = place + 1
#         print(x, " ", row)


# def check_shot(shot, boat1, boat2, boat3, hit, miss, sink):
#     if shot in boat1:
#         boat1.remove(shot)
#         if len(boat1) > 0:
#             hit.append(shot)
#             print("You Hit")
#         else:
#             sink.append(shot)
#             print("You sunk a ship")
#     elif shot in boat2:
#         boat2.remove(shot)
#         if len(boat2) > 0:
#             hit.append(shot)
#             print("You Hit")
#         else:
#             sink.append(shot)
#             print("You sunk a ship")
#     elif shot in boat3:
#         boat3.remove(shot)
#         if len(boat3) > 0:
#             hit.append(shot)
#             print("You Hit")
#         else:
#             sink.append(shot)
#             print("You sunk a ship")
#     else:
#         miss.append(shot)
#         print("You missed")

#     return boat1, boat2, boat3, hit, miss, sink


# boat1 = [45, 46, 47]
# boat2 = [12, 13, 14, 15]
# boat3 = [23, 24]

# hit = []
# miss = []
# sink = []

# for i in range(10):
#     guesses = hit + miss + sink
#     shot = get_shot(guesses)
#     boat1, boat2, boat3, hit, miss, sink = check_shot(shot, boat1, boat2,
#                                                       boat3, hit, miss, sink)
#     show_board(hit, miss, sink)

#     if len(boat1) < 1 and len(boat2) < 1 and len(boat3) < 1:
#         print("You've won")
#         break
# print("Finished")
