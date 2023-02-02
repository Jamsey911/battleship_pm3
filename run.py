from random import randrange
import random


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
    print("          Computer")
    print("     A  B  C  D  E  F  G  H  I  J")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " c "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def get_shot_comp(guesses, tactics):
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except Exception:
            print("Incorrect entry, please select again")
    return shot, guesses


def show_board(hit, miss, sink):
    print("          Battleships")
    print("     A  B  C  D  E  F  G  H  I  J")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " o "
            elif place in hit:
                ch = " x "
            elif place in sink:
                ch = " S "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, ships, hit, miss, sink):
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                sink.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)

    return ships, hit, miss, sink, missed


def cal_tactics(shot, tactics, guesses, hit):

    temp = []
    if len(tactics) < 1:
        temp = [shot - 1, shot + 1, shot - 10, shot + 10]
    else:
        if shot - 1 in hit:
            if shot - 2 in hit:
                temp = [shot - 3, shot + 1]
            else:
                temp = [shot - 2, shot + 1]
        elif shot + 1 in hit:
            if shot + 2 in hit:
                temp = [shot + 3, shot - 1]
            else:
                temp = [shot + 2, shot - 1]
        elif shot - 10 in hit:
            if shot - 20 in hit:
                temp = [shot - 30, shot + 10]
            else:
                temp = [shot - 20, shot + 10]
        elif shot + 10 in hit:
            if shot + 20 in hit:
                temp = [shot + 30, shot - 10]
            else:
                temp = [shot + 20, shot - 10]
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)

    return cand


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])


hit = []
miss = []
sink = []
guesses = []

ships, taken = create_boats()

tactics = []
for i in range(100):
    shot, guesses = get_shot_comp(guesses, tactics)
    ships, hit, miss, sink, missed = check_shot(shot, ships, hit, miss, sink)
    if missed == 1:
        tactics = cal_tactics(shot, tactics, guesses, hit)
    elif missed == 2:
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0)
    if check_if_empty_2(ships):
        print("End of game", i)
        break


show_board_c(taken)
show_board(hit, miss, sink)  


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
