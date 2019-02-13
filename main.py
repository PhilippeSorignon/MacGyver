"""
    Main file
"""

import pygame

import map

MAP = map.Map()

while MAP.get_game():
    for event in pygame.event.get():
        MAP.move_player(event)
