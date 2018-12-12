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
                tab.append(read_line[i])
            self.map.append(tab)

        self.mac = MacGyver("M", self.select_random_empty_sprite())
        self.move_sprite(self.mac.get_name(), self.mac.get_position(), self.mac.get_position())

        # self.needle = Objects("n", self.select_random_empty_sprite())
        needle = self.select_random_empty_sprite()
        self.move_sprite("n", needle, needle)
        tube = self.select_random_empty_sprite()
        self.move_sprite("t", tube, tube)
        ether = self.select_random_empty_sprite()
        self.move_sprite("e", ether, ether)
        guard = self.select_random_empty_sprite()
        self.move_sprite("G", guard, guard)

        map_file.close()

        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 600))
        self.sprites = [pygame.image.load("ressource/floor.png").convert_alpha(), pygame.image.load("ressource/wall.png").convert_alpha(), pygame.image.load("ressource/player.png").convert_alpha(), pygame.image.load("ressource/guardian.png").convert_alpha(), pygame.image.load("ressource/ether.png").convert_alpha(), pygame.image.load("ressource/needle.png").convert_alpha(), pygame.image.load("ressource/tube.png").convert_alpha()]

        self.display()

    def display(self):
        object = 0
        for line in range(0, 15):
            for column in range(0, 15):
                if self.map[line][column] == " ":
                    object = 0
                elif self.map[line][column] == "x":
                    object = 1
                elif self.map[line][column] == "M":
                    object = 2
                elif self.map[line][column] == "G":
                    object = 3
                elif self.map[line][column] == "e":
                    object = 4
                elif self.map[line][column] == "n":
                    object = 5
                elif self.map[line][column] == "t":
                    object = 6

                if object > 1:
                    self.fenetre.blit(self.sprites[0], (column*40,line*40))

                self.fenetre.blit(self.sprites[object], (column*40,line*40))
            pygame.display.flip()

    def get_game(self):
        return self.game

    def is_empty(self, line, column):
        return self.map[line][column] != "x"

    def select_random_empty_sprite(self):
        line = 0
        column = 0

        while self.map[line][column] == "x":
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
            print(self.mac.show_bag())

    def verify_object(self, position):
        if self.map[position[0]][position[1]] != " " and self.map[position[0]][position[1]] != "x" and self.map[position[0]][position[1]] != "M":
            if self.map[position[0]][position[1]] != "G":
                self.mac.pick_item(self.map[position[0]][position[1]])
            else:
                if self.mac.is_bag_full():
                    print("Gagné !")
                else:
                    print("Perdu :(")
                self.game = False

    def move_sprite(self, name, before, after):
        self.map[before[0]][before[1]] = " "
        self.map[after[0]][after[1]] = name
