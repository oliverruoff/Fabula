import random

import pygame

from Model.Floor import Grass, Grass2, DeciduousTree

class Field:

    def __init__(self, no_x_blocks, no_y_blocks):
        self.no_x_blocks = no_x_blocks
        self.no_y_blocks = no_y_blocks

        self.image_map = {}

        self.field_list = self._create_field()

    def _create_field(self):
        field_list = []
        for y in range(self.no_x_blocks):
            for x in range(self.no_y_blocks):
                rnd = random.randint(0,100)
                if rnd > 80:
                    tree = DeciduousTree.DeciduousTree(x,y)
                    if not tree.name in self.image_map:
                        self.image_map[tree.name] = pygame.image.load(tree.img)
                    field_list.append(tree)
                else:
                    grass = Grass2.Grass2(x,y)
                    if not grass.name in self.image_map:
                        self.image_map[grass.name] = pygame.image.load(grass.img)
                    field_list.append(grass)
        print(self.image_map)
        return field_list