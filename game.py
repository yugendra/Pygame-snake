import pygame
import time
import random

pygame.init()

white = (255,255,255)
lightsalmon = (255,160,122)
salmon = (250,128,114)
red = (255,0,0)
green = (34,177,76)
blue = (0,0,255)
black = (0,0,0)

#display params
height=600
width=800



gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Python')

img = pygame.image.load('snakehead.png')


#for appearance of motion like a flipbook, update entire frame 
#updates only desired area on the surface(frame)
#pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
direction = "right"

def snake(change_factor,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],change_factor,change_factor])

def text_objects(msg,color):
    surf = font.render(msg,True,color)
    return surf , surf.get_rect()
    
    

def message_to_screen(msg,color):
    textSurface, textRect = text_objects(msg,color)
    gameDisplay.fill(white)
    textRect.center = (width/2),(height/2)
    gameDisplay.blit(textSurface,textRect)
    
    #screen_text = font.render(msg,True,color)
    #gameDisplay.blit(screen_text, [width/2 - 200 , height/2])
    pygame.display.update()
    
        
def gameloop():
    gameExit= False
    gameOver= False
    lead_x = width/2
    lead_y = height/2
    lead_x_change=0
    lead_y_change=0
    prev_key = "null"
    global direction
    change_factor=20
    clockTick=14
    snakelist = []
    snakeLength =1
    AppleThickness = 30


    randAppleY = round(random.randrange(0,height-AppleThickness)/10.0)*10.0
    randAppleX = round(random.randrange(0,width-AppleThickness)/10.0)*10.0
  

    while not gameExit:
        while gameOver == True:
            message_to_screen("Press c to start over or q to quit", red)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit=True
                    gameOver= False
                    message_to_screen("BuhBye!!",red)
                if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_q:
                        gameExit=True
                        gameOver= False
                      if event.key == pygame.K_c:
                        gameloop()
                 
                          
        for event in pygame.event.get():        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and prev_key != "right":
                    lead_x_change = -change_factor
                    lead_y_change = 0
                    prev_key = "left"
                    direction="left"
                if event.key == pygame.K_RIGHT and prev_key != "left":
                    lead_x_change = change_factor
                    lead_y_change = 0
                    prev_key = "right"
                    direction="right"
                if event.key == pygame.K_UP and prev_key != "down":
                    lead_y_change = -change_factor
                    lead_x_change=0
                    prev_key = "up"
                    direction = "up" 
                if event.key == pygame.K_DOWN and prev_key != "up":
                    lead_y_change = change_factor
                    lead_x_change=0
                    prev_key = "down"
                    direction="down"
                    
             
            if event.type == pygame.QUIT:
                gameExit=True
                message_to_screen("BuhBye!!",red)
                time.sleep(2)

        if lead_x >= width or lead_x <= 0 or lead_y >= height or lead_y <= 0:
            #gameExit=True
            gameOver=True

        lead_x += lead_x_change
        lead_y += lead_y_change
       
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, blue, [randAppleX,randAppleY,AppleThickness,AppleThickness])

        
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakeLength:
            del snakelist[0]
        
        for element in snakelist[:-1]:
            if element == snakehead:
                gameOver = True
            
        
        snake(change_factor,snakelist)
        pygame.display.update()
##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleY = round(random.randrange(0,height-AppleThickness)/10.0)*10.0
##                randAppleX = round(random.randrange(0,width-AppleThickness)/10.0)*10.0
##                snakeLength += 1


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + change_factor > randAppleX and lead_x + change_factor < randAppleX + AppleThickness:
            print("X crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                print("Y crossover")
                randAppleY = round(random.randrange(0,height-AppleThickness)/10.0)*10.0
                randAppleX = round(random.randrange(0,width-AppleThickness)/10.0)*10.0
                snakeLength += 1
            elif lead_y + change_factor > randAppleY and lead_y + change_factor < randAppleY + AppleThickness:
                print("X and Y crossover")
                randAppleY = round(random.randrange(0,height-AppleThickness)/10.0)*10.0
                randAppleX = round(random.randrange(0,width-AppleThickness)/10.0)*10.0
                snakeLength += 1
                
            

        clock.tick(clockTick)
        
    pygame.quit()
    quit()
    
gameloop()
