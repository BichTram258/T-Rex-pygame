#from numpy import true_divide
import pygame
import os
import random
from hinhanh import *
from Dinosaur import *
from Cloud import *


pygame.init()
class Obstacle:
    
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
            
            

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird (Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    global pause
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font .Font("freesansbold.ttf",20)
    obstacles = []
    death_count = 0
    create_name = True

    def score():
        global points, game_speed
        try:
            highestScore = int(getHighestScore())
        except:
            highestScore = 0

        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render('Scores: ' + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

        if(highestScore < points):
            highestScore = points
        with open("highest score.txt","w") as f:
            f.write(str(highestScore))

        text1 = font.render('Highest Scores: ' + str(highestScore), True, red)
        textRect = text1.get_rect()
        textRect.center = (800, 40)
        SCREEN.blit(text1, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    text1 = font.render( create_name(), True, red)
    textRect = text1.get_rect()
    textRect.center = (800, 40)
    SCREEN.blit(text1, textRect)

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pause=True
        

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()
        
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                #pygame.draw.rect(SCREEN, (255, 0, 0), player.dino_rect, 2)
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()
        button("Pause",50,0,150,50,blue,bright_blue,"pause")
        
        score()
        
        clock.tick(30)
        pygame.display.update()

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(SCREEN,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                main()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                menu(death_count=0)
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()
            elif action == "name":
                create_name()
    else:
        pygame.draw.rect(SCREEN,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    SCREEN.blit(textsurf,textrect)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            SCREEN.blit(background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
            SCREEN.blit(TextSurf,TextRect)
            button("CONTINUE",250,450,150,50,green,bright_green,"unpause")
            button("RESTART",450,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",650,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        SCREEN.blit(intro_bg,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("You need to jumping and ducking overcome obstacles to gain more points",smalltext)
        textRect.center=((550),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((550),(100))
        SCREEN.blit(TextSurf,TextRect)
        SCREEN.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects(" K_UP : JUMPING",smalltext)
        stextRect.center=((450),(400))
        hTextSurf,hTextRect=text_objects(" K_DOWN : DUCKING" ,smalltext)
        hTextRect.center=((450),(450))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((450),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((500),(250))
        SCREEN.blit(sTextSurf,sTextRect)
        SCREEN.blit(stextSurf,stextRect)
        SCREEN.blit(hTextSurf,hTextRect)
        SCREEN.blit(ptextSurf,ptextRect)
        button("BACK",800,520,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)

def create_name():
    create_name = True

    input_rect = pygame.Rect(440, 300, 160, 40)
    color= pygame.Color(43, 31, 216)
    base_font = pygame.font.Font('freesansbold.ttf', 32)
    user_text = ''


    while create_name:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0:-1]
                    else:
                        user_text += event.unicode

        SCREEN.blit(background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',60)
        #smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        
        
        textSurf,textRect=text_objects("What are your name?",mediumtext)
        textRect.center=((550),(230))
        TextSurf,TextRect=text_objects("CREATE TO NAME GAME!",largetext)
        TextRect.center=((550),(150))
        SCREEN.blit(TextSurf,TextRect)
        SCREEN.blit(textSurf,textRect)


        pygame.draw.rect(SCREEN, color, input_rect, 2)

        text_surface = base_font.render(user_text, True, (43, 31, 216))
        #textRect = text_surface.get_rect()
        #textRect.center(550, 300)
        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(200, text_surface.get_width() + 10)

        button("OK",800,520,200,50,red,bright_red,"play")
        button("BACK",100,520,200,50,green,bright_green,"menu")
        pygame.display.flip()
        clock.tick(60)



def getHighestScore():
    with open("highest score.txt","r") as f:
        return f.read()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            SCREEN.blit(background_2,(0,0))
            #font1 = pygame.font.Font('freesansbold.ttf',115)
            #text = font1.render('T-REX', True, black)
            largetext=pygame.font.Font('freesansbold.ttf',100)
            text = largetext.render('T-REX', True, (59, 48, 49))
            text_rect = largetext.render('T-REX', True, (59, 48, 49))
            textRect = text_rect.get_rect()
            #text,textRect=text_objects("T-REX",largetext)
            textRect.center=((550),(230))
            SCREEN.blit(text_rect, textRect)
            button("START",300,430,100,50,green,bright_green,"play")
            button("QUIT",700,430,100,50,red,bright_red,"quit")
            button("INSTRUCTION",450,430,200,50,yellow,bright_yellow,"intro")
            button("CREATE NAME", 450, 350, 200, 50, dark_blue, bright_dark_blue, "name")
        elif death_count > 0:
            SCREEN.blit(end_bg,(0,0))
            text = font.render('Press any Key to restart', True, (0, 0, 0))
            score = font.render('Your Score: ' + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()

menu(death_count=0)


