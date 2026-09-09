import consts
import random

lst = []


def list_of_status(lst):
    for i in range(consts.BOARD_ROWS):
        status_list = []
        for j in range(consts.BOARD_COLS):
            status = "empty"
            status_list.append(status)
        lst.append(status_list)


list_of_status(lst)
print(len(lst))
print(lst[consts.BOARD_ROWS- consts.FLAG_ROWS][consts.BOARD_COLS - consts.FLAG_COLS])


def change_status_to_flag():
    x = consts.BOARD_ROWS - consts.FLAG_ROWS  # 22
    y = consts.BOARD_COLS - consts.FLAG_COLS  # 46
    for i in range(consts.FLAG_ROWS):           #3
        for j in range(consts.FLAG_COLS):       #4
            lst[x][y] = "flag"
            y+=1
        y = consts.BOARD_COLS - consts.FLAG_COLS  # 46
        x += 1

change_status_to_flag()
def print_list(lst):
    for row in lst:
        for col in row:
            print (col,end=' ')
        print()
print_list(lst)



def is_mine_placement_valid(x, y):
    y_cord=y
    for i in range(consts.MINE_ROWS):
        for j in range(consts.MINE_COLS):
            if (not (lst[x][y] == "empty")):
                return False
            y += 1
        y=y_cord
        x += 1


def random_mine():  # הגרלת מוקש ושינוי מצב ל"מוקש" בהתאם
    for i in range(consts.MINES_COUNT):
        x = random.randint(0,consts.BOARD_ROWS - consts.MINE_ROWS)  # נגריל בגבולות של המוקש
        y = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)
        while (is_mine_placement_valid(x, y) == False):
            x = random.randint(0,consts.BOARD_ROWS - consts.MINE_ROWS)  # נגריל בגבולות של המוקש
            y = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)
        y_cord=y
        for i in range(consts.MINE_ROWS):
            for j in range(consts.MINE_COLS):
                lst[x][y] = "mine"
                y+=1
            y=y_cord
            x += 1
random_mine()
print_list(lst)
