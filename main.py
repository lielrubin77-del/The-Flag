import consts


def converts_cord_to_pixel(tup):
    x = tup[0] * consts.CELL_SIZE
    y = tup[1] * consts.CELL_SIZE
    tup_pixel = (x, y)
    return tup_pixel


tup = (6, 7)
tup1 = converts_cord_to_pixel(tup)
print(tup1[0])
print(tup1[1])
