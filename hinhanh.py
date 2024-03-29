import pygame
import os 

#Global Constants
gray=(119,118,110)
bright_gray = (0,255,0)
white = (255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
orange = (255,165,0)
bright_orange = (255, 160, 0)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
yellow = (255,255,0)
bright_yellow = (255,250,179)
dark_blue = (0,178,191)
bright_dark_blue = (0,146,152)
orange = (255, 165, 0)
pink = (197,0,35)
pause=False
clock = pygame.time.Clock()
pygame.mixer.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("picture/Dino", "DinoRun1.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join('picture/Dino', 'DinoJump.png'))

DUCKING = [pygame.image.load(os.path.join("picture/Dino", "DinoDuck1.png")), 
            pygame.image.load(os.path.join("picture/Dino", "DinoDuck2.png"))]

RUNNING_2 = [pygame.image.load(os.path.join("picture/Dino", "Dinosaur5.png")),
            pygame.image.load(os.path.join("picture/Dino", "Dinosaur6.png"))]

JUMPING_2 = pygame.image.load(os.path.join('picture/Dino', 'Dinosaur4.png'))


RUNNING_3 = [pygame.image.load(os.path.join("picture/Dino", "DinoChibi.png")), 
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi8.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi5.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi3.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi2.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi6.png")),
            pygame.image.load(os.path.join("picture/Dino", "DinoChibi4.png"))]

JUMPING_3 = pygame.image.load(os.path.join('picture/Dino', 'DinoChibiJump.png'))


OBSTACLE_1_1 = [pygame.image.load(os.path.join("picture/Cactus", "SmallCactus1.png")), 
            pygame.image.load(os.path.join("picture/Cactus", "SmallCactus2.png")),
            pygame.image.load(os.path.join("picture/Cactus", "SmallCactus3.png"))]

OBSTACLE_1_2 = [pygame.image.load(os.path.join("picture/Cactus", "LargeCactus1.png")), 
            pygame.image.load(os.path.join("picture/Cactus", "LargeCactus2.png")),
            pygame.image.load(os.path.join("picture/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("picture/Bird", "Bird1.png")), 
            pygame.image.load(os.path.join("picture/Bird", "Bird2.png"))]

OBSTACLE_2_1 = [pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-3.png")), 
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-1.png")),
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-3.png"))]

OBSTACLE_2_2 = [pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-4.png")), 
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-4.png")),
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_2-4.png"))]

OBSTACLE_3_1 = [pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-1.png")), 
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-1.png")),
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-2.png"))]

OBSTACLE_3_2 = [pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-1.png")), 
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-3.png")),
            pygame.image.load(os.path.join("picture/obstacle", "obstacle_4-1.png"))]

CLOUD = pygame.image.load(os.path.join('picture/Other', 'Cloud.png'))

BG = pygame.image.load(os.path.join('picture/background', 'bg_nen.jpg'))
BG_NEN = pygame.image.load(os.path.join('picture/Other', 'Track.png'))
BG1 = pygame.image.load(os.path.join('picture/background','bg9.jpg'))
BG2 = pygame.image.load(os.path.join('picture/background','anime2.png'))
BG3 = pygame.image.load(os.path.join('picture/background','bg14.png'))

background = pygame.image.load(os.path.join('./picture/background/bg6.jpg'))
background_menu = pygame.image.load(os.path.join('./picture/background/bg_dino1.jpg'))
background_name = pygame.image.load(os.path.join('./picture/background/bgdino1.jpg'))
intro_bg = pygame.image.load(os.path.join('./picture/background/bg-anime5.jpg'))
end_bg = pygame.image.load(os.path.join('./picture/background/dino.jpg'))
score_bg = pygame.image.load(os.path.join('./picture/background/bg8.jpg'))

FINISH = pygame.image.load("./picture/background/dino1.jpg")

sound1 = pygame.mixer.Sound('./Sound/nhacnen.mp3')
sound2 = pygame.mixer.Sound('./Sound/te.wav')
