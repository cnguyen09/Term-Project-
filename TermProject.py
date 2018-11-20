import pygame
import random
import librosa

from module_manager import * 
# import module_manager
# module_manager.review()
################################################################################
################### Initialize the program #####################################
#Passing values into init function
pygame.init()
windowWidth = 500
windowHeight = 800
#Setting up the width and height of the game window
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Tap Tap to The Beats")
clock = pygame.time.Clock()
fps = 20

#Set up some initial variables:
numberOfLanes = 3

################################################################################
######################## Color Chart ###########################################
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PERUBROWN = (205, 133, 63)
BLACK = (0, 0, 0)
################################################################################
#################### Play background music #####################################
# pygame.mixer.init()
# song = "Ariana Grande - thank u, next (audio).mp3"
# musicLib = pygame.mixer.music.load(song)
# pygame.mixer.music.play()
################################################################################
##################### Classify components of the game ##########################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.center = (windowWidth//2, windowHeight//2)
        self.velocity = 5
    
    def move(self):
        self.rect.y -= self.velocity
        if self.rect.top < 0:
            self.rect.bottom = windowHeight

class Beat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, windowWidth - 15), 15)
        self.velocity = 5
    
    def move(self):
        self.rect.y += self.velocity

class BowlingLane(pygame.sprite.Sprite):
    def __init__(self):
        #Ratio of distance of bowling lane from the upper top:
        self.ratioY = 1 / 15
        pygame.sprite.Sprite.__init__(self)
        self.color = PERUBROWN
        self.width = windowWidth / numberOfLanes
        self.height = windowHeight
        self.topX = 4 * windowWidth / 10
        self.topY = windowHeight * self.ratioY
        self.disXTop = (windowWidth - 2 * self.topX) / numberOfLanes
        self.botX = 1 * windowWidth / 10
        self.botY = windowHeight
        self.disXBot = (windowWidth - 2 * windowWidth / 10) / numberOfLanes
    
    def drawLane(self):
        pointList = [(self.topX, self.topY), (self.botX, self.botY,), \
     (windowWidth - self.botX, self.botY), (windowWidth - self.topX, self.topY)]
        pygame.draw.polygon(gameDisplay, PERUBROWN, pointList)
        pygame.draw.line(gameDisplay, BLACK, (self.topX, self.topY),\
                                                      (self.botX, self.botY), 2)
    
    def drawBorder(self):
        for i in range(numberOfLanes):
            startX = self.topX + self.disXTop * i
            startY = self.topY 
            endX = self.botX + self.disXBot * i
            endY = self.botY
            pygame.draw.line(gameDisplay, BLACK, (startX, startY),\
                                                                (endX, endY), 2)
        
################################################################################
#################### Create Player on the screen ###############################
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

################################################################################
##################### Create beats on the screen ###############################
all_beats = pygame.sprite.Group()
beat1 = Beat()
beat2 = Beat()
beat3 = Beat()
all_beats.add(beat1, beat2, beat3)

################################################################################
##################### Create bowling lanes #####################################
bowlingLane = BowlingLane()

################################################################################
##################### Create the main loop for the game ########################
# Always set up an infinit loop to make sure the game is going. 
# Stop when it's told to.
timePassed = 0
running = True
while running:
    #Never run faster than #frames per second
    # clock.tick(fps) #similar to timerDelay
    countTime = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.rect.x > 0:
            player.rect.x -= player.velocity
    elif keys[pygame.K_RIGHT]:
        if player.rect.x < windowWidth - 50:
            player.rect.x += player.velocity
    elif keys[pygame.K_UP]:
        if player.rect.y > 0:
            player.rect.y -= player.velocity
    elif keys[pygame.K_DOWN]:
        if player.rect.y < windowHeight:
            player.rect.y += player.velocity
    
    gameDisplay.fill((0, 0, 0))
    
    # Draw bowling lane
    bowlingLane.drawLane()
    
    
    #Draw border for the lanes:
    bowlingLane.drawBorder()
    
    #Draw the player 
    all_sprites.draw(gameDisplay)
    for sprite in all_sprites:
        sprite.move()
        
    #Draw all of the beats
    all_beats.draw(gameDisplay)
    for beat in all_beats:
        beat.move()
        if beat.rect.bottom > windowHeight:
            beat.rect.top = 0
    
    pygame.display.flip()
    
pygame.quit()


