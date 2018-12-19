import random
from MacGyver import *
import pygame
from pygame.locals import *
import time
import const


class Map:
    def __init__(self):
        self.map = []
        self.game = True

        self.read_file()

        self.init_objects()

        pygame.init()
        self.fenetre = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.sprites = [pygame.image.load("ressource/floor.png").convert_alpha(), pygame.image.load("ressource/wall.png").convert_alpha(), pygame.image.load("ressource/player.png").convert_alpha(), pygame.image.load("ressource/guardian.png").convert_alpha(), pygame.image.load("ressource/ether.png").convert_alpha(), pygame.image.load("ressource/needle.png").convert_alpha(), pygame.image.load("ressource/tube.png").convert_alpha()]

        self.display()


    def read_file(self):
        map_file = open("map.txt", "r")
        lines = map_file.readlines()

        for read_line in lines:
            tab = []
            for i in range(0, const.SPRITES):
                tab.append(int(read_line[i]))
            self.map.append(tab)

        map_file.close()


    def init_objects(self):
        self.mac = MacGyver(2, self.select_random_empty_sprite())
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
        object = 0
        for line in range(0, const.SPRITES):
            for column in range(0, const.SPRITES):
                object = int(self.map[line][column])
                if object > 1:
                    self.fenetre.blit(self.sprites[0], (column*const.SPRITE_WIDTH, line*const.SPRITE_WIDTH))
                self.fenetre.blit(self.sprites[object], (column*const.SPRITE_WIDTH, line*const.SPRITE_WIDTH))

            bag = self.mac.show_bag()
            for i in range(3):
                self.fenetre.blit(self.sprites[bag[i]], (i*const.SPRITE_WIDTH+250, const.WIDTH))
            pygame.display.flip()

    def get_game(self):
        return self.game

    def is_empty(self, line, column):
        return self.map[line][column] != 1

    def select_random_empty_sprite(self):
        line = 0
        column = 0

        while self.map[line][column] == 1:
            line = random.randint(0, const.SPRITES - 1)
            column = random.randint(0, const.SPRITES - 1)

        return [line, column]

    def move_player(self, event):
        pos = self.mac.get_position()
        x = 0
        y = 0

        if event.type == KEYDOWN and event.key == K_UP and pos[0] - 1 >= 0 and self.is_empty(pos[0] - 1, pos[1]):
            x = -1

        elif event.type == KEYDOWN and event.key == K_DOWN and pos[0] + 1 >= 0 and self.is_empty(pos[0] + 1, pos[1]):
            x = 1

        elif event.type == KEYDOWN and event.key == K_RIGHT and pos[1] + 1 >= 0 and self.is_empty(pos[0], pos[1] + 1):
            y = 1

        elif event.type == KEYDOWN and event.key == K_LEFT and pos[1] - 1 >= 0 and self.is_empty(pos[0], pos[1] - 1):
            y = -1

        self.verify_object([pos[0] + x, pos[1] + y])
        self.move_sprite(self.mac.get_name(), self.mac.get_position(), [pos[0] + x, pos[1] + y])
        self.mac.move([pos[0] + x, pos[1] + y])

        if self.game:
            self.display()


    def verify_object(self, position):
        if self.map[position[0]][position[1]] != 0 and self.map[position[0]][position[1]] != 1 and self.map[position[0]][position[1]] != 2:
            if self.map[position[0]][position[1]] != 3:
                self.mac.pick_item(self.map[position[0]][position[1]])
            else:
                if self.mac.is_bag_full():
                    self.fenetre.blit(pygame.image.load("ressource/win.png").convert_alpha(), (0,0))
                    pygame.display.flip()
                    time.sleep(5)
                else:
                    self.fenetre.blit(pygame.image.load("ressource/lost.png").convert_alpha(), (0,0))
                    pygame.display.flip()
                    time.sleep(5)
                self.game = False

    def move_sprite(self, name, before, after):
        self.map[before[0]][before[1]] = 0
        self.map[after[0]][after[1]] = name
