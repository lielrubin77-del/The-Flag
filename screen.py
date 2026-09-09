from PIL import Image
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

    window.blit(flag, (300, 200))


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
        # if event.type == pygame.KEYDOWN:
        #     if event.key in (pygame.K_UP, pygame.K_w):
        #         y += 20
        #         print("o")
        #     if event.key in (pygame.K_DOWN, pygame.K_s):
        #         player.y += consts.CELL_SIZE
        #     if event.key in (pygame.K_LEFT, pygame.K_a):
        #         player.x -= consts.CELL_SIZE
        #     if event.key in (pygame.K_RIGHT, pygame.K_d):
        #         player.x += consts.CELL_SIZE
    #window.blit(player, player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= consts.CELL_SIZE
    if keys[pygame.K_DOWN]:
        y += consts.CELL_SIZE
    if keys[pygame.K_LEFT]:
        x -= consts.CELL_SIZE
    if keys[pygame.K_RIGHT]:
        x += consts.CELL_SIZE


    draw()
    window.blit(player, (x, y))
    pygame.display.update()
    clock.tick(consts.CLOCK)