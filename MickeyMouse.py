# import modules
import pygame, random, math
pygame.init()
SIZE = (800, 600)

# Constants for colours and their RGB values
WHITE = (255, 255, 255)
BLACK = (0,0,0)
TAN = (250,231,218)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (17, 172, 250)
GREEN = (2, 219, 60)
DARKG = (0, 148, 40)
VIOLET = (47, 35, 176)
PURPLE = (240, 127, 250)
MAROON = (135, 23, 11)
BROWN = (165, 42, 42)
GREY = (192, 196, 204)
FOREST = (9, 71, 31)
PINEG = (61, 168, 25)
DARKYELLOW = (204, 198, 39)
DARKGREY = (141, 140, 145)
ORANGE = (237, 114, 69)

# Blue Colours for Sky
COLOUR1 = (50, 109, 168)
COLOUR2 = (50, 131, 168)
COLOUR3 = (50, 146, 168)
COLOUR4 = (50, 162, 168)
COLOUR5 = (80, 217, 210)
COLOUR6 = (111, 232, 226)
COLOUR7 = (165, 232, 242)

# Opens the pygame window
screen = pygame.display.set_mode(SIZE)

running = True
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False

# Sky in its different shades of blue
    pygame.draw.rect(screen, COLOUR1, pygame.Rect(0, 0, 800, 100))
    pygame.draw.rect(screen, COLOUR2, pygame.Rect(0, 50, 800, 100))
    pygame.draw.rect(screen, COLOUR3, pygame.Rect(0, 100, 800, 100))
    pygame.draw.rect(screen, COLOUR4, pygame.Rect(0, 150, 800, 100))
    pygame.draw.rect(screen, COLOUR5, pygame.Rect(0, 200, 800, 100))
    pygame.draw.rect(screen, COLOUR6, pygame.Rect(0, 250, 800, 100))
    pygame.draw.rect(screen, COLOUR7, pygame.Rect(0, 300, 800, 100))
    
# Background Grass    
    pygame.draw.rect(screen, DARKG, pygame.Rect(0, 350, 800, 200))
    pygame.draw.rect(screen, GREEN, pygame.Rect(0, 420, 800, 200))   

# Background flowers function with parameters
    def drawFlower(screen, x, y):
        pygame.draw.circle(screen, VIOLET, (170+x,90+y), 15)
        pygame.draw.circle(screen, VIOLET, (130+x,90+y), 15)
        pygame.draw.circle(screen, VIOLET, (150+x,70+y), 15)
        pygame.draw.circle(screen, VIOLET, (150+x,110+y),15)
        pygame.draw.circle(screen, YELLOW, (150+x,90+y), 10)
    
    drawFlower(screen, 20, 400)
    drawFlower(screen, 420, 350)  
    
# Random Colour Generator for flowers
    rand_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    def drawColour(screen, x, y):
        pygame.draw.circle(screen, rand_color, (110+x,410+y), 10)
        pygame.draw.circle(screen, rand_color, (90+x,410+y), 10)
        pygame.draw.circle(screen, rand_color, (100+x,400+y), 10)
        pygame.draw.circle(screen, rand_color, (100+x,420+y),10)
        pygame.draw.circle(screen, YELLOW, (100+x,410+y), 5)
    
    drawColour(screen, -50, 45)
    drawColour(screen, 620, 90)
  
# Displaying Purple Bird in background   
    def drawBird():
        # Legs for the bird 
        pygame.draw.line(screen, BROWN, (105, 115), (105, 135), 2) 
        pygame.draw.line(screen, BROWN, (85, 115), (85, 135), 2)
        
        # Feet for the bird 
        pygame.draw.line(screen, BROWN, (100, 135), (115, 135), 2) 
        pygame.draw.line(screen, BROWN, (77, 135), (92, 135), 2) 
        
        # Body of Bird
        pygame.draw.polygon(screen, PURPLE, [[100,120], [100,95], [135,110]])
        pygame.draw.polygon(screen, MAROON, [[75,110], [50,100], [110,100]])
        pygame.draw.ellipse(screen,PURPLE, pygame.Rect(70, 85, 55, 35))
        pygame.draw.circle(screen, MAROON, (80, 98), 3)
        
    drawBird()
    
# Displaying Orange Birds in background   
    def drawBird2(screen, x, y):
        # Legs for the bird 
        pygame.draw.line(screen, BROWN, (105+x, 115+y), (105+x, 135+y), 2) 
        pygame.draw.line(screen, BROWN, (85+x, 115+y), (85+x, 135+y), 2)
        
        # Feet for the bird 
        pygame.draw.line(screen, BROWN, (100+x, 135+y), (115+x, 135+y), 2) 
        pygame.draw.line(screen, BROWN, (77+x, 135+y), (92+x, 135+y), 2) 
        
        # Body of Bird
        pygame.draw.polygon(screen, ORANGE, [[100+x,120+y], [100+x,95+y], [135+x,110+y]])
        pygame.draw.polygon(screen, MAROON, [[75+x,110+y], [50+x,100+y], [110+x,100+y]])
        pygame.draw.ellipse(screen,ORANGE, pygame.Rect(70+x, 85+y, 55, 35))
        pygame.draw.circle(screen, MAROON, (80+x, 98+y), 3)
        
    drawBird2(screen, 150, 85)
    drawBird2(screen, 450, 120)
    
# Functions to display clusters of grass     
    def drawGrass(screen, x, y):
        pygame.draw.line(screen, FOREST, (425+x, 410+y), (430+x, 370+y), 2) 
        pygame.draw.line(screen, FOREST, (420+x, 410+y), (420+x, 370+y), 2) 
        pygame.draw.line(screen, FOREST, (415+x, 410+y), (410+x, 370+y), 2) 

    def drawLargeCluster(screen, x, y):
        drawGrass(screen, -395+x, 185+y)
        drawGrass(screen, -365+x, 195+y)
        drawGrass(screen, -335+x, 185+y)
        
    drawLargeCluster(screen, 0, 0)
    drawLargeCluster(screen, 190, 0)
    drawLargeCluster(screen, 380, 0)
    drawLargeCluster(screen, 570, 0)
    
    def drawOtherLargeCluster(screen, x, y):
        drawGrass(screen, -305+x, 195+y)
        drawGrass(screen, -270+x, 185+y)
        drawGrass(screen, -240+x, 195+y)
        
    drawOtherLargeCluster(screen, 0, 0)
    drawOtherLargeCluster(screen, 190, 0)
    drawOtherLargeCluster(screen, 380, 0)
    drawOtherLargeCluster(screen, 570, 0)
    
    def drawSmallCluster(screen, x, y):
        drawGrass(screen, 185+x, 95+y)
        drawGrass(screen, 210+x, 85+y)
        drawGrass(screen, 235+x, 95+y)
        
    drawSmallCluster(screen, -375, -20)
    drawSmallCluster(screen, 0, 20)
    
    drawGrass(screen, 360, 185)
    

# MICKEY MOUSE

# Mickey Mouse's Tail
    pygame.draw.arc(screen, BLACK, (365,230,130,190), 3*math.pi/2, 2*math.pi, 2)
    
# Mickey Mouse's right arm and hand
    pygame.draw.line(screen, BLACK, (520, 280), (420, 330), 18)
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(510, 265, 20, 30)) #vertical ellipse at base of hand
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(520, 267, 30, 8))
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(520, 275, 30, 8))
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(520, 283, 30, 8))
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(520, 290, 20, 8)) # pinky finger

# Mickey Mouse's left arm and hand
    pygame.draw.line(screen, BLACK, (280, 280), (380, 330), 18)
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(265, 260, 20, 30)) #vertical ellipse at base of hand
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(245, 262, 30, 8)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(245, 270, 30, 8)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(245, 278, 30, 8)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(252, 285, 20, 8))  # pinky finger
    
# Mickey Mouse's legs 
    pygame.draw.rect(screen, BLACK, pygame.Rect(372, 435, 15, 60))
    pygame.draw.rect(screen, BLACK, pygame.Rect(412, 435, 15, 60))    
    
# Mickey Mouse's yellow shoes    
    pygame.draw.ellipse(screen,YELLOW, pygame.Rect(400, 475, 60, 30))
    pygame.draw.ellipse(screen,YELLOW, pygame.Rect(330, 475, 60, 30))
        
# Mickey Mouse's body and pants
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(352, 250, 90, 180))
    pygame.draw.ellipse(screen,RED, pygame.Rect(345, 320, 105, 100))
    pygame.draw.ellipse(screen,RED, pygame.Rect(343, 345, 110, 100))
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(352, 299, 91, 70))
    
# Mickey Mouse's Pants' Buttons
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(370, 380, 20, 35)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(410, 380, 20, 35)) 

# Mickey Mouse's face    
    pygame.draw.circle(screen, BLACK, (400,210), 55)
    pygame.draw.ellipse(screen,TAN, pygame.Rect(398, 171, 45, 60)) 
    pygame.draw.ellipse(screen,TAN, pygame.Rect(358, 171, 45, 60)) 
    pygame.draw.ellipse(screen,TAN, pygame.Rect(367, 222, 65, 35))
    pygame.draw.circle(screen, TAN, (433,227),15)
    pygame.draw.circle(screen, TAN, (368,227), 15)
       
# Mickey Mouse's mouth 
    pygame.draw.arc(screen, BLACK, (365,178,68,75), math.pi, 3*math.pi/2, 2)
    pygame.draw.arc(screen, BLACK, (365,178,68,75), 3*math.pi/2, 2*math.pi, 2)
  
# Mickey Mouse's ears   
    pygame.draw.circle(screen, BLACK, (343,160), 25)
    pygame.draw.circle(screen, BLACK, (457,160), 25)

# Mickey Mouse's eyes
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(370, 182, 18, 31)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(410, 182, 18, 31)) 
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(373, 195, 11, 17)) 
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(413, 195, 11, 17)) 

# Mickey Mouse's nose
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(380, 210,38, 22))
    
    
# Clouds and Sun
    pygame.draw.ellipse(screen,YELLOW, pygame.Rect(550, 15, 125, 85))
    pygame.draw.ellipse(screen,DARKGREY, pygame.Rect(600, 65, 140, 45))
    pygame.draw.ellipse(screen,DARKGREY, pygame.Rect(500, 70, 140, 45))
    
# Trees in the background
    pygame.draw.rect(screen, BROWN, (615, 325, 20, 70))
    pygame.draw.polygon(screen, PINEG, [[670, 335], [625, 265], [580, 335]])
    pygame.draw.polygon(screen, PINEG, [[660, 295], [625, 215], [590, 295]])
    
    pygame.draw.rect(screen, BROWN, (770, 340, 15, 50))
    pygame.draw.polygon(screen, FOREST, [[800, 360], [775, 310], [750, 360]])
    pygame.draw.polygon(screen, FOREST, [[790, 330], [775, 290], [760, 330]]) 
    
    pygame.draw.rect(screen, BROWN, (730, 320, 15, 50))
    pygame.draw.polygon(screen, PINEG, [[760, 340], [735, 290], [710, 340]])
    pygame.draw.polygon(screen, PINEG, [[750, 310], [735, 270], [720, 310]]) 
    
    pygame.draw.rect(screen, BROWN, (690, 350, 15, 50))
    pygame.draw.polygon(screen, FOREST, [[720, 370], [695, 320], [670, 370]])
    pygame.draw.polygon(screen, FOREST, [[710, 340], [695, 300], [680, 340]]) 
    
    pygame.draw.rect(screen, BROWN, (548, 335, 15, 50))
    pygame.draw.polygon(screen, PINEG, [[580, 355], [555, 305], [530, 355]])
    pygame.draw.polygon(screen, PINEG, [[570, 325], [555, 285], [540, 325]]) 
    
    pygame.draw.rect(screen, BROWN, (175, 335, 20, 70))
    pygame.draw.polygon(screen, FOREST, [[230, 345], [185, 275], [140, 345]])
    pygame.draw.polygon(screen, FOREST, [[220, 305], [185, 225], [150, 305]])
    
    pygame.draw.rect(screen, BROWN, (270, 350, 15, 50))
    pygame.draw.polygon(screen, PINEG, [[300, 370], [275, 320], [250, 370]])
    pygame.draw.polygon(screen, PINEG, [[290, 340], [275, 300], [260, 340]]) 
        
# Clubhouse 
    pygame.draw.circle(screen, BLACK, (100,240), 20)
    pygame.draw.circle(screen, BLACK, (50,240), 20)
    pygame.draw.circle(screen, BLACK, (75,275), 30)
    pygame.draw.rect(screen, BLACK, (68, 280, 15, 30))
    pygame.draw.ellipse(screen,RED, pygame.Rect(28, 310, 100, 75))
    pygame.draw.ellipse(screen,YELLOW, pygame.Rect(105, 310, 30, 45))
    pygame.draw.ellipse(screen,YELLOW, pygame.Rect(105, 340, 30, 45))
    pygame.draw.ellipse(screen,DARKYELLOW, pygame.Rect(120, 360, 15, 20))
    pygame.draw.rect(screen, DARKG, (15, 350, 120, 40))
    
    
# Randomized position of clouds 
    randpos = (random.randint(525,650), 160, 130, 35)
    pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos))
    
    randpos2 = (random.randint(0,140), 25, 120, 45)
    pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos2))
    
    randpos3 = (random.randint(120,190), 120, 100, 30)
    pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos3))
    
    pygame.display.flip()
    pygame.time.wait(500)   
pygame.quit()
