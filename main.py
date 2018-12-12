from Map import *
import pygame


map = Map()

while map.get_game():
    for event in pygame.event.get():
        map.move_player(event)
