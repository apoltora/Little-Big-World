#This file is the set up of the final boss stage
import pygame
from Level import *
from WorldObjects import *

screenWidth = 1300
screenHeight = 800
wings = pygame.image.load("wings.png")
bowser = pygame.image.load("bowser.png")

class Level03(Level):

	def __init__(self, player):
		Level.__init__(self, player)

		self.levelWidth = -1500

		flooring = [[1050, screenHeight, -1000, 0], #left wall
		[1300, 50, 0, screenHeight-50], #regular flooring
		[40, 40, 300, screenHeight-170],
		[40, 40, 400, screenHeight-290],
		[40, 40, 520, screenHeight-310],
		[40, 40, 750, screenHeight-310],
		[40, 40, 850, screenHeight-430],
		[50, screenHeight, screenWidth-50, 0]]


		for platform in flooring:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platforms.add(block)

		enemy1 = FinalBoss(150,150)
		enemy1.rect.x = 1080
		enemy1.rect.y = screenHeight - 200
		screen.blit(bowser, (enemy1.rect.x - 100, enemy1.rect.y))
		enemy1.image = bowser
		enemy1.player = self.player
		enemy1.level = self
		enemy1.lavaBreath = self.lavaBreath
		self.enemies.add(enemy1)
		self.boss.add(enemy1)
		enemy1.enemies = self.enemies
		enemy1.platforms = self.platforms
		enemy1.fireballs = self.fireballs
		enemy1.stalkers = self.stalkers

		enemy2 = ShootingEnemy(40, 40, 3, 0)
		enemy2.rect.x = 50
		enemy2.rect.y = 225
		enemy2.player = self.player
		enemy2.level = self
		self.enemies.add(enemy2)
		self.shootingEnemies.add(enemy2)
		enemy2.enemies = self.enemies
		enemy2.pellets = self.pellets
		enemy2.platforms = self.platforms

		enemy3 = ShootingEnemy(40, 40, 2, 0)
		enemy3.rect.x = 50
		enemy3.rect.y = 400
		enemy3.player = self.player
		enemy3.level = self
		self.enemies.add(enemy3)
		self.shootingEnemies.add(enemy2)
		enemy3.enemies = self.enemies
		enemy3.pellets = self.pellets
		enemy3.platforms = self.platforms

		enemy4 = ShootingEnemy(40, 40, 2, 0)
		enemy4.rect.x = 50
		enemy4.rect.y = 575
		enemy4.player = self.player
		enemy4.level = self
		self.enemies.add(enemy4)
		self.shootingEnemies.add(enemy2)
		enemy4.enemies = self.enemies
		enemy4.pellets = self.pellets
		enemy4.platforms = self.platforms

		wing = Wings()
		wing.rect.x = 850
		wing.rect.y = screenHeight - 460
		screen.blit(wings, (wing.rect.x, wing.rect.y))
		wing.image = wings
		wing.player = self.player
		wing.wings = self.wings
		self.wings.add(wing)
	
	def draw(self, screen):
		screen.fill(LIGHTBROWN)
		super().draw(screen)

	def update(self):
		super().update()