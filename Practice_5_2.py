import random
import time
from timeit import default_timer as timer
start = timer()

w = True
c1 = key = True
c2 = False
cp = False
count = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while w:
    try:

        mode = int(input("Enter (1) to play with the 'PC' and (2) to play with the 'user': "))
        if (type(mode) == int) & (1 <= mode <= 2):
            break
        print(bcolors.FAIL + "index out of range!, try again" + bcolors.ENDC)
    except ValueError:
        print(bcolors.FAIL + "ERROR >>>>> Enter a digit :" + bcolors.ENDC)

def show_game_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == "X":
                print(bcolors.WARNING + game[i][j], end=' ' + bcolors.ENDC)
            if game[i][j] == "O":
                print(bcolors.OKCYAN + game[i][j], end=' ' + bcolors.ENDC)
            if game[i][j] == "-":
                print(bcolors.ENDC + game[i][j], end=' ' + bcolors.ENDC)
        print()


def check():
    for i in range(3):
        if (game[i][0] == "X") and (game[i][1] == "X") and (game[i][2] == "X") or \
                (game[0][i] == "X") and (game[1][i] == "X") and (game[2][i] == "X") or \
                (game[0][0] == "X") and (game[1][1] == "X") and (game[2][2] == "X") or \
                (game[2][0] == "X") and (game[1][1] == "X") and (game[0][2] == "X"):
            print(bcolors.WARNING + "player 1 wins" + bcolors.ENDC)
            end = timer()
            print("Time has passed: ", round((end - start), 2))  # Time in seconds
            exit()
        if (game[i][0] == "O") and (game[i][1] == "O") and (game[i][2] == "O") or \
                (game[0][i] == "O") and (game[1][i] == "O") and (game[2][i] == "O") or \
                (game[0][0] == "O") and (game[1][1] == "O") and (game[2][2] == "O") or \
                (game[2][0] == "O") and (game[1][1] == "O") and (game[0][2] == "O"):
            if mode == 2:
                print(bcolors.OKCYAN + "player 2: wins" + bcolors.ENDC)
                end = timer()
                print("Time has passed: ", round((end - start), 2))  # Time in seconds
                exit()
            if mode == 1:
                print(bcolors.OKCYAN + "PC: wins" + bcolors.ENDC)
                end = timer()
                print("Time has passed: ", round((end - start), 2))  # Time in seconds
                exit()
        elif count == 9:
            print("** The game ended in a draw **")
            exit()

game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

while True:
    show_game_board()
    check()
    if c1:
        print(bcolors.WARNING + "player: 1 " + bcolors.ENDC)
        key = False
        count += 1
    if cp:
        print(bcolors.OKCYAN + "player: PC" + bcolors.ENDC)
        count += 1
    if c2:
        print(bcolors.OKCYAN + "player: 2" + bcolors.ENDC)
        count += 1
    while True:
        while cp:
            row = (random.randint(1, 3)) - 1
            col = (random.randint(-1, 1)) + 1
            print("row:", row, "col:", col)
            if game[row][col] == '-':
                # if game[row][col] == '-':
                print("row: ", row, "col: ", col)
                game[row][col] = "O"
                cp = False
                c1 = key = True
                break
            else:
                print(bcolors.FAIL + "cell is not empty!, try again" + bcolors.ENDC)
                time.sleep(1)
        if key:
            break
        if (c1 == True) or (c2 == True):

            try:
                row = int(input("Enter your row: "))
                col = int(input("Enter your col: "))
                # except ValueError:
                #     print(" \n ERROR >>>>> enter a digit :")
                if (0 <= row <= 2) & (0 <= col <= 2) & (type(row) == int):
                    if game[row][col] == '-':
                        if c1:
                            game[row][col] = "X"
                            c1 = False
                            if mode == 2:
                                c2 = True
                            if mode == 1:
                                cp = True
                                c1 = False
                            break
                        if c2:
                            game[row][col] = "O"
                            c1 = True
                            c2 = False
                            break
                    else:
                        print(bcolors.FAIL + "cell is not empty!, try again" + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + "index out of range!, try again" + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "ERROR >>>>> enter a digit :" + bcolors.ENDC)
