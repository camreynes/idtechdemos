import pygame, sys
from pygame import key

pygame.init() #initialize pygame

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
#making width and height of screen

bg_color = (255,255,255) #making background color

spriteX = 10 #this is the initial x position of the sprite
spriteY = 40 #initial y position
spriteWidth = 640
spriteHeight = 640
sprite = pygame.image.load('images/slush.png')
enemy_image = pygame.image.load('images/enemy.png')

sprite = pygame.transform.scale(sprite, (spriteWidth, spriteHeight))
enemy_image = pygame.transform.scale(enemy_image, (500,500))
spriteColor = (90, 231, 125) #Green

spriteObject = pygame.Rect(spriteX, spriteY, spriteWidth, spriteHeight)

speed = 10

clock = pygame.time.Clock()
fps = 24

def draw_sprites():
    screen.blit(sprite,spriteObject)

#MAIN GAME LOOP
while True:
    clock.tick(fps)

    #this for loop gets every input from the user and every event in the game
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_w]: #if the key pressed is w
            spriteObject.move_ip(0,-speed)
        if key[pygame.K_s]:
            spriteObject.move_ip(0,speed)
        if key[pygame.K_a]:
            spriteObject.move_ip(-speed,0)
        if key[pygame.K_d]:
            spriteObject.move_ip(speed,0)

        if event.type == pygame.QUIT:
            sys.exit()
            #this if condition checks if the user is trying to quit the program and if they are
            #we use sys.exit() to close the window
    screen.fill(bg_color)
    draw_sprites()

    pygame.display.flip() #updates screen