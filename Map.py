import random
from MacGyver import *
import pygame
from pygame.locals import *


class Map:
    def __init__(self):
        self.map = []
        self.game = True
        map_file = open("map.txt", "r")
        lines = map_file.readlines()

        for read_line in lines:
            tab = []
            for i in range(0, 15):
                tab.append(int(read_line[i]))
            self.map.append(tab)

        self.mac = MacGyver(2, self.select_random_empty_sprite())
        self.move_sprite(self.mac.get_name(), self.mac.get_position(), self.mac.get_position())

        # self.needle = Objects("n", self.select_random_empty_sprite())
        needle = self.select_random_empty_sprite()
        self.move_sprite(5, needle, needle)
        tube = self.select_random_empty_sprite()
        self.move_sprite(6, tube, tube)
        ether = self.select_random_empty_sprite()
        self.move_sprite(4, ether, ether)
        guard = self.select_random_empty_sprite()
        self.move_sprite(3, guard, guard)

        map_file.close()

        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 640))
        self.sprites = [pygame.image.load("ressource/floor.png").convert_alpha(), pygame.image.load("ressource/wall.png").convert_alpha(), pygame.image.load("ressource/player.png").convert_alpha(), pygame.image.load("ressource/guardian.png").convert_alpha(), pygame.image.load("ressource/ether.png").convert_alpha(), pygame.image.load("ressource/needle.png").convert_alpha(), pygame.image.load("ressource/tube.png").convert_alpha()]

        self.display()

    def display(self):
        object = 0
        for line in range(0, 15):
            for column in range(0, 15):
                object = int(self.map[line][column])
                if object > 1:
                    self.fenetre.blit(self.sprites[0], (column*40,line*40))
                self.fenetre.blit(self.sprites[object], (column*40,line*40))

            bag = self.mac.show_bag()
            for i in range(3):
                self.fenetre.blit(self.sprites[bag[i]], (i*40+250, 600))
            pygame.display.flip()

    def get_game(self):
        return self.game

    def is_empty(self, line, column):
        return self.map[line][column] != 1

    def select_random_empty_sprite(self):
        line = 0
        column = 0

        while self.map[line][column] == 1:
            line = random.randint(0, 14)
            column = random.randint(0, 14)

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
                    print("Gagné !")
                else:
                    print("Perdu :(")
                self.game = False

    def move_sprite(self, name, before, after):
        self.map[before[0]][before[1]] = 0
        self.map[after[0]][after[1]] = name
