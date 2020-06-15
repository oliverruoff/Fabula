import pygame
import random
import time

from Model.Floor import Grass, Grass2, DeciduousTree
from Model.Player import Player

pygame.init()

screen_width = 640
screen_height = 640

block_width = 32
block_height = 32

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

#background = pygame.image.load('background.png')

# Sound
# mixer.music.load("background.wav")
# mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Fabula")
icon = pygame.image.load('Assets/icon.png')
pygame.display.set_icon(icon)

# FPS
font = pygame.font.Font('freesansbold.ttf', 32)
def show_fps(fps_value):
    fps = font.render("FPS : " + str(fps_value), True, (255, 255, 255))
    screen.blit(fps, (10, 10))

# Create field
def init_field(screen_width, screen_height, block_width, block_height):
    y = 0
    floor_array = []
    for i in range(int(screen_height/block_height)):
        x = 0
        floor_row = []
        for j in range(int(screen_width/block_width)):
            rnd = random.randint(0,100)
            if rnd <= 20:
                floor_row.append(DeciduousTree.DeciduousTree(x,y))
            elif rnd > 20 and rnd <= 60:
                floor_row.append(Grass.Grass(x,y))
            elif rnd > 60 and rnd <= 100:
                floor_row.append(Grass2.Grass2(x,y))
            x += block_width
        y += block_height
        floor_array.append(floor_row)
    return floor_array

def draw_floor(floor_field, block_width, block_height):
    for i in range(int(screen_height/block_height)):
        for j in range(int(screen_width/block_width)):
            block = floor_field[i][j]
            floor_img = pygame.image.load(block.img)
            screen.blit(floor_img, (block.x, block.y))

def draw_player(player):
    screen.blit(player.image, (player.x, player.y))


floor_field = init_field(screen_width, screen_height, block_width, block_height)

player = Player.Player(int(screen_width/2), int(screen_height/2))

fps_value = 0
last_time = time.time()
running = True
while running:
    clock.tick(10)
    # RGB = Red, Green, Blue
    screen.fill((49, 142, 70))
    # Background Image
    # screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_floor(floor_field, block_width, block_height)

    print(event.type)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.is_walking = True
            player.mode = 'left'
            player.x -= 6
        if event.key == pygame.K_RIGHT:
            player.is_walking = True
            player.mode = 'right'
            player.x += 6
        if event.key == pygame.K_UP:
            player.is_walking = True
            player.mode = 'up'
            player.y -= 6
        if event.key == pygame.K_DOWN:
            player.is_walking = True
            player.mode = 'down'
            player.y += 6
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or \
            event.key == pygame.K_RIGHT or \
            event.key == pygame.K_UP or \
            event.key == pygame.K_DOWN:
            player.is_walking = False

    print('Player x:', player.x, '| :y', player.y, '| is_walking:', player.is_walking)

    player.update()
    draw_player(player)

    # FPS management
    curr_time = time.time()
    seconds_passed = curr_time - last_time
    last_time = curr_time
    fps_value = int(1 / seconds_passed)
    show_fps(fps_value)


    # Render
    pygame.display.update()
