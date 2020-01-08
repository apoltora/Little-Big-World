#This file creates the player class
import pygame
from WorldObjects import *
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 204, 255)
BROWN = (128, 64, 0)
LIGHTBLUE = (204, 238, 255)
YELLOW = (255, 255, 0)
screenWidth = 1300
screenHeight = 800

fireballLeft = pygame.image.load("fireballLeft.png")
fireballRight = pygame.image.load("fireballRight.png")

class Player(pygame.sprite.Sprite):
    #outside of init because init restarts the game to position that works
    lives = 3
    score = 0
    def __init__(self):
        super().__init__()
        width = 40
        height = 40
        self.image = pygame.Surface([width, height],pygame.SRCALPHA)
        self.image.fill((255,255,255,128))
        self.rect = self.image.get_rect()

        self.xVector = 0
        self.yVector = 0
        self.level = None
        self.alive = True
        self.wings = False
 
    def update(self):
        waterHit = pygame.sprite.spritecollide(self, self.level.water, False)
        if len(waterHit) > 0:
            self.calcBouyancy()
        else:
            self.calcGrav()
        self.rect.x += self.xVector
        blocksHit = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in blocksHit:
            if self.xVector > 0:
                self.rect.right = block.rect.left
            elif self.xVector < 0:
                self.rect.left = block.rect.right
        self.rect.y += self.yVector
        blocksHit = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in blocksHit:
            if self.yVector > 0:
                self.rect.bottom = block.rect.top
            elif self.yVector < 0:
                self.rect.top = block.rect.bottom
            self.yVector = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.xVector
        if self.rect.y >= screenHeight:
            self.lives -= 1
            self.alive = False
            return
 
    def calcGrav(self):
        if self.yVector == 0:
            self.yVector = 1
        else:
            self.yVector += .40
        if self.rect.y >= screenHeight + self.rect.height and self.yVector >= 0:
            self.yVector = 0
            self.rect.y = screenHeight
            self.previousLives = self.lives
            self.lives -= 1
            if self.lives < self.previousLives:
            #should restart
                #falling music potentially?
                # pygame.init()
                # pygame.mixer.music.load('FallingSound.mp3')
                # pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                # pygame.mixer.music.play()
                if self.lives == 0:
                    self.alive = False

    def calcBouyancy(self):
        waterHit = pygame.sprite.spritecollide(self, self.level.water, False)
        if len(waterHit)>0:
            self.yVector += .40 #the jump under water
        if self.rect.y >= screenHeight + self.rect.height and self.yVector >= 0:
            self.yVector = 0
            self.rect.y = screenHeight
 
    def jump(self):
        self.rect.y += 2
        platformHit = pygame.sprite.spritecollide(self, self.level.platforms, False)
        self.rect.y -= 2
        waterHit = pygame.sprite.spritecollide(self, self.level.water, False)
        if self.wings == True: #but change_y changes then can make character fly/double jump
            self.yVector = -10
        if len(platformHit) > 0 and len(waterHit) == 0: #or self.rect.bottom >= SCREEN_HEIGHT:
            self.yVector = -10
        #so can work harded to "jump" in the water
        #"swimming"
        elif len(waterHit) > 0:
            self.yVector = -8
 
    def go_left(self):
        waterHit = pygame.sprite.spritecollide(self, self.level.water, False)
        #goes slower in water
        if len(waterHit) > 0:
            self.xVector = -4
        else:
            self.xVector = -5

 
    def go_right(self):
        waterHit = pygame.sprite.spritecollide(self, self.level.water, False)
        #goes slower in water
        if len(waterHit) > 0:
            self.xVector = 4
        else:
            self.xVector = 5
 
    def stop(self):
        self.xVector = 0

    def shoot(self, directionX, directionY):
        fireball = Fireball()
        fireball.rect.y = (self.rect.top + self.rect.bottom) // 2
        if directionX > 0:
            fireball.rect.x = self.rect.right
            screen.blit(fireballRight, (fireball.rect.x, fireball.rect.y))
            fireball.image = fireballRight
        if directionX < 0:
            fireball.rect.x = self.rect.left
            screen.blit(fireballLeft, (fireball.rect.x, fireball.rect.y))
            fireball.image = fireballLeft
        fireball.xVector = directionX
        fireball.yVector = directionY
        self.level.fireballs.add(fireball)
            


    def __repr__(self):
        return "this many lives %d" % (self.lives)
 