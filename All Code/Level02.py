#This file is the set up of the second level
import pygame
from Level import *
from WorldObjects import *

screenWidth = 1300
screenHeight = 800
wings = pygame.image.load("wings.png")
coinPic = pygame.image.load("coin.png")
treasureChest = pygame.image.load("treasureChest.png")

class Level02(Level):

	def __init__(self, player):
		Level.__init__(self, player)

		self.levelWidth = -4000

		flooring = [[1000, screenHeight, -1000, 0], #left wall
		[2000, 50, 0, screenHeight-50], #regular flooring
		[900, screenHeight - 150, 100, 0], #above tube
		[900, 400, 1000, 0], #after tube above screen
		[100, 100, 1900, 0], #platform for gainLife
		[100, 200, 1900, 200], #platform for gainLife

		#the stairs
		[100, 150, 2000, screenHeight-150],
		[100, 250, 2100, screenHeight-250],
		[100, 350, 2200, screenHeight-350],
		[100, 450, 2300, screenHeight-450],
		[100, 550, 2400, screenHeight-550],
		#column after well
		[100, 550, 2650, screenHeight-550],

		#the jumps in the column well
		#on the left
		[50,50,2500,screenHeight-550],
		[50,50,2500,screenHeight-350],
		[50,50,2500,screenHeight-150],
		#on the right
		[50,50,2600,screenHeight-450],
		[50,50,2600,screenHeight-250],
		[50,50,2600,screenHeight-50],

		#after column ground dip
		[1000,450,2750,screenHeight-450],

		#two right columns
		[100,550,3750,screenHeight-550],
		[100,550,3850,screenHeight-550],
		#flooring under tube
		[2000, 50, 3950, screenHeight-50],
		#above tube
		[200,150,3850,0], [2000,650,4050,0],
		[4200, 50, 100, -50]] #above the screen so player doesnt go off

		for platform in flooring:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platforms.add(block)

		tubesList = [[1000,100,0,screenHeight-150],
					[100,screenHeight-150,0,0],
					[200,100,3850,screenHeight-650],
					[2000,100,3950,screenHeight-150],
					[100,500,3950,screenHeight-550]]

		for t in tubesList:
			tube = Tube(t[0],t[1])
			tube.rect.x = t[2]
			tube.rect.y = t[3]
			tube.player = self.player
			self.tubes.add(tube)

		        #x and y positions
		coinsList = [[3050,screenHeight-500],
					[3150, screenHeight-500],
					[3250, screenHeight-500],
					[3350, screenHeight-500]]

		for c in coinsList:
			coin = Coin(50,50)
			coin.rect.x = c[0]
			coin.rect.y = c[1]
			screen.blit(coinPic, (coin.rect.x, coin.rect.y))
			coin.image = coinPic
			coin.player = self.player
			coin.coins = self.coins
			self.coins.add(coin)

		#first shooter enemy
		enemy1 = ShootingEnemy(40, 40, 0, 1)
		enemy1.rect.x = 1100
		enemy1.rect.y = 400
		enemy1.player = self.player
		enemy1.level = self
		self.shootingEnemies.add(enemy1)
		self.enemies.add(enemy1)
		enemy1.enemies = self.enemies
		enemy1.pellets = self.pellets
		enemy1.platforms = self.platforms

		#second shooter enemy
		enemy2 = ShootingEnemy(40, 40, 0, 3)
		enemy2.rect.x = 1200
		enemy2.rect.y = 400
		enemy2.player = self.player
		enemy2.level = self
		self.shootingEnemies.add(enemy2)
		self.enemies.add(enemy2)
		enemy2.enemies = self.enemies
		enemy2.pellets = self.pellets
		enemy2.platforms = self.platforms

		enemy3 = ShootingEnemy(40, 40, 0, 8)
		enemy3.rect.x = 1300
		enemy3.rect.y = 400
		enemy3.player = self.player
		enemy3.level = self
		self.shootingEnemies.add(enemy3)
		self.enemies.add(enemy3)
		enemy3.enemies = self.enemies
		enemy3.pellets = self.pellets
		enemy3.platforms = self.platforms

		enemy4 = ShootingEnemy(40, 40, 0, 3)
		enemy4.rect.x = 1400
		enemy4.rect.y = 400
		enemy4.player = self.player
		enemy4.level = self
		self.shootingEnemies.add(enemy4)
		self.enemies.add(enemy4)
		enemy4.enemies = self.enemies
		enemy4.pellets = self.pellets
		enemy4.platforms = self.platforms

		enemy5 = ShootingEnemy(40, 40, 0, 1)
		enemy5.rect.x = 1500
		enemy5.rect.y = 400
		enemy5.player = self.player
		enemy5.level = self
		self.shootingEnemies.add(enemy5)
		self.enemies.add(enemy5)
		enemy5.enemies = self.enemies
		enemy5.pellets = self.pellets
		enemy5.platforms = self.platforms

		enemy6 = ShootingEnemy(40, 40, -1, 0)
		enemy6.rect.x = 3710
		enemy6.rect.y = screenHeight - 490
		enemy6.player = self.player
		enemy6.level = self
		self.shootingEnemies.add(enemy6)
		self.enemies.add(enemy6)
		enemy6.enemies = self.enemies
		enemy6.pellets = self.pellets
		enemy6.platforms = self.platforms

		enemy7 = ShootingEnemy(40, 40, -1, 0)
		enemy7.rect.x = 3750
		enemy7.rect.y = screenHeight - 590
		enemy7.player = self.player
		enemy7.level = self
		self.shootingEnemies.add(enemy7)
		self.enemies.add(enemy7)
		enemy7.enemies = self.enemies
		enemy7.pellets = self.pellets
		enemy7.platforms = self.platforms

		wing = Wings()
		wing.rect.x = 2600
		wing.rect.y = screenHeight-80
		screen.blit(wings, (wing.rect.x, wing.rect.y))
		wing.image = wings
		wing.wings = self.wings
		wing.player = self.player
		self.wings.add(wing)

		gainLife = GainLife()
		gainLife.rect.x = 1900
		gainLife.rect.y = 170
		screen.blit(treasureChest, (gainLife.rect.x, gainLife.rect.y))
		gainLife.image = treasureChest
		self.gainLives.add(gainLife)
		gainLife.gainLives = self.gainLives
		gainLife.player = self.player

	def draw(self, screen):
		screen.fill(LIGHTBROWN)
		super().draw(screen)

	def update(self):
		super().update()