"""
    map.py
"""

import random
import time

import pygame

import macgyver
import const


class Map:
    """
        Contains the map and functions
    """
    def __init__(self):
        """
            Initialise the map with the objects and the player
        """
        self.map = []
        self.game = True

        self.read_file()

        self.init_objects()

        pygame.init()
        self.window = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.sprites = [pygame.image.load("ressource/floor.png").convert_alpha(),
                        pygame.image.load("ressource/wall.png").convert_alpha(),
                        pygame.image.load("ressource/player.png").convert_alpha(),
                        pygame.image.load("ressource/guardian.png").convert_alpha(),
                        pygame.image.load("ressource/ether.png").convert_alpha(),
                        pygame.image.load("ressource/needle.png").convert_alpha(),
                        pygame.image.load("ressource/tube.png").convert_alpha()]

        self.display()


    def read_file(self):
        """
            Read the map file and save it
        """
        map_file = open("map.txt", "r")
        lines = map_file.readlines()

        for read_line in lines:
            tab = []
            for i in range(0, const.SPRITES):
                tab.append(int(read_line[i]))
            self.map.append(tab)

        map_file.close()


    def init_objects(self):
        """
            Initialise the objects
        """
        self.mac = macgyver.MacGyver(2, self.select_random_empty_sprite())
        self.move_sprite(self.mac.get_name(), self.mac.get_position(), self.mac.get_position())
        needle = self.select_random_empty_sprite()
        self.move_sprite(5, needle, needle)
        tube = self.select_random_empty_sprite()
        self.move_sprite(6, tube, tube)
        ether = self.select_random_empty_sprite()
        self.move_sprite(4, ether, ether)
        guard = self.select_random_empty_sprite()
        self.move_sprite(3, guard, guard)


    def display(self):
        """
            Display the map
        """
        for line in range(0, const.SPRITES):
            for column in range(0, const.SPRITES):
                if self.map[line][column] > 1:
                    self.window.blit(self.sprites[0],
                                     (column*const.SPRITE_WIDTH, line*const.SPRITE_WIDTH))

                self.window.blit(self.sprites[self.map[line][column]],
                                 (column*const.SPRITE_WIDTH, line*const.SPRITE_WIDTH))

            bag = self.mac.show_bag()
            for i in range(3):
                self.window.blit(self.sprites[bag[i]], (i*const.SPRITE_WIDTH+250, const.WIDTH))
            pygame.display.flip()

    def get_game(self):
        """
            Return if the game is over
        """
        return self.game

    def is_empty(self, line, column):
        """
            Return if the tile contain a wall
        """
        return self.map[line][column] != 1

    def select_random_empty_sprite(self):
        """
            Return an empty sprite
        """
        line = 0
        column = 0

        while self.map[line][column] != 0:
            line = random.randint(0, const.SPRITES - 1)
            column = random.randint(0, const.SPRITES - 1)

        return [line, column]

    def move_player(self, event):
        """
            Read the key pressed and move the player
        """
        pos = self.mac.get_position()
        pos_x = 0
        pos_y = 0

        if event.type == pygame.KEYDOWN\
            and event.key == pygame.K_UP\
            and pos[0] - 1 >= 0 and self.is_empty(pos[0] - 1, pos[1]):
            pos_x = -1

        elif event.type == pygame.KEYDOWN\
            and event.key == pygame.K_DOWN\
            and pos[0] + 1 < 15 and self.is_empty(pos[0] + 1, pos[1]):
            pos_x = 1

        elif event.type == pygame.KEYDOWN\
            and event.key == pygame.K_RIGHT\
            and pos[1] + 1 < 15 and self.is_empty(pos[0], pos[1] + 1):
            pos_y = 1

        elif event.type == pygame.KEYDOWN\
            and event.key == pygame.K_LEFT\
            and pos[1] - 1 >= 0 and self.is_empty(pos[0], pos[1] - 1):
            pos_y = -1

        self.verify_object([pos[0] + pos_x, pos[1] + pos_y])
        self.move_sprite(self.mac.get_name(), self.mac.get_position(),
                         [pos[0] + pos_x, pos[1] + pos_y])
        self.mac.move([pos[0] + pos_x, pos[1] + pos_y])

        if self.game:
            self.display()


    def verify_object(self, position):
        """
            Verify the object

            If the object is the guard, verify if the player won or lost
        """
        if self.map[position[0]][position[1]] != 0\
            and self.map[position[0]][position[1]] != 1 and self.map[position[0]][position[1]] != 2:
            if self.map[position[0]][position[1]] != 3:
                self.mac.pick_item(self.map[position[0]][position[1]])
            else:
                if self.mac.is_bag_full():
                    self.window.blit(pygame.image.load("ressource/win.png").convert_alpha(),
                                     (0, 0))
                    pygame.display.flip()
                    time.sleep(5)
                else:
                    self.window.blit(pygame.image
                                     .load("ressource/lost.png").convert_alpha(), (0, 0))
                    pygame.display.flip()
                    time.sleep(5)
                self.game = False

    def move_sprite(self, name, before, after):
        """
            Move a sprite
        """
        self.map[before[0]][before[1]] = 0
        self.map[after[0]][after[1]] = name
