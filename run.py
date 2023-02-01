def get_shot(guesses):
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:
                print("Number already guessed")
            else:
                ok = "y"
                break
        except Exception:
            print("Incorrect entry, please select again")
    return shot


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


def check_shot(shot, boat1, hit, miss, sink):
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
            print("You Hit")
        else:
            sink.append(shot)
            print("You sunk a ship")
    else:
        miss.append(shot)
        print("You missed")

    return boat1, hit, miss, sink


boat1 = [45, 46, 47]
hit = []
miss = []
sink = []

for i in range(10):
    guesses = hit + miss + sink
    shot = get_shot(guesses)
    boat1, hit, miss, sink = check_shot(shot, boat1, hit, miss, sink)
    show_board(hit, miss, sink)
