import Map
import pygame


MAP = Map.Map()

while MAP.get_game():
    for event in pygame.event.get():
        MAP.move_player(event)
