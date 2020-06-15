import pygame

class Player():

    def __init__(self, x, y):
        super(Player, self).__init__()

        sprite_width = 32
        sprite_height = 32

        # down images
        self.down_images = []
        self.down_images.append(pygame.image.load('Assets/Player/player_down_1.png'))
        self.down_images.append(pygame.image.load('Assets/Player/player_down_2.png'))

        # up images
        self.up_images = []
        self.up_images.append(pygame.image.load('Assets/Player/player_up_1.png'))
        self.up_images.append(pygame.image.load('Assets/Player/player_up_2.png'))
        # left images
        self.left_images = []
        self.left_images.append(pygame.image.load('Assets/Player/player_left_1.png'))
        self.left_images.append(pygame.image.load('Assets/Player/player_left_2.png'))
        # right images
        self.right_images = []
        self.right_images.append(pygame.image.load('Assets/Player/player_right_1.png'))
        self.right_images.append(pygame.image.load('Assets/Player/player_right_2.png'))

        self.x = x
        self.y = y
        self.is_walking = False
        self.field_of_view = 5

        self.index = 0
        self.image = self.down_images[self.index]
        self.rect = pygame.Rect(x, y, sprite_width, sprite_height)

        self.mode = 'down'

    def update(self):
        if self.is_walking:
            self.index += 1
            if self.index >= len(self.down_images):
                self.index = 0

        if self.mode == 'down':
            self.image = self.down_images[self.index]
        elif self.mode == 'up':
            self.image = self.up_images[self.index]
        elif self.mode == 'left':
            self.image = self.left_images[self.index]
        elif self.mode == 'right':
            self.image = self.right_images[self.index]
