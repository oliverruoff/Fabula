import pygame
import random
import time

from Model.Floor import Grass, Grass2, DeciduousTree, Field
from Model.Player import Player

DEBUG = True

pygame.init()


block_width = 32
block_height = 32
screen_width = 640
screen_height = 640

def show_fps(fps_value):
    fps = font.render("FPS : " + str(fps_value), True, (255, 255, 255))
    screen.blit(fps, (10, 10))

def draw_field(field):
    for block in field.field_list:
        screen.blit(field.image_map[block.name],
        (block.x*block_width, block.y*block_height))

def draw_player(player):
    screen.blit(player.image, (player.x, player.y))

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
        
field = Field.Field(20,20)

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

    # Drawing the field
    draw_field(field)

    # Debugging
    if DEBUG:
        print('Player x:', player.x, '| :y',
        player.y, '| is_walking:', player.is_walking)

    player.update()
    draw_player(player)

    # FPS management
    curr_time = time.time()
    seconds_passed = curr_time - last_time
    last_time = curr_time
    fps_value = int(1 / seconds_passed)
    if DEBUG:
        show_fps(fps_value)

    # Render
    pygame.display.update()
