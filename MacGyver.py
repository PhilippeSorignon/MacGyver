from Objects import *


class MacGyver(Objects):

    def __init__(self, name, position):
        Objects.__init__(self, name, position)


    def move(self, position):
        self.position = position


    def is_bag_full(self):
        pass

    def pick_item(self):
        pass
