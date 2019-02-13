"""
    macgyver.py
"""

class MacGyver:
    """
        Contains all informations and usefull classes about the player
    """
    def __init__(self, name, position):
        """
            Initialisation
        """
        self.name = name
        self.position = position
        self.bag = [1, 1, 1]

    def get_position(self):
        """
            Return the player's position
        """
        return self.position

    def get_name(self):
        """
            Return the name
        """
        return self.name

    def move(self, position):
        """
            Update the position with a new one
        """
        self.position = position


    def is_bag_full(self):
        """
            Return true if the bag is full or false if it's not
        """
        return self.bag[2] != 1


    def pick_item(self, item):
        """
            Pick an item and put it in the bag
        """
        for i in range(0, 3):
            if self.bag[i] == 1:
                self.bag[i] = item
                break

    def show_bag(self):
        """
            Show the bag's content
        """
        return self.bag
