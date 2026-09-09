import consts
from consts import SOLDIER_BODY_ROWS

# soldier_image =
tup_index_soldier = (0, 50)


# BOARD_ROWS = 25
# BOARD_COLS = 50
# SOLDIER_ROWS = 4
# SOLDIER_COLS = 2

def limits(top_left_square):
    y = top_left_square[0]
    x = top_left_square[1]
    return ((y >= 0 and y < consts.BOARD_ROWS - consts.SOLDIER_ROWS) and (
                x >= 0 and x < consts.BOARD_COLS - consts.SOLDIER_COLS))
print(limits(tup_index_soldier))

def index_legs(top_left_square):
    list = []
    if(limits(top_left_square)):
        y = top_left_square[0]
        x = top_left_square[1]
        tup_left_leg = (y + 3, x)
        tup_right_leg = (y + 3, x + 1)
        list.append(tup_left_leg)
        list.append(tup_right_leg)
    return list
print(index_legs(tup_index_soldier))

def index_body(top_left_square):
    list=[]
    if(limits(top_left_square)):
        y = top_left_square[0]  #0
        x = top_left_square[1]  #0
        tup1 = top_left_square  # (0,0)
        tup2 = (y, x + 1)  # (0,1)
        tup3 = (y + 1, x)  # (1,0)
        tup4 = (y + 1, x + 1)  # (1,1)
        tup5 = (y + 2, x)  # (2,0)
        tup6 = (y + 2, x + 1)  # (2,1)
        list.append(tup1)
        list.append(tup2)
        list.append(tup3)
        list.append(tup4)
        list.append(tup5)
        list.append(tup6)
    return list
print(index_body(tup_index_soldier))