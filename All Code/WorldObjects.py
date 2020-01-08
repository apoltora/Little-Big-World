#This file keeps track of class objects
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 204, 255)
BROWN = (128, 64, 0)
LIGHTBLUE = (204, 238, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 153, 51)
LAVENDER = (198, 26, 255)
LAVARED = (153, 51, 0)
GRAY = (153, 153, 153)

screenWidth = 1300
screenHeight = 800

pygame.init()
size = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)

goomba = pygame.image.load("goomba.gif")
ghost = pygame.image.load("ghost.png")
sharkLeft = pygame.image.load("sharkLeft.png")
sharkRight = pygame.image.load("sharkRight.png")

class Enemy(pygame.sprite.Sprite):
    xVector = 0
    yVector = 0
 
    topBoundary = 0
    bottomBoundary = 0
    leftBoundary = 0
    rightBoundary = 0

    player = None
 
    level = None

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        self.rect.x += self.xVector
        self.rect.y += self.yVector
        if hit:
            self.player.lives -= 1
            self.player.alive = False
            return
        if self.rect.bottom > self.bottomBoundary or self.rect.top < self.topBoundary:
            self.yVector *= -1
        currentPosition = self.rect.x - self.level.worldShiftX
        if currentPosition < self.leftBoundary or currentPosition > self.rightBoundary:
            self.xVector *= -1

class TopKillEnemy(Enemy):
    xVector = 0
    yVector = 0
 
    topBoundary = 0
    bottomBoundary = 0
    leftBoundary = 0
    rightBoundary = 0

    player = None
 
    level = None

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        self.rect.x += self.xVector
        self.rect.y += self.yVector
        if hit:
            #for top then kills
            #10 is to account for any error/glitches
            if self.rect.top + 20 >= self.player.rect.bottom:
                self.player.score += 1
                self.enemies.remove(self)
                return
            else:
                self.player.lives -= 1
                self.player.alive = False
                return
        if self.rect.bottom > self.bottomBoundary or self.rect.top < self.topBoundary:
            self.yVector *= -1
        currentPosition = self.rect.x - self.level.worldShiftX
        if currentPosition < self.leftBoundary or currentPosition > self.rightBoundary:
            self.xVector *= -1
        #checks collisions between fellow enemies
        self.enemies.remove(self)
        enemiesCollision = pygame.sprite.spritecollideany(self, self.enemies, None)
        if enemiesCollision != None:
            self.xVector *= -1
        self.enemies.add(self)

class SeaUrchin(Enemy):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.player.lives -= 1
            self.enemies.remove(self)
            if self.player.lives == 0:
                self.player.alive = False

class StalkerShark(Enemy):

    player = None
 
    level = None

    def __init__(self, width, height, waterHeightBeg, waterHeightEnd):
        super().__init__(width, height)
        self.waterHeightBeg = waterHeightBeg
        self.waterHeightEnd = waterHeightEnd
        self.image.fill(WHITE)

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        self.rect.x -= self.width
        inWaterLeft = pygame.sprite.spritecollide(self, self.water, False)
        self.rect.x += self.width

        self.rect.x += self.width
        inWaterRight = pygame.sprite.spritecollide(self, self.water, False)
        self.rect.x -= self.width

        if hit:
            self.player.lives -= 1
            self.player.alive = False
            return
        diffX = self.player.rect.x - self.rect.x
        diffY = self.player.rect.y - self.rect.y
        if inWaterLeft:
            if diffX < 0:
                screen.blit(sharkLeft, (self.rect.x,self.rect.y))
                self.image = sharkLeft
                self.rect.x -= 2
        if inWaterRight:
            if diffX > 0:
                self.rect.x += 2
                screen.blit(sharkRight, (self.rect.x,self.rect.y))
                self.image = sharkRight
        if self.rect.top > self.waterHeightBeg:
            if diffY < 0:
                self.rect.y -= 2
        if self.rect.bottom < self.waterHeightEnd:
            if diffY > 0:
                self.rect.y += 2

class ChaserGhost(Enemy):
    player = None
 
    level = None

    def __init__(self, width, height, topBound, bottomBound):
        super().__init__(width, height)
        self.topBound = topBound
        self.bottomBound = bottomBound
        self.image.fill(GRAY)

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.player.lives -= 1
            self.player.alive = False
            return
        diffX = self.player.rect.x - self.rect.x
        diffY = self.player.rect.y - self.rect.y
        if diffX < 0:
            self.rect.x -= 2
        if diffX > 0:
            self.rect.x += 2
        if diffY < 0:
            self.rect.y -= 2
        if diffY > 0:
            self.rect.y += 2


class ShootingEnemy(Enemy):
    def __init__(self, width, height, directionX, directionY):
        super().__init__(width, height)
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.time = 0
        self.directionX = directionX
        self.directionY = directionY

    def update(self):
        collision = pygame.sprite.collide_rect(self.player, self)
        if collision:
            self.player.lives -= 1
            self.player.alive = False
            return
        self.time += 1
        if self.directionY > 0:
            if self.time % 180 == 0:
                pellet = Pellet()
                pellet.rect.x = (self.rect.right + self.rect.left) // 2
                pellet.rect.y = self.rect.bottom
                pellet.xVector = self.directionX
                pellet.yVector = self.directionY
                self.level.pellets.add(pellet)
        if self.directionX < 0:
            if self.time % 180 == 0:
                pellet = Pellet()
                pellet.rect.x = self.rect.left
                pellet.rect.y = (self.rect.bottom + self.rect.top) // 2
                pellet.xVector = self.directionX
                pellet.yVector = self.directionY
                self.level.pellets.add(pellet)
        if self.directionX > 0:
            if self.time % 180 == 0:
                pellet = Pellet()
                pellet.rect.x = self.rect.right
                pellet.rect.y = (self.rect.bottom + self.rect.top) // 2
                pellet.xVector = self.directionX
                pellet.yVector = self.directionY
                self.level.pellets.add(pellet)
        for pellet in self.level.pellets:
            if pygame.sprite.spritecollideany(pellet, self.level.platforms) != None:
                self.level.pellets.remove(pellet)

class Coin(pygame.sprite.Sprite):
    player = None
    level = None
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height

    def update(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.player.score += 1
            self.coins.remove(self)
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(BROWN)
 
        self.rect = self.image.get_rect()
 
 
class MovingPlatform(Platform):
    xVector = 0
    yVector = 0
 
    topBoundary = 0
    bottomBoundary = 0
    leftBoundary = 0
    rightBoundary = 0
 
    player = None
 
    level = None
 
    def update(self):
        self.rect.x += self.xVector
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.xVector < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
        self.rect.y += self.yVector
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.yVector < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        if self.rect.bottom > self.bottomBoundary or self.rect.top < self.topBoundary:
            self.yVector *= -1
        currentPosition = self.rect.x - self.level.worldShiftX
        if currentPosition < self.leftBoundary or currentPosition > self.rightBoundary:
            self.xVector *= -1

class Water(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

class Tube(pygame.sprite.Sprite):
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()

class Pellet(pygame.sprite.Sprite):
    player = None
    Level = None
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.xVector = 0
        self.yVector = 0

    def update(self):
        self.rect.x += self.xVector
        self.rect.y += self.yVector

class Fireball(Pellet):
    level = None
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.xVector = 0
        self.yVector = 0

    def update(self):
        self.rect.x += self.xVector
        self.rect.y += self.yVector

class Wings(pygame.sprite.Sprite):
    player = None
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        if pygame.sprite.collide_rect(self, self.player):
            self.player.wings = True
            self.wings.remove(self)

class LavaBreath(pygame.sprite.Sprite):
    player = None
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([300,150])
        self.image.fill(LAVARED)
        self.rect = self.image.get_rect()
        self.xVector = 0

    def update(self):
        self.rect.x += self.xVector

class FinalBoss(Enemy):
    xVector = 0
    yVector = 0
 
    topBoundary = 0
    bottomBoundary = 0
    leftBoundary = 0
    rightBoundary = 0

    player = None
 
    level = None

    def __init__(self, width, height):
        super().__init__(width, height)
        self.lives = 30
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.time = 0
        self.alive = True

    def update(self):
        if pygame.sprite.collide_rect(self, self.player):
            self.player.lives -= 1
            self.player.alive = False
            return
        self.time += 1
        if self.time % 700 == 0:
            #breath out lava
            for lavaDrop in range(5):
                lava = LavaBreath()
                lava.rect.right = self.rect.left
                lava.rect.y = self.rect.top
                lava.xVector += -3
                self.lavaBreath.add(lava)
        if self.time % 200 == 0:
            #creating a walking goomba
            henchman = TopKillEnemy(40,50)
            henchman.rect.right = self.rect.x
            henchman.rect.y = screenHeight - 100
            screen.blit(goomba,(henchman.rect.x,henchman.rect.y-10))
            henchman.image = goomba
            henchman.leftBoundary = 50
            henchman.rightBoundary = screenWidth - 90
            henchman.xVector = -3
            henchman.player = self.player
            henchman.level = self.level
            self.enemies.add(henchman)
            henchman.enemies = self.enemies
        if self.time % 500 == 0:
            #summon stalker ghost
            foe = ChaserGhost(50,50,50,screenHeight-50)
            foe.rect.x = self.rect.x - 50
            foe.rect.y = self.rect.y - 50
            screen.blit(ghost, (foe.rect.x, foe.rect.y))
            foe.image = ghost
            foe.player = self.player
            foe.level = self.level
            self.enemies.add(foe)
            self.stalkers.add(foe)
            foe.enemies = self.enemies
            foe.platforms = self.platforms

class GainLife(pygame.sprite.Sprite):
    player = None
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(LAVENDER)
        self.rect = self.image.get_rect()

    def update(self):
        if pygame.sprite.collide_rect(self, self.player):
            self.player.lives += 1
            self.gainLives.remove(self)