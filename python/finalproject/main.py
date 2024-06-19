import pygame, sys

pygame.init() #initialize pygame

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
#making width and height of screen

bg_color = (255,255,255) #making background color

spriteX = 10 #this is the initial x position of the sprite
spriteY = 40 #initial y position
spriteWidth = 640
spriteHeight = 640
sprite = pygame.image.load('images/slush.png')
sprite = pygame.transform.scale(sprite, (spriteWidth, spriteHeight))

spriteColor = (90, 231, 125) #Green

def draw_sprites():
    screen.blit(sprite,(spriteX,spriteY))

#MAIN GAME LOOP
while True:
    #this for loop gets every input from the user and every event in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #this if condition checks if the user is trying to quit the program and if they are
            #we use sys.exit() to close the window
    screen.fill(bg_color)
    draw_sprites()

    pygame.display.flip() #updates screen