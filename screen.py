from PIL import Image
import pygame
import random
import consts

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption(consts.NAME_GAME)
clock = pygame.time.Clock()
player_image = pygame.image.load("soldier.png")
player = player_image.get_rect()


def draw():
    window.fill(consts.BACKGROUND_COLOR)
    window.blit(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key in (pygame.K_UP, pygame.K_w):
        #         player.y -= consts.CELL_SIZE
        #     if event.key in (pygame.K_DOWN, pygame.K_s):
        #         player.y += consts.CELL_SIZE
        #     if event.key in (pygame.K_LEFT, pygame.K_a):
        #         player.x -= consts.CELL_SIZE
        #     if event.key in (pygame.K_RIGHT, pygame.K_d):
        #         player.x += consts.CELL_SIZE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= consts.CELL_SIZE
    if keys[pygame.K_DOWN]:
        player.y += consts.CELL_SIZE
    if keys[pygame.K_LEFT]:
        player.x -= consts.CELL_SIZE
    if keys[pygame.K_RIGHT]:
        player.x += consts.CELL_SIZE


    draw()
    pygame.display.update()
    clock.tick(consts.CLOCK)