#This file is the set up of the first level
import pygame
from Level import *
from WorldObjects import *
screenWidth = 1300
screenHeight = 800
LIGHTBLUE = (204, 238, 255)

class Level01(Level):
 
    def __init__(self, player):
        goomba = pygame.image.load("goomba.gif")
        cloud = pygame.image.load("cloud.png")
        seaUrchin = pygame.image.load("seaUrchin.png")
        squid = pygame.image.load("squid.png")
        cactusUpright = pygame.image.load("cactus.png")
        cactusUpsideDown = pygame.image.load("cactusUpsideDown.png")
        sharkLeft = pygame.image.load("sharkLeft.png")
        coinPic = pygame.image.load("coin.png")
        wings = pygame.image.load("wings.png")
        treasureChest = pygame.image.load("treasureChest.png")
        Level.__init__(self, player)
        self.levelWidth = -8000
 
        # Array with width, height, x, and y of platform
        flooring = [[1900, screenHeight, -2100, 0], #left wall
        [100, screenHeight//5, -200, -100], #secret upper
        [100, screenHeight, -200, screenHeight*2//5-200], #secret lower
        [2100, 50, -100, screenHeight-50], #regular flooring
        [1000, 50, 1000, screenHeight-100], #up a level on regular flooring
        [50, 50, 1350, screenHeight-200], #block next to coin
        [50, 50, 1450, screenHeight-200], #block next to coin
        [50, 50, 1550, screenHeight-200], #block next to coin
        [50, 50, 1650, screenHeight-200], #block next to coin
        [1000, 50, 2000, screenHeight-20], #water flooring
        [1000, 100, 3000, screenHeight-100], #flooring after water before tunnel
        [1000, screenHeight//2, 3500, 0], #upper tunnel
        [1000, screenHeight//3, 3500, screenHeight*3//4], #lower tunnel
        [70, screenHeight-screenHeight*4//5+100, 5170, screenHeight*4//5-100], #first column
        [70, screenHeight-screenHeight*4//5+200, 5370, screenHeight*4//5-200], #second column
        [70, screenHeight-screenHeight*4//5+300, 5570, screenHeight*4//5-300], #third column
        [60,20,5640,screenHeight-50], #ledge in water to hold gain a life
        [screenWidth*2, 540, 8000, 0], #top end column (above tube)
        [screenWidth*2, 500, 8000, screenHeight*4//5], #bottom end column (below tube)
        [8200,50,-200,-50]] #top layer so doesn't go above screen
 
        # Go through the array above and add platforms
        for platform in flooring:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platforms.add(block)


        tubesList = [[screenWidth*2, 100, 8000, 540]]

        for t in tubesList:
        	tube = Tube(t[0],t[1])
        	tube.rect.x = t[2]
        	tube.rect.y = t[3]
        	tube.player = self.player
        	self.tubes.add(tube)


        #x and y positions
        coinsList = [[1400, screenHeight-200],
                    [1500, screenHeight-200],
                    [1600, screenHeight-200],
                    #in water
                    [6230, 440], [6300, 440],
                    [6370, 440], [6440, 440],
                    [6820, 540], [6890, 540],
                    [6960, 540], [7030, 540],
                    [7410, 640], [7480, 640],
                    [7550, 640], [7620, 640]]

        for c in coinsList:
            coin = Coin(50,50)
            coin.rect.x = c[0]
            coin.rect.y = c[1]
            screen.blit(coinPic, (coin.rect.x, coin.rect.y))
            coin.image = coinPic
            coin.player = self.player
            coin.coins = self.coins
            self.coins.add(coin)


        waves = [[1000, 100, 2000, screenHeight-100],
                 [2360, screenHeight-screenHeight*4//5+400, 5640, screenHeight*4//5-300]]

        for wave in waves:
            block = Water(wave[0], wave[1])
            block.rect.x = wave[2]
            block.rect.y = wave[3]
            block.player = self.player
            self.water.add(block)

        ##### Moving Platforms #####

        #moving platforms
        #first side ways platform
        block1 = MovingPlatform(70, 40)
        block1.rect.x = 4500
        block1.rect.y = screenHeight*2//3
        block1.leftBoundary = 4500
        block1.rightBoundary = 4700
        block1.xVector = 1
        block1.player = self.player
        block1.level = self
        self.platforms.add(block1)

        #second upwards/downwards platform
        block2 = MovingPlatform(70, 40)
        block2.rect.x = 4800
        block2.rect.y = 300
        block2.topBoundary = screenHeight//5
        block2.bottomBoundary = screenHeight*2//3
        block2.yVector = -1
        block2.player = self.player
        block2.level = self
        self.platforms.add(block2)

        block3 = MovingPlatform(70, 40)
        block3.rect.x = -100
        block3.rect.y = screenHeight//5
        block3.topBoundary = screenHeight//5
        block3.bottomBoundary = screenHeight-100
        block3.yVector = -1
        block3.player = self.player
        block3.level = self
        self.platforms.add(block3)

        ##### Enemies #####

        #first side ways enemy
        enemy1 = TopKillEnemy(40,50)
        enemy1.rect.x = 1000
        enemy1.rect.y = screenHeight-150
        screen.blit(goomba,(enemy1.rect.x,enemy1.rect.y-10))
        enemy1.image = goomba
        enemy1.leftBoundary = 1000
        enemy1.rightBoundary = 1960
        enemy1.xVector = 3
        enemy1.player = self.player
        enemy1.level = self
        self.enemies.add(enemy1)
        enemy1.enemies = self.enemies

        #first upwards/downwards enemy
        #first column
        enemy2 = Enemy(70,60)
        enemy2.rect.x = 5270
        enemy2.rect.y = screenHeight*4//5-320
        screen.blit(cloud,(enemy2.rect.x, enemy2.rect.y))
        enemy2.image = cloud
        enemy2.topBoundary = screenHeight*4//5-320
        enemy2.bottomBoundary = screenHeight-100
        enemy2.yVector = -10
        enemy2.player = self.player
        enemy2.level = self
        self.enemies.add(enemy2)
        enemy2.enemies = self.enemies

        #second upwards/downwards enemy
        #second column
        enemy3 = Enemy(70,60)
        enemy3.rect.x = 5470
        enemy3.rect.y = screenHeight*4//5-400
        screen.blit(cloud,(enemy3.rect.x, enemy3.rect.y))
        enemy3.image = cloud
        enemy3.topBoundary = screenHeight*4//5-400
        enemy3.bottomBoundary = screenHeight-200
        enemy3.yVector = -10
        enemy3.player = self.player
        enemy3.level = self
        self.enemies.add(enemy3)
        enemy3.enemies = self.enemies

        #cactus at beginning of game
        enemy4 = Enemy(40,80)
        enemy4.rect.x = 600
        enemy4.rect.y = screenHeight-150
        screen.blit(cactusUpright,(enemy4.rect.x,enemy4.rect.y))
        enemy4.image = cactusUpright
        self.enemies.add(enemy4)
        enemy4.enemies = self.enemies
        enemy4.player = self.player
        enemy4.level = self

        #cacti in tunnel
        enemy14 = Enemy(50,100)
        enemy14.rect.x = 3750
        enemy14.rect.y = screenHeight*3//4-100
        screen.blit(cactusUpright,(enemy14.rect.x,enemy14.rect.y))
        enemy14.image = cactusUpright
        self.enemies.add(enemy14)
        enemy14.enemies = self.enemies
        enemy14.player = self.player
        enemy14.level = self

        enemy15 = Enemy(50,100)
        enemy15.rect.x = 4100
        enemy15.rect.y = screenHeight*3//4-100
        screen.blit(cactusUpright,(enemy15.rect.x,enemy15.rect.y))
        enemy15.image = cactusUpright
        self.enemies.add(enemy15)
        enemy15.enemies = self.enemies
        enemy15.player = self.player
        enemy15.level = self

        enemy16 = Enemy(50,100)
        enemy16.rect.x = 3925
        enemy16.rect.y = screenHeight//2
        screen.blit(cactusUpsideDown,(enemy16.rect.x,enemy16.rect.y))
        enemy16.image = cactusUpsideDown
        self.enemies.add(enemy16)
        enemy16.enemies = self.enemies
        enemy16.player = self.player
        enemy16.level = self
        #end of cacti


        #fellow to first sideways enemy
        enemy5 = TopKillEnemy(40,50)
        enemy5.rect.x = 1500
        enemy5.rect.y = screenHeight-150
        screen.blit(goomba,(enemy5.rect.x,enemy5.rect.y))
        enemy5.image = goomba
        enemy5.leftBoundary = 1000
        enemy5.rightBoundary = 1960
        enemy5.xVector = 3
        enemy5.player = self.player
        enemy5.level = self
        self.enemies.add(enemy5)
        enemy5.enemies = self.enemies

        #right most sea urchin... goes in following order to left
        #in first water
        enemy6 = SeaUrchin(10,10)
        enemy6.rect.x = 2900
        enemy6.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy6.rect.x,enemy6.rect.y-10))
        enemy6.image = seaUrchin
        enemy6.player = self.player
        enemy6.level = self
        self.enemies.add(enemy6)
        enemy6.enemies = self.enemies

        enemy7 = SeaUrchin(10,10)
        enemy7.rect.x = 2880
        enemy7.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy7.rect.x,enemy7.rect.y-10))
        enemy7.image = seaUrchin
        enemy7.player = self.player
        enemy7.level = self
        self.enemies.add(enemy7)
        enemy7.enemies = self.enemies

        enemy8 = SeaUrchin(10,10)
        enemy8.rect.x = 2860
        enemy8.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy8.rect.x,enemy8.rect.y-10))
        enemy8.image = seaUrchin
        enemy8.player = self.player
        enemy8.level = self
        self.enemies.add(enemy8)
        enemy8.enemies = self.enemies

        enemy9 = SeaUrchin(10,10)
        enemy9.rect.x = 2840
        enemy9.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy9.rect.x,enemy9.rect.y-10))
        enemy9.image = seaUrchin
        enemy9.player = self.player
        enemy9.level = self
        self.enemies.add(enemy9)
        enemy9.enemies = self.enemies

        enemy10 = SeaUrchin(10,10)
        enemy10.rect.x = 2820
        enemy10.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy10.rect.x,enemy10.rect.y-10))
        enemy10.image = seaUrchin
        enemy10.player = self.player
        enemy10.level = self
        self.enemies.add(enemy10)
        enemy10.enemies = self.enemies

        enemy11 = SeaUrchin(10,10)
        enemy11.rect.x = 2800
        enemy11.rect.y = screenHeight - 30
        screen.blit(seaUrchin,(enemy11.rect.x,enemy11.rect.y-10))
        enemy11.image = seaUrchin
        enemy11.player = self.player
        enemy11.level = self
        self.enemies.add(enemy11)
        enemy11.enemies = self.enemies

        #end of sea urchins in first water

        # in water swimming around
        enemy12 = Enemy(30,30)
        enemy12.rect.x = 2500
        enemy12.rect.y = screenHeight - 50
        screen.blit(squid,(enemy12.rect.x,enemy12.rect.y-10))
        enemy12.image = squid
        enemy12.leftBoundary = 2150
        enemy12.rightBoundary = 2540
        enemy12.xVector = -4
        enemy12.player = self.player
        enemy12.level = self
        self.enemies.add(enemy12)
        enemy12.enemies = self.enemies

        #stalker shark in sea
        #pseudo AI
        enemy13 = StalkerShark(70,35, screenHeight*4//5-300, screenHeight)
        enemy13.rect.x = 5800
        enemy13.rect.y = screenHeight - 60
        screen.blit(sharkLeft,(enemy13.rect.x,enemy13.rect.y))
        enemy13.image = sharkLeft
        enemy13.player = self.player
        enemy13.level = self
        self.enemies.add(enemy13)
        enemy13.enemies = self.enemies
        enemy13.water = self.water

        wing = Wings()
        wing.rect.x = -200
        wing.rect.y = screenHeight*2//5-230
        screen.blit(wings, (wing.rect.x, wing.rect.y))
        wing.image = wings
        self.wings.add(wing)
        wing.wings = self.wings
        wing.player = self.player

        gainLife = GainLife()
        gainLife.rect.x = 5640
        gainLife.rect.y = screenHeight - 80
        screen.blit(treasureChest, (gainLife.rect.x, gainLife.rect.y))
        gainLife.image = treasureChest
        self.gainLives.add(gainLife)
        gainLife.gainLives = self.gainLives
        gainLife.player = self.player

        

    def draw(self, screen):
        screen.fill(LIGHTBLUE)
        super().draw(screen)

    def update(self):
        super().update()