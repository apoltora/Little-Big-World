##### Credits #####
""" 
##### Coding Skills #####
This helped me with gravity/jumping and bouyancy/swimming
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py

This helped me with screen scrolling
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py

This helped me with moving platforms
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py

Helped me with start screen and button clicks
https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection

##### Songs #####

Where I got the game song from (Mario)
https://www.freegalmusic.com/search-page/video%2520game/artists/VGhlIFZpZGVvIEdhbWUgTXVzaWMgT3JjaGVzdHJhfEFyY2FkaWE

Where I got the start and end song from (Tetris)
https://montgomerycountymd.freegalmusic.com/search-page/video%252520game/artists/VGhlIFZpZGVvIEdhbWUgTXVzaWMgT3JjaGVzdHJhfEFyY2FkaWE/songs

Credits to final boss stage song goes to Seth Everman
https://www.youtube.com/watch?v=6dEjh1BhTsM

##### Pictures #####

Got the picture of mario from...
http://pixelartmaker.com/art/7b807432010bfc3.png

Got the picture of the cloud from...
https://www.pond5.com/stock-video-footage/1/cloud-animation.html

Got the picture of bowser from...
https://www.tynker.com/community/projects/play/bowser-battle/5983eb915ae02923498b456f

Got the picture of ghost from...
https://www.youtube.com/watch?v=cnhY4rDRRp4

Got the picture of the goomba/mushroom from...
http://www.how-to-draw-cartoons-online.com/goomba.html

Got the picture of the sea Urchins from...
https://depositphotos.com/16295861/stock-illustration-sea-urchin-cartoon.html

Got the picture of the squid from...
https://www.ebay.com/itm/Cartoon-Splatoon-Multi-Color-Squid-Vinyl-Sticker-bumper-phone-window-console-/322835812984

Got picture of cacti from...
https://www.amazon.com/Simple-Prickly-Cactus-Cartoon-Sticker/dp/B073WPPW6F

Got picture of shark from...
https://www.how-to-draw-funny-cartoons.com/shark-picture.html

Got picture of fireball from...
https://www.shutterstock.com/image-vector/cartoon-flame-fire-animated-blazing-flames-645627124

Got the picture of coin from...
https://www.vectorstock.com/royalty-free-vector/gold-dollar-coin-cartoon-style-isolated-vector-16630715

Got the picture of wings from...
https://www.pinterest.com/pin/434315957788963966/?lp=true

Got the picture of treasure chest from...
https://pngtree.com/freepng/front-view-golden-treasure-chest-cool-treasure-chest-gold-coin-chest_3820953.html

Picture of startScreen
https://www.pinterest.com/pin/293296994457308303/?lp=true

##### Pictures for Video #####

Mario & Peach pictures
https://i.telegraph.co.uk/gaming/what-to-play/gamings-greatest-love-stories/mario-and-peach-super-mario-bros/
https://www.svg.com/124986/strange-things-about-mario-and-peachs-relationship/

Mario characters
https://en.wikipedia.org/wiki/List_of_Mario_franchise_characters

Bowser attack character
https://characterprofile.fandom.com/wiki/Bowser

Mario front
https://www.giantbomb.com/mario/3005-177/images/

"""
##### End of Credits #####

#Link to video: https://youtu.be/u4Z5R4HOb5g

import pygame
from Level01 import *
from Level02 import *
from Level03 import *
from Level import *
from Player import *
from WorldObjects import *

#Note:
#controls movements through changing rect attributes
#uses change of x and y to do so

# Global constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 204, 255)
BROWN = (128, 64, 0)
LIGHTBLUE = (204, 238, 255)
YELLOW = (255, 255, 0)
LAVARED = (153, 51, 0)

screenWidth = 1300
screenHeight = 800

#Enemies
goomba = pygame.image.load("goomba.gif")
ghost = pygame.image.load("ghost.png")
sharkLeft = pygame.image.load("sharkLeft.png")
bowser = pygame.image.load("bowser.png")
seaUrchin = pygame.image.load("seaUrchin.png")
squid = pygame.image.load("squid.png")
cactusUpright = pygame.image.load("cactus.png")
cloud = pygame.image.load("cloud.png")

#Special features
coinPic = pygame.image.load("coin.png")
wings = pygame.image.load("wings.png")
treasureChest = pygame.image.load("treasureChest.png")
fireballRight = pygame.image.load("fireballRight.png")

player = Player()

#Where you can skip levels by commenting out appends
levels = []
levels.append(Level01(player))
levels.append(Level02(player))
levels.append(Level03(player))

pygame.init()
size = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)


startScreen = pygame.image.load("startScreen.jpg")

def start():
    #set up screen
    pygame.init()

    size = [screenWidth, screenHeight]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Begin Play!")
    screen.blit(startScreen, (0,0))

    title = pygame.font.SysFont("Times New Roman", 120)
    title = title.render("Little Big World", True, (0,0,0))
    screen.blit(title, (screenWidth//4, 100))

    #set up buttons
    startGameButton = [screenWidth//7,screenHeight//2+20,400,200]
    instructionButton = [screenWidth//7+500,screenHeight//2+20,400,200]
    pygame.draw.rect(screen, (255,255,255), startGameButton)
    pygame.draw.rect(screen, (255,255,255), instructionButton)
    play = pygame.font.SysFont("Times New Roman", 80)
    startGame = play.render("Play", True, (0,0,0))
    screen.blit(startGame, (330,500))
    instructions = pygame.font.SysFont("Times New Roman", 80)
    instruct = play.render("Instructions", True, (0,0,0))
    screen.blit(instruct, (730,500))

    #check if button was clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #play button
            if (startGameButton[0]<=pos[0]<=startGameButton[0]+startGameButton[2])\
             and (startGameButton[1]<=pos[1]<=startGameButton[1]+startGameButton[3]):
                run()
                return True
            #instructions button
            if (instructionButton[0]<=pos[0]<=instructionButton[0]+instructionButton[2])\
             and (instructionButton[1]<=pos[1]<=instructionButton[1]+instructionButton[3]):
                instruction()
                return True


def instruction():
    pygame.init()
    gameFinished = False
    size = [screenWidth, screenHeight]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Instructions")
    screen.fill((255,153,51))
    while not gameFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFinished = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (startGameButton[0]<=pos[0]<=startGameButton[0]+startGameButton[2])\
                and (startGameButton[1]<=pos[1]<=startGameButton[1]+startGameButton[3]):
                    run()
                    return True
        startGameButton = [screenWidth//3,screenHeight//2+20,400,200]
        pygame.draw.rect(screen, (255,255,255), startGameButton)
        play = pygame.font.SysFont("Times New Roman", 80)
        startGame = play.render("Play", True, (0,0,0))
        screen.blit(startGame, (575,500))

        title = pygame.font.SysFont("Times New Roman", 120)
        title = title.render("Instructions", True, (0,0,0))
        screen.blit(title, (450, 50))

        instruct = pygame.font.SysFont("Times New Roman", 30)
        instruct = instruct.render("Goal: Get highest score as possible and kill final boss at end. Keystrokes: To move player, use left, up, and right arrow keys.", True, (0,0,0))
        screen.blit(instruct, (25, 25))

        enemiesTitle = pygame.font.SysFont("Times New Roman", 80)
        enemiesTitle = enemiesTitle.render("Enemies", True, (0,0,0))
        screen.blit(enemiesTitle, (100, 100))

        enemy1 = TopKillEnemy(40,50)
        enemy1.rect.x = 50
        enemy1.rect.y = 200
        screen.blit(goomba,(enemy1.rect.x,enemy1.rect.y))
        enemy1.image = goomba

        goombaRules = pygame.font.SysFont("Times New Roman", 18)
        goombaRules = goombaRules.render("Can only be killed by jumping on top of.", True, (0,0,0))
        screen.blit(goombaRules,(100,200))

        enemy2 = Enemy(70,60)
        enemy2.rect.x = 50
        enemy2.rect.y = 300
        screen.blit(cloud,(enemy2.rect.x, enemy2.rect.y))
        enemy2.image = cloud

        cloudRules = pygame.font.SysFont("Times New Roman", 18)
        cloudRules = cloudRules.render("Cannot be killed. Do not touch.", True, (0,0,0))
        screen.blit(cloudRules,(150,320))

        enemy3 = Enemy(40,80)
        enemy3.rect.x = 50
        enemy3.rect.y = 400
        screen.blit(cactusUpright,(enemy3.rect.x,enemy3.rect.y))
        enemy3.image = cactusUpright

        cactusRules = pygame.font.SysFont("Times New Roman", 18)
        cactusRules = cactusRules.render("Cannot be killed. Do not touch.", True, (0,0,0))
        screen.blit(cactusRules,(130,450))

        enemy4 = SeaUrchin(10,10)
        enemy4.rect.x = 50
        enemy4.rect.y = 550
        screen.blit(seaUrchin,(enemy4.rect.x,enemy4.rect.y))
        enemy4.image = seaUrchin

        urchinRules = pygame.font.SysFont("Times New Roman", 18)
        urchinRules = urchinRules.render("Cannot be killed. Do not touch. Will deduct a life, but not kill you.", True, (0,0,0))
        screen.blit(urchinRules,(75,550))

        enemy5 = Enemy(30,30)
        enemy5.rect.x = 50
        enemy5.rect.y = 600
        screen.blit(squid,(enemy5.rect.x,enemy5.rect.y))
        enemy5.image = squid

        squidRules = pygame.font.SysFont("Times New Roman", 18)
        squidRules = squidRules.render("Cannot be killed. Do not touch.", True, (0,0,0))
        screen.blit(squidRules,(100,600))


        enemy6 = StalkerShark(70,35, screenHeight*4//5-300, screenHeight)
        enemy6.rect.x = 50
        enemy6.rect.y = 700
        screen.blit(sharkLeft,(enemy6.rect.x,enemy6.rect.y))
        enemy6.image = sharkLeft

        sharkRules = pygame.font.SysFont("Times New Roman", 18)
        sharkRules = sharkRules.render("Cannot be killed. Do not touch. Will follow you.", True, (0,0,0))
        screen.blit(sharkRules,(100,700))

        pygame.draw.rect(screen, (255,0,0), (400,175,40,40))

        shooterRules = pygame.font.SysFont("Times New Roman", 18)
        shooterRules = shooterRules.render("Cannot be killed. Do not touch. Shoots pellets- avoid pellets.", True, (0,0,0))
        screen.blit(shooterRules,(450,200))

        enemy8 = FinalBoss(150,150)
        enemy8.rect.x = 350
        enemy8.rect.y = 630
        screen.blit(bowser, (enemy8.rect.x, enemy8.rect.y))
        enemy8.image = bowser

        bossRules = pygame.font.SysFont("Times New Roman", 18)
        bossRules = bossRules.render("Has 20 lives. Shoot with 20 fireballs to kill. Death worth 200 points. Do not touch.", True, (0,0,0))
        screen.blit(bossRules,(450,630))

        foe = ChaserGhost(50,50,50,screenHeight-50)
        foe.rect.x = 400
        foe.rect.y = 100
        screen.blit(ghost, (foe.rect.x, foe.rect.y))
        foe.image = ghost

        ghostRules = pygame.font.SysFont("Times New Roman", 18)
        ghostRules = ghostRules.render("Follows you. Do not touch. Can only kill with a fireball.", True, (0,0,0))
        screen.blit(ghostRules,(450,125))


        pygame.draw.rect(screen, (LAVARED), (400,250,300,150))

        lavaRules = pygame.font.SysFont("Times New Roman", 18)
        lavaRules = lavaRules.render("Do not touch. Bowser breaths it out.", True, (0,0,0))
        screen.blit(lavaRules,(450,350))

        featuresTitle = pygame.font.SysFont("Times New Roman", 18)
        featuresTitle = play.render("Features", True, (0,0,0))
        screen.blit(featuresTitle, (screenWidth-300, 100))

        wing = Wings()
        wing.rect.x = screenWidth - 400
        wing.rect.y = 200
        screen.blit(wings, (wing.rect.x, wing.rect.y))
        wing.image = wings

        Wing = pygame.font.SysFont("Times New Roman", 18)
        Wing = Wing.render("Wings. Will allow player to double jump/fly.", True, (0,0,0))
        screen.blit(Wing, (screenWidth-300, 200))

        gainLife = GainLife()
        gainLife.rect.x = screenWidth - 400
        gainLife.rect.y = 300
        screen.blit(treasureChest, (gainLife.rect.x, gainLife.rect.y))
        gainLife.image = treasureChest

        treasure = pygame.font.SysFont("Times New Roman", 18)
        treasure = treasure.render("Gives player another life.", True, (0,0,0))
        screen.blit(treasure, (screenWidth-300, 300))

        coin = Coin(50,50)
        coin.rect.x = screenWidth-400
        coin.rect.y = 400
        screen.blit(coinPic, (coin.rect.x, coin.rect.y))
        coin.image = coinPic

        c = pygame.font.SysFont("Times New Roman", 18)
        c = c.render("Gives player a point.", True, (0,0,0))
        screen.blit(c, (screenWidth-300, 400))

        fireball = Fireball()
        fireball.rect.x = screenWidth-400
        fireball.rect.y = 500
        screen.blit(fireballRight, (fireball.rect.x, fireball.rect.y))
        fireball.image = fireballRight

        fire = pygame.font.SysFont("Times New Roman", 18)
        fire = fire.render("Player shoots it out with 'a' and 'd' keys.", True, (0,0,0))
        screen.blit(fire, (screenWidth-300, 500))

        pygame.display.flip()
    return True


def run():
    pygame.init()
    #keeps main run function running
    if __name__ == "__main__":
        #keeps going until no more lives left
        while player.lives > 0:
            #calls init to restart player's position
            player.__init__()
            #restarts level on
            for level in levels:
                level.__init__(player)
            if main(player, levels) == True:
                break
        pygame.mixer.music.load('Tetris.mp3')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        end(player)
        pygame.quit()

def end(player):
    pygame.init()
    gameFinished = False
    size = [screenWidth, screenHeight]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Instructions")
    screen.fill((255,0,0))
    startScreenButton = [screenWidth//7,screenHeight//2+20,400,200]
    endGameButton = [screenWidth//7+500,screenHeight//2+20,400,200]
    pygame.draw.rect(screen, (255,255,255), endGameButton)
    pygame.draw.rect(screen, (255,255,255), startScreenButton)

    mainMenu = pygame.font.SysFont("Times New Roman", 80)
    mainMenu = mainMenu.render("Main Menu", True, (0,0,0))
    screen.blit(mainMenu, (250,500))

    endGame = pygame.font.SysFont("Times New Roman", 80)
    endGame = endGame.render("Quit", True, (0,0,0))
    screen.blit(endGame, (800,500))

    #check if button was clicked

    while not gameFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFinished = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (endGameButton[0]<=pos[0]<=endGameButton[0]+endGameButton[2])\
                and (endGameButton[1]<=pos[1]<=endGameButton[1]+endGameButton[3]):
                    return True
                if (startScreenButton[0]<=pos[0]<=startScreenButton[0]+startScreenButton[2])\
                and (startScreenButton[1]<=pos[1]<=startScreenButton[1]+startScreenButton[3]):
                    #restarts player
                    player.lives = 3
                    player.score = 0
                    game()
                    return True

        score = pygame.font.SysFont("Times New Roman", 80)
        score = score.render("Score: " + str(player.score), True, (0,0,0))
        screen.blit(score, (500,250))

        gameOver = pygame.font.SysFont("Times New Roman", 120)
        gameOver = gameOver.render("Game Over!", True, (0,0,0))
        screen.blit(gameOver, (375, 50))

        pygame.display.flip()
    return True

#main run function

def main(character,levels):
    """ Main Program """
    pygame.init()
    size = [screenWidth, screenHeight]
    screen = pygame.display.set_mode(size)

    mario = pygame.image.load("marioFaceRight.png")
    mario = pygame.transform.scale(mario, (50,50))
    #music set-up
    if len(levels) > 1:
        pygame.mixer.music.load('SuperMarioBros.mp3')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
    if len(levels) == 1:
        pygame.mixer.music.load('FinalBoss.mid')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    # Set the height and width of the screen
 
    pygame.display.set_caption("Little Big World")
 
    # Set the current level
    currentLevelNum = 0
    currentLevel = levels[currentLevelNum]
 
    players = pygame.sprite.Group()
    player.level = currentLevel
 
    player.rect.x = 340
    player.rect.y = screenHeight - 75
    players.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        if player.alive == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    closed = True
                    return closed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                        mario = pygame.image.load("marioFaceLeft.png")
                        mario = pygame.transform.scale(mario, (50,50))
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                        mario = pygame.image.load("marioFaceRight.png")
                        mario = pygame.transform.scale(mario, (50,50))
                    if event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_d:
                        player.shoot(10,0)
                    if event.key == pygame.K_a:
                        player.shoot(-10,0)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.xVector < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.xVector > 0:
                        player.stop()

                if event.type == pygame.constants.USEREVENT:
                    if len(levels) > 1:
                        pygame.mixer.music.load('SuperMarioBros.mp3')
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.load('FinalBoss.mid')
                        pygame.mixer.music.play()
     
            # Update the player.
            players.update()
     
            # Update items in the level
            currentLevel.update()
            if len(levels) > 1:
                # If the player gets near the right side, shift the world left (-x)
                if player.rect.right >= 500:
                    diff = player.rect.right - 500
                    player.rect.right = 500
                    currentLevel.shiftWorld(-diff)
         
                # If the player gets near the left side, shift the world right (+x)
                if player.rect.left <= 250:
                    diff = 250 - player.rect.left
                    player.rect.left = 250
                    currentLevel.shiftWorld(diff)
     
            # If the player gets to the end of the level, go to the next level
            currentPosition = player.rect.x + currentLevel.worldShiftX
            if currentPosition <= currentLevel.levelWidth:
                if currentLevelNum <= len(levels)-1:
                    player.rect.x = 120
                    player.rect.y = screenHeight-100
                    currentLevelNum = 0
                    currentLevel = levels[currentLevelNum]
                    player.level = currentLevel
                    #checkpoint makes sure returns to most recent checkpoint
                    levels.pop(0)
                    return
                else:
                    # Out of levels. This just exits the program.
                    # You'll want to do something better.
                    done = True
                    player.lives = 0
     
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            currentLevel.draw(screen)

            score = pygame.font.SysFont("Times New Roman", 30)
            scoreText = score.render("Score: " + str(player.score), True, (0,0,0))
            screen.blit(scoreText, (50,50))

            lives = pygame.font.SysFont("Times New Roman", 30)
            livesText = lives.render("Lives: " + str(player.lives), True, (0,0,0))
            screen.blit(livesText, (screenWidth-150,50))
            if player.wings == True:
                screen.blit(wings, (player.rect.x-5,player.rect.y-5))
            screen.blit(mario, (player.rect.x-5,player.rect.y-5))
            player.image = mario

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
            # Limit to 120 frames per second
            clock.tick(120)
            pygame.display.flip()

        #restarts game if player dies
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #trust me you need this "return None"
            return None

def game():
    pygame.init()
    pygame.mixer.music.load('Tetris.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    gameFinished = False
    # -------- Main Program Loop -----------
    while not gameFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFinished = True
        clock.tick(120)
        if start() == True:
            break
        pygame.display.flip()
    pygame.quit()

game()