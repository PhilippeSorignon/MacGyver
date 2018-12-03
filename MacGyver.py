from Objects import *


class MacGyver(Objects):

    def __init__(self, name, position):
        Objects.__init__(self, name, position)
        self.bag = ["", "", ""]


    def move(self, position):
        self.position = position


    def is_bag_full(self):
        pass

    def pick_item(self, item):
        for i in range(0, 3):
            if self.bag[i] == "":
                self.bag[i] = item
                break

    def show_bag(self):
        return self.bag
