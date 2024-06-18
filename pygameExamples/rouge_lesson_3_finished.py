import pygame, sys, os
from enum import Enum
import numpy as np

# Set up pygame screen
pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)

# Enumeration for different tile types in the map. We'll use this instead of raw numbers like we did in the last lesson.
# This makes it easier to add new tile types later if we want without changing code!!
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

    map_height = 10
    map_width = 10

    try:
        file = open(filename)

        lines = [line.rstrip() for line in file.readlines()]

        print("File opened")

        # If the file doesn't have any lines it's not a valid map_grid.
        assert len(lines) > 0

        # Updating map_width and map_height based on what we read from the file.
        map_width = max([len(line) for line in lines])
        map_height = len(lines)

        map_grid = np.full((map_height, map_width), TileType.EMPTY.value)

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                for type in TileType:
                    if char in TILE_TYPE_DICT[type]:
                        map_grid[row, col] = type.value
                        break

        print("Valid")
        return map_grid



    except (OSError, AssertionError):
        print("Map file not found or invalid, using default grid.")
        return np.full((map_height, map_width), TileType.GROUND.value)



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
#------------#--#
#--#######---#--########
#--#-----#---#---------#
#--#--S--#-E-#--#--##--###
#--#-----#---#--#--#E--#E#
######-#######--#--##--###
#----------------------#
########################
##

loaded_map = load_map("one-room.txt")

map_height, map_width = loaded_map.shape

clock = pygame.time.Clock()

# Game loop
while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    for row, col in np.ndindex(loaded_map.shape):
        color = TILE_COLOR_DICT[TileType(loaded_map[row, col])]
        rect = tile_rect((col, row))
        screen.fill(color, rect=rect)

    pygame.display.flip()