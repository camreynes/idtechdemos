import pygame, sys, os
from enum import Enum
import numpy as np

# Set up pygame screen
pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)


# Enumeration for different tile types in the map. We'll use this instead of raw numbers like we did in the last lesson.
# This makes it easier to add new tile types later if we want without changing code!
class TileType(Enum):
    EMPTY = -1
    GROUND = 0
    WALL = 1


# Dict of what characters can represent each tile type, will be used when we load the map from a file.
TILE_TYPE_DICT = {
    TileType.EMPTY: " ",
    TileType.GROUND: "-SE",
    TileType.WALL: "#"
}

# Sets of RGB values. These will control what color each tile is when drawn to the screen.
TILE_COLOR_DICT = {
    TileType.EMPTY: (10, 10, 10),
    TileType.GROUND: (42, 86, 98),
    TileType.WALL: (7, 44, 54)
}


def load_map(filename):
    # TODO: Build a function that creates a grid map.

    return None


# Functions to make our lives drawing tiles easier.

# the width and height of a square tile in pixels.
tile_size = 16


# take a pixel postion (x,y) and convert it to a grid (x, y) we can use as an index in the grid map
def tile_position(pixel):
    tile_x, tile_y = pixel
    tile_x //= tile_size
    tile_y //= tile_size
    return tile_x, tile_y


# take a grid index (x, y) and return the pixel position. By default, returns the top left pixel position of the tile.
# if center=True, returns the center pixel position of the tile instead.
def pixel_position(tile, center=False):
    pixel_x, pixel_y = tile
    pixel_x *= tile_size
    pixel_y *= tile_size
    if center:
        pixel_x += tile_size // 2
        pixel_y += tile_size // 2
    return pixel_x, pixel_y


# gets a pygame Rect for a given tile (x, y) index for easy drawing
def tile_rect(tile):
    pixel_pos = pixel_position(tile)
    return pygame.Rect(pixel_pos, (tile_size, tile_size))


##
# Test Map - Copy this into a text file to test the loading once completed
#################
# ------------#--#
# --#######---#--########
# --#-----#---#---------#
# --#--S--#-E-#--#--##--###
# --#-----#---#--#--#E--#E#
######-#######--#--##--###
# ----------------------#
########################
##

# TODO: Set up game variables, load the map

clock = pygame.time.Clock()

# Game loop
while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    # TODO: Draw the map to the screen.

    pygame.display.flip()