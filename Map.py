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

        self.display()

    def display(self):
        for line in range(0, 15):
            line_tab = ""
            for column in range(0, 15):
                line_tab += self.map[line][column]
            print(line_tab)

    def is_empty(self, line, column):
        pass

    def move_sprite(self, before, after):
        pass
