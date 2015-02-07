import pygame
import time
import random


pygame.init()

#width and height of the screen
display_width = 800
display_height = 600

#RGB colours 
BLACK = (0,  0,  0)
WHITE = (255,  255,  255)
RED = (255,  0,  0)
GREEN = (0,  255,  0)
BLUE = (0,  0,  255)
ORANGE = (255,  128,  0)
LIGHT_GREEN = (0,  200,  0)
LIGHT_RED = (185,  0,  0)
LIGHT_ORANGE = (200,  130,  0)
block_colour = (55, 255, 200)

banana_width = 32


appDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Health4FUN')
clock = pygame.time.Clock()

#getting image for player
player1 = pygame.image.load('banana.png')
    
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count),True, BLACK)
    appDisplay.blit(text,(0,0))


def things(thingx, thingy, thingw, thingh,colour):
    number_of_things = pygame.draw.rect(appDisplay, colour, [thingx, thingy, thingw, thingh])
       
def banana(x,y):
    appDisplay.blit(player1,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def fruitinfo(text, display_height, font):
    textSurf, textRect = text_objects(text, font)
    textRect.center = ((display_width/2),(display_height/2))
    appDisplay.blit(textSurf, textRect)

def message_display(text):
    largeText = pygame.font.Font('AGENCYR.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    appDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    app_loop()

def crash():
    message_display('You Died')

def Info():
    into = True
    

    while into:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
                
                
        
        appDisplay.fill(WHITE)
        midText = pygame.font.Font('AGENCYR.ttf',35)
        smallText = pygame.font.Font("AGENCYR.ttf", 20)
        largeText = pygame.font.Font('AGENCYR.ttf',100)
        TextSurf, TextRect = text_objects("Banana", largeText)
        TextRect.center = ((display_width/2),(display_height/2+-250))
        fruitinfo("Nutritional value per 100 g (3.5 oz)", 275,midText)
        fruitinfo("Energy: 371 kJ (89 kcal)",350,smallText)
        fruitinfo("Carbohydrates 22.84 g",400,smallText)
        fruitinfo("Dietary fiber: 2.6 g",450,smallText)
        fruitinfo("Fat: 0.33 g",500,smallText)
        fruitinfo("Protein: 1.09 g",550,smallText)
        
        appDisplay.blit(TextSurf, TextRect)
        button("Back",50, 450, 100,50,LIGHT_RED,RED, "Back")
        pygame.display.update()

        

    

    

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(appDisplay, ic, (x, y, w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                app_loop()
            elif action == "info":
                Info()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "Back":
                app_intro()
            elif action == "mainmenu":
                app_intro()
                
                
    else:
        pygame.draw.rect(appDisplay, ac, (x, y, w,h))

    smallText = pygame.font.Font("AGENCYR.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    appDisplay.blit(textSurf, textRect)






def app_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
##        print (event)
        
           
        appDisplay.fill(WHITE)
        largeText = pygame.font.Font('AGENCYR.ttf',115)
        TextSurf, TextRect = text_objects("Health4FUN", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        appDisplay.blit(TextSurf, TextRect)

        button("Start",150, 450, 100,50,LIGHT_GREEN,GREEN, "play")
        button("Info",350, 450, 100,50,LIGHT_ORANGE,ORANGE, "info")
        button("Quit",550, 450, 100,50,LIGHT_RED,RED, "quit")
        

        pygame.display.update()
        clock.tick(120)


    
def app_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
   
    dodged = 0

    

    appExit = False
    paused = False

    while not appExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   paused = not paused
        if paused:
            largeText = pygame.font.Font('AGENCYR.ttf',100)
            TextSurf, TextRect = text_objects("Paused", largeText)
            TextRect.center = ((display_width/2),(display_height/2+-250))
            appDisplay.blit(TextSurf, TextRect)
            button("Menu",100, 150, 100,50,LIGHT_RED,RED, "mainmenu")



            pygame.display.update()

            
        else:
            appDisplay.fill(WHITE)
            things(thing_startx, thing_starty, thing_width, thing_height, block_colour)
            thing_starty += thing_speed
            banana(x,y)
            things_dodged(dodged)
        
        x += x_change

        
        if x > display_width - banana_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 0.45)
            if thing_speed > 15:
                thing_speed = 14
            

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + banana_width > thing_startx and x + banana_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(120)

        






app_intro()

pygame.quit()
quit()

