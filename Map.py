import random
from MacGyver import *


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
        tube = self.select_random_empty_sprite()
        ether = self.select_random_empty_sprite()
        guard = self.select_random_empty_sprite()
        self.move_sprite("n", needle, needle)
        self.move_sprite("t", tube, tube)
        self.move_sprite("e", ether, ether)
        self.move_sprite("G", guard, guard)

        map_file.close()

        self.display()

    def display(self):
        for line in range(0, 15):
            line_tab = ""
            for column in range(0, 15):
                line_tab += self.map[line][column]
            print(line_tab)

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

    def move_player(self, direction):
        pos = self.mac.get_position()

        if direction == "n" and pos[0] - 1 >= 0 and self.is_empty(pos[0] - 1, pos[1]):
            self.verify_object([pos[0] - 1, pos[1]])
            self.move_sprite(self.mac.get_name(), self.mac.get_position(), [pos[0] - 1, pos[1]])
            self.mac.move([pos[0] - 1, pos[1]])

        elif direction == "s" and pos[0] + 1 >= 0 and self.is_empty(pos[0] + 1, pos[1]):
            self.verify_object([pos[0] + 1, pos[1]])
            self.move_sprite(self.mac.get_name(), self.mac.get_position(), [pos[0] + 1, pos[1]])
            self.mac.move([pos[0] + 1, pos[1]])

        elif direction == "e" and pos[1] + 1 >= 0 and self.is_empty(pos[0], pos[1] + 1):
            self.verify_object([pos[0], pos[1] + 1])
            self.move_sprite(self.mac.get_name(), self.mac.get_position(), [pos[0], pos[1] + 1])
            self.mac.move([pos[0], pos[1] + 1])

        elif direction == "o" and pos[1] - 1 >= 0 and self.is_empty(pos[0], pos[1] - 1):
            self.verify_object([pos[0], pos[1] - 1])
            self.move_sprite(self.mac.get_name(), self.mac.get_position(), [pos[0], pos[1] - 1])
            self.mac.move([pos[0], pos[1] - 1])

        if self.game:
            self.display()
            print(self.mac.show_bag())

    def verify_object(self, position):
        if self.map[position[0]][position[1]] != " " and self.map[position[0]][position[1]] != "x":
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
