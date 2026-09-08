import consts

lst = []


def list_of_status(lst):
    for i in range(consts.BOARD_ROWS):
        status_list = []
        for j in range(consts.BOARD_COLS):
            status = "empty"
            status_list.append(status)
        lst.append(status_list)


list_of_status(lst)
#mdkgvmfdm
print(len(lst))
