#This file is the parent class of all levels
#It updates the screen continuously
import pygame
from Player import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 204, 255)
BROWN = (128, 64, 0)
LIGHTBLUE = (204, 238, 255)
YELLOW = (255, 255, 0)
LIGHTBROWN = (204, 153, 0)
screenWidth = 1300
screenHeight = 800
class Level(object):
    def __init__(self, player):
        self.platforms = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.tubes = pygame.sprite.Group()
        self.player = player
        self.pellets = pygame.sprite.Group()
        self.fireballs = pygame.sprite.Group()
        self.wings = pygame.sprite.Group()
        self.gainLives = pygame.sprite.Group()
        self.lavaBreath = pygame.sprite.Group()
        self.shootingEnemies = pygame.sprite.Group()
        self.stalkers = pygame.sprite.Group()
        self.boss = pygame.sprite.Group()
        self.endGame = False
         
        # Background image
        self.background = None
     
        # How far this world has been scrolled left/right
        self.worldShiftX = 0
        self.levelWidth = -1000
 
    # Update everythign on this level
    def update(self):
        self.platforms.update()
        self.water.update()
        self.enemies.update()
        self.coins.update()
        self.tubes.update()
        self.pellets.update()
        self.fireballs.update()
        self.wings.update()
        self.gainLives.update()
        self.lavaBreath.update()
        self.shootingEnemies.update()
        for breath in self.lavaBreath:
            if pygame.sprite.collide_rect(breath, self.player):
                self.player.lives -= 1
                self.player.alive = False
                return
        for stalker in self.stalkers:
            for fireball in self.fireballs:
                if pygame.sprite.collide_rect(stalker, fireball):
                    self.enemies.remove(stalker)
                    self.stalkers.remove(stalker)
                    self.fireballs.remove(fireball)   
        for pellet in self.pellets:
            if pygame.sprite.spritecollideany(pellet, self.fireballs) != None:
                self.pellets.remove(pellet)
                for fireball in self.fireballs:
                    if pygame.sprite.collide_rect(pellet, fireball):
                        self.fireballs.remove(fireball)
            if pygame.sprite.collide_rect(pellet, self.player):
                self.pellets.remove(pellet)
                self.player.lives -= 1
                self.player.alive = False
                return
        for fireball in self.fireballs:
            if fireball.rect.x < 0 or fireball.rect.x > screenWidth:
                self.fireballs.remove(fireball)
            if pygame.sprite.spritecollideany(fireball, self.platforms) != None:
                self.fireballs.remove(fireball)
            for boss in self.boss:
                if pygame.sprite.collide_rect(fireball, boss):
                    boss.lives -= 1
                    self.player.score += 1
                    self.fireballs.remove(fireball)
                    if boss.lives == 0:
                        self.player.score += 200
                        self.boss.remove(boss)
                        self.enemies.remove(boss)
                        #ends game - have a different finish than just closing though
                        self.player.lives = 0
                        self.player.alive = False
                        return
            if pygame.sprite.spritecollideany(fireball, self.enemies) != None:
                self.fireballs.remove(fireball)
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
 
        # Draw all the sprite lists that we have
        self.water.draw(screen)
        self.platforms.draw(screen)
        self.lavaBreath.draw(screen)
        self.enemies.draw(screen)
        self.coins.draw(screen)
        self.tubes.draw(screen)
        self.pellets.draw(screen)
        self.fireballs.draw(screen)
        self.wings.draw(screen)
        self.gainLives.draw(screen)
 
    def shiftWorld(self, shift_x):
        self.worldShiftX += shift_x

        for wave in self.water:
    	    wave.rect.x += shift_x

        for platform in self.platforms:
            platform.rect.x += shift_x

        for enemy in self.enemies:
            enemy.rect.x += shift_x

        for coin in self.coins:
            coin.rect.x += shift_x

        for tube in self.tubes:
        	tube.rect.x += shift_x

        for pellet in self.pellets:
            pellet.rect.x += shift_x

        for fireball in self.fireballs:
            fireball.rect.x += shift_x

        for wing in self.wings:
            wing.rect.x += shift_x

        for life in self.gainLives:
            life.rect.x += shift_x