import pygame
from pygame import mixer
import time
import math
import pickle
import random

#initialize pygame
pygame.init()
mixer.init()


death = False

# create screen
display_width = 960
display_height = 960


counter = 0
joe = 0
screen = pygame.display.set_mode((display_width, display_height))

#Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('001-snake.png').convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
crashed = False
running = True

playerImg = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (40, 40))

border = pygame.image.load('Black_Box.png').convert_alpha()
border = pygame.transform.scale(border, (40, 960))
border2 = pygame.image.load('Black_Box.png').convert_alpha()
border2 = pygame.transform.scale(border, (960, 40))

warning1 = pygame.image.load('warning.png').convert_alpha()
warning2 = pygame.image.load('warning2.png').convert_alpha()

global index

index = None



body_x0 = -40
body_y0 = -40
body_x1 = -40
body_y1 = -40

playerX = 370 
playerY = 370

global food_x
global food_y

food_x = 500
food_y = 400



body_p = pygame.image.load('pixil-frame-0.png').convert_alpha()
body_p = pygame.transform.scale(body_p, (40, 40))

snakebody = []
snakebody_x = []
snakebody_y = []


global rightcq
global leftcq
global upcq
global downcq
rightcq = 1
leftcq = 1
upcq = 1
downcq = 1


def figuremovement(event):
    
    global rightcq
    global leftcq
    global upcq
    global downcq
    global playerX
    global playerY

    Rightmovement = False
    Leftmovement = False
    Upmovement = False
    Downmovement = False
    
    if rightcq == 0:
        Leftmovement = True
    if leftcq == 0:
        Rightmovement = True
    if downcq == 0:
        Upmovement = True
    if upcq == 0:
        Downmovement = True


    if rightcq == 1:        
        if event.key == pygame.K_RIGHT:
            x_change = (45)
            
           
            Rightmovement = True 
            Leftmovement = False
            Upmovement = False
            Downmovement = False
            leftcq = 0
            rightcq = 1
            upcq = 1
            downcq = 1
          
    if leftcq == 1:
        if event.key == pygame.K_LEFT:
            x_change = (45)* -1
            
            
            Leftmovement = True 
            Rightmovement = False
            Upmovement = False
            Downmovement = False
            rightcq = 0
            leftcq = 1
            upcq = 1
            downcq = 1
            

    if upcq == 1:       
        if event.key == pygame.K_UP:
            y_change = 45 * -1
            Rightmovement = False 
            Leftmovement = False
            Upmovement = True
            Downmovement = False
            downcq = 0
            leftcq = 1
            rightcq = 1
            upcq = 1
            

    if downcq == 1:
        if event.key == pygame.K_DOWN:
            y_change = 45
            Rightmovement = False
            Leftmovement = False
            Upmovement = False
            Downmovement = True
            upcq = 0
            leftcq = 1
            rightcq = 1
            downcq = 1
           

    return(Leftmovement, Rightmovement, Upmovement, Downmovement, rightcq, leftcq, upcq, downcq)
    

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))
    
    
a1 = 134
a2 = 146
a3 = 74

cake = pygame.image.load('Piece-of-cake-icon.png').convert_alpha()
cake = pygame.transform.scale(cake, (40, 40))

apple = pygame.image.load('Apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (40, 40))

banana = pygame.image.load('Banana.png').convert_alpha()
banana = pygame.transform.scale(banana, (40, 40))

peach = pygame.image.load('Peach.png').convert_alpha()
peach = pygame.transform.scale(peach, (40, 40))

cherry = pygame.image.load('Cherry.png').convert_alpha()
cherry = pygame.transform.scale(cherry, (40, 40))

durian = pygame.image.load('Durian.png').convert_alpha()
durian = pygame.transform.scale(durian, (40, 40))

orange = pygame.image.load('Orange.png').convert_alpha()
orange = pygame.transform.scale(orange, (40, 40))

pear = pygame.image.load('Pear.png').convert_alpha()
pear = pygame.transform.scale(pear, (40, 40))

decider = 1

def food_spawn():
    
    eaten = False
    
    global food_x
    global food_y
    global a1
    global a2
    global a3
    global decider

    food_x = random.randint(80, 880)
    food_y = random.randint(80, 880)

    decider = random.randint(1,7)

    a1 = random.randint(0, 255)
    a2 = random.randint(0, 255)
    a3 = random.randint(0, 255)
   
    x = 400
    y = 300
    


    
    
    snakebody.append(body_p)
    snakebody_x.append(body_x1)
    snakebody_y.append(body_y1)
    if score == 2:
        snakebody.append(body_p)
        snakebody_x.append(body_x1)
        snakebody_y.append(body_y1)

    if score > 0:
        mixer.music.load('Eat_Munch_2_Sound.mp3')
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Eat_Munch_2_Sound.mp3'))


curr_direction_X = None


score = 0

myfont = pygame.font.SysFont("astigmatic", 30)
diefont = pygame.font.SysFont("astigmatic", 90)
menufont = pygame.font.SysFont("astigmatic", 60)

menu = True
game = False

sound = True

while running == True:
   
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    while menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                death = False
                running = False
                menu = False
                game = False
        if sound == True:
            pygame.mixer.Channel(2).fadeout(1000)
            
        mainmenu = pygame.image.load('snake_menu.jpg').convert_alpha()
        mainmenu = pygame.transform.scale(mainmenu, (960, 960))
        try:
            with open('score.dat', 'rb') as file:
                high_score = pickle.load(file)
        except:
            high_score = 0
        screen.blit(mainmenu, (0,0))
        menu_high_scoretext = menufont.render("High Score = "+str(high_score), 1, (0,0,0))
        screen.blit(menu_high_scoretext, (600, 850))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                menu = False
                game = True
                death = False   


        pygame.display.update()
        clock.tick(30)
        
        
         


    while death == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                death = False
                running = False
                game = False
                menu = False
        pygame.mixer.Channel(0).stop()
        with open('score.dat', 'wb') as file:
            pickle.dump(high_score, file)


        

        gameover = pygame.image.load('32847539f3d1e018a00145a3848f67e8.jpg').convert_alpha()
        gameover = pygame.transform.scale(gameover, (960, 960))
        screen.blit(gameover, (0,0))
        scoretext_dead = diefont.render("Score = "+str(score), 1, (255,255,255))
        screen.blit(scoretext_dead, (350, 730))
        high_scoretext_dead = diefont.render("High Score = "+str(high_score), 1, (255,255,255))
        screen.blit(high_scoretext_dead, (275, 800))
        if sound == False:
            pygame.mixer.music.load('Game.mp3')
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('Game.mp3'))
            
            sound = True
       
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_ESCAPE:
                
                death = False
                menu = True
                game = False
                score = 0
                snakebody = []
                snakebody_x = []
                snakebody_y = []
                body_x0 = 0
                body_y0 = 0
                body_x1 = 0
                body_y1 = 0
                a1 = 134
                a2 = 146
                a3 = 74

                playerX = 360 
                playerY = 360


                food_x = 500
                food_y = 400
                curr_direction_X = None
                Rightmovement = False
                Leftmovement = False
                Upmovemnet = False
                Downmovement = False
                rightcq = 1
                leftcq = 1
                upcq = 1
                downcq = 1
                sound = True
                
        pygame.display.update()
        

    
    
    if game == True:
        if sound == True:
            pygame.mixer.music.load('On_God.mp3')
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('On_God.mp3'),)
            
            sound = False  

        
        
        if score > high_score:
            high_score = score
        
        

        screen.fill((a1,a2,a3))

        distance = math.sqrt(((playerX - food_x)**2)+(playerY - food_y)**2)

        scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
        screen.blit(scoretext, (750, 50))

        high_scoretext = myfont.render("High Score = "+str(high_score), 1, (0,0,0))
        screen.blit(high_scoretext, (750, 80))

        player(playerX, playerY)

        if score < 30:
            if playerX > 920:
                playerX = 0
            if playerX < 0:
                playerX = 920
            if playerY > 920:
                playerY = 0
            if playerY < 0:
                playerY = 920
       
        
        if decider == 1:
            screen.blit(apple, (food_x, food_y))
        if decider == 2:
            screen.blit(pear, (food_x, food_y))
        if decider == 3:
            screen.blit(orange, (food_x, food_y))
        if decider == 4:
            screen.blit(durian, (food_x, food_y))
        if decider == 5:
            screen.blit(cherry, (food_x, food_y))
        if decider == 6:
            screen.blit(peach, (food_x, food_y))
        if decider == 7:
            screen.blit(banana, (food_x, food_y))


        if distance < 40:
            

            score = score + 1

            food_spawn()


        for index in range (len(snakebody_x)):

            if score > 3:
                if playerX == snakebody_x[index] and playerY == snakebody_y[index]:
                    
                    death = True
                    game = False

                    
                    
            if index != len(snakebody_x) - 1 :
                
                snakebody_x[index] = snakebody_x[index + 1]
            
                

                snakebody_y[index] = snakebody_y[index + 1]
                
                screen.blit(snakebody[index], (snakebody_x[index], snakebody_y[index]))

            snakebody_x[-1] = body_x0
            snakebody_y[-1] = body_y0
            screen.blit(snakebody[-1], (snakebody_x[-1], snakebody_y[-1]))
            
        body_x0 = playerX
        body_y0 = playerY


        if death == False:
            if event.type == pygame.KEYDOWN:
                
                
                (Leftmovement, Rightmovement, Downmovement, Upmovement, rightcq, leftcq, upcq, downcq) = figuremovement(event)
                
                if Rightmovement == True:
                    
                    playerX += 40
                    curr_direction_X = "right"
                    playerImg = pygame.image.load('pixil-frame-0 (1)right.png').convert_alpha()
                    
                if Leftmovement == True:
                    
                    playerX -= 40
                    curr_direction_X = "left"
                    playerImg = pygame.image.load('pixil-frame-0 (1)left.png').convert_alpha()
                    
                if Upmovement == True:
                    
                    playerY += 40
                    curr_direction_X = "up"
                    playerImg = pygame.image.load('pixil-frame-0 (1)down.png').convert_alpha()
            
                if Downmovement == True:
                    
                    playerY -= 40
                    curr_direction_X = "down"
                    playerImg = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()
                
                
            else:
                
                
                if curr_direction_X != None:
                    
                
                    if curr_direction_X == "right":
                        
                        playerX += 40
                        
                    if curr_direction_X == "left":
                        
                        playerX -= 40
                    
                    if curr_direction_X == "up":
                        
                        playerY += 40

                    if curr_direction_X == "down":
                        
                        playerY -= 40


        if score > 27 and score < 30:
            if counter % 30  == 0:
                screen.blit(warning1, (40, 40))
                joe += 1
                if joe % 2 == 0:
                    screen.blit(warning2, (40, 40))

                
        if score > 29:
            if playerX <= 0 or playerX >= 960:
                death = True
                game = False

            if playerY <= 0 or playerY >= 960:
                death = True
                game = False
            

            
            screen.blit(border, (0, 0))
            screen.blit(border, (920, 0))
            screen.blit(border2, (0, 0))
            screen.blit(border2, (0, 920))
        

        pygame.display.update()
        clock.tick(15)
        counter += counter
pygame.quit()
quit()
