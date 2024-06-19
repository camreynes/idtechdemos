import pygame, sys

pygame.init() #initialize pygame

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
#making width and height of screen

bg_color = (45,76,180) #making background color

sprite = pygame.image.load('images/slush.png')
spriteX = 10 #this is the initial x position of the sprite

#MAIN GAME LOOP
while True:
    #this for loop gets every input from the user and every event in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #this if condition checks if the user is trying to quit the program and if they are
            #we use sys.exit() to close the window
    screen.fill(bg_color)
    pygame.display.flip() #updates screen