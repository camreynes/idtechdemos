import pygame, sys
from pygame import key

pygame.init() #initialize pygame

score = 0

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
score_ui = pygame.Rect(0,0,width,50)

#making width and height of screen

bg_color = (255,255,255) #making background color

spriteX = 10 #this is the initial x position of the sprite
spriteY = 40 #initial y position
spriteWidth = 100
spriteHeight = 100
sprite = pygame.image.load('images/slush.png')
enemy_image = pygame.image.load("images/enemy.png")
coin = pygame.image.load("images/coin.png")


sprite = pygame.transform.scale(sprite, (spriteWidth, spriteHeight))
enemy_image = pygame.transform.scale(enemy_image, (100,100))
coin = pygame.transform.scale(coin,(80,80))
spriteColor = (90, 231, 125) #Green

spriteObject = pygame.Rect(spriteX, spriteY, 40, 40)
enemyObject = pygame.Rect(spriteX+200, spriteY+200, 40,40)
coinObject = [pygame.Rect(300,300,40,40),
              pygame.Rect(400,400,40,40)]
coinVis = [True, True]

speed = 10

clock = pygame.time.Clock()
fps = 24

def draw_sprites():
    screen.blit(sprite,spriteObject)
    if (coinVis[0]):
        screen.blit(coin,coinObject[0])
    if (coinVis[1]):
        screen.blit(coin, coinObject[1])

    pygame.draw.rect(screen,(0,0,0),score_ui)
    draw_text(("Score: " + str(score)), pygame.font.SysFont("",30),(255,255,255),10,10)

def draw_text(text,font,color,x,y):
    image = font.render(text,True,color)
    screen.blit(image,(x,y))

    global score
    for i, coins in enumerate(coinObject):
        if coins.colliderect(spriteObject): #if we touch a coin
            coinVis[i] = False

def draw_enemies():
    screen.blit(enemy_image,enemyObject)
    if spriteObject.colliderect(enemyObject): #these two lines of code will detect collision and end the program
                                              #if the enemies collide
        sys.exit()

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
    # pygame.draw.rect(screen, (0, 0, 255), spriteObject) #HOW TO DRAW HITBOX
    draw_sprites()
    draw_enemies()

    pygame.display.flip() #updates screen