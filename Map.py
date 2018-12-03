import random
from MacGyver import *


class Map:
    def __init__(self):
        self.map = []
        map_file = open("map.txt", "r")
        lines = map_file.readlines()

        for read_line in lines:
            tab = []
            for i in range(0, 15):
                tab.append(read_line[i])
            self.map.append(tab)

        mac = MacGyver("M", self.select_random_empty_sprite())
        self.move_sprite(mac.get_name(), mac.get_position(), mac.get_position())

        self.display()

    def display(self):
        for line in range(0, 15):
            line_tab = ""
            for column in range(0, 15):
                line_tab += self.map[line][column]
            print(line_tab)

    def is_empty(self, line, column):
        return self.map[line][column] != "x"

    def select_random_empty_sprite(self):
        line = 0
        column = 0

        while self.map[line][column] == "x":
            line = random.randint(0, 15)
            column = random.randint(0, 15)

        return [line, column]


    def move_sprite(self, name, before, after):
        self.map[before[0]][before[1]] = " "
        self.map[after[0]][after[1]] = name
