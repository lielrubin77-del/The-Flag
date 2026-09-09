import time

import soldier
import pygame
import random
import consts

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption(consts.NAME_GAME)
clock = pygame.time.Clock()

player = pygame.image.load("soldier.png")
player_rect_width = player.get_rect().width#width big pic
player_rect_hight = player.get_rect().height#hight big pic

player_hight = consts.SOLDIER_ROWS *consts.CELL_SIZE# what hight needs to be

player = pygame.transform.smoothscale(player, (player_hight, (player_hight/player_rect_width) *player_rect_hight))#
x = consts.SOLDIER_START[0]
y = consts.SOLDIER_START[1]

font = pygame.font.Font(None, size=25)
def random_bush():
    list = []
    for i in range(consts.BUSH_NUM):
        bush_y = random.randrange(0, consts.WINDOW_WIDTH - (consts.CELL_SIZE * consts.BUSH_HIGHT), consts.CELL_SIZE)
        bush_x = random.randrange(0, consts.WINDOW_HEIGHT - (consts.CELL_SIZE * consts.BUSH_HIGHT), consts.CELL_SIZE)#(consts.CELL_SIZE * consts.BUSH_HIGHT) not right
        list.append((bush_y,bush_x))
    return list
bush_list = random_bush()
def put_flag():
    flag = pygame.image.load("flag.png")
    flag_rect_width = flag.get_rect().width
    flag_rect_hight = flag.get_rect().height
    yachas = flag_rect_hight/flag_rect_width
    flag_hight = consts.FLAG_ROWS* consts.CELL_SIZE
    flag = pygame.transform.smoothscale(flag, (flag_hight, flag_hight*yachas))

    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_ROWS*consts.CELL_SIZE
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_COLS*consts.CELL_SIZE+20
    #print(flag_y)

    window.blit(flag, (flag_x, flag_y))


def draw_bush():
    for bush_place in bush_list:
        bush = pygame.image.load("grass.png")
        bush_rect_width = player.get_rect().width
        bush_rect_hight = player.get_rect().height
        bush_hight = consts.BUSH_HIGHT * consts.CELL_SIZE
        bush = pygame.transform.smoothscale(bush, (bush_hight, (bush_hight/bush_rect_width*bush_rect_hight)))

        window.blit(bush, (bush_place[0], bush_place[1]))

def draw():
    window.fill(consts.BACKGROUND_COLOR)
    draw_bush()
    put_flag()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y > 0:
            y -= consts.CELL_SIZE
    if keys[pygame.K_DOWN]:
        if y < consts.WINDOW_HEIGHT - consts.SOLDIER_ROWS*consts.CELL_SIZE:
            y += consts.CELL_SIZE
    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= consts.CELL_SIZE
    if keys[pygame.K_RIGHT]:
        if x < consts.WINDOW_WIDTH - consts.SOLDIER_COLS*consts.CELL_SIZE-53:
            x += consts.CELL_SIZE
    if keys[pygame.K_SPACE]:
        window.fill('red')
        print(0)
        time.sleep(3)
        #continue

    draw()
    window.blit(player, (x, y))
    pygame.display.update()
    clock.tick(consts.CLOCK)