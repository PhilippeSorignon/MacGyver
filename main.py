from Map import *

map = Map()

while map.get_game():
    map.move_player(input("Où souhaitez vous aller ?"))
