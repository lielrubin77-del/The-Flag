import consts
import game_field

def converts_cord_to_pixel(tup):
    x = tup[0] * consts.CELL_SIZE
    y = tup[1] * consts.CELL_SIZE
    tup_pixel = (x, y)
    return tup_pixel  # מחזירה קורדינציה בפיקסלים

tup = (6, 7)
tup1 = converts_cord_to_pixel(tup)
print(tup1[0])
print(tup1[1])

def is_soldier_on_mine(left_leg, right_leg):
    x_l = left_leg[0]
    y_l = left_leg[1]
    x_r = right_leg[0]
    y_r = right_leg[1]
    if (game_field.lst[x_l][y_l] == "mine" or game_field.lst[x_r][y_r] == "mine"):
        return True
    return False

def is_soldier_on_flag(tup1, tup2, tup3):
    x1 = tup1[0]
    y1 = tup1[1]
    x2 = tup2[0]
    y2 = tup2[1]
    x3 = tup3[0]
    y3 = tup3[1]
    if (game_field.lst[x1][y1] == "flag" or game_field.lst[x2][y2] == "flag" or
            game_field.lst[x3][y3] == "flag"):
        return True
    return False
