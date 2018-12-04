class MacGyver:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.bag = ["", "", ""]

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

    def move(self, position):
        self.position = position


    def is_bag_full(self):
        return self.bag[2] != ""


    def pick_item(self, item):
        for i in range(0, 3):
            if self.bag[i] == "":
                self.bag[i] = item
                break

    def show_bag(self):
        return self.bag
