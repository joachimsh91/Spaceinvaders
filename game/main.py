# Current game version
import time, pygame, random
from setup import *
from objects import Bullet, Ammunation, Player, Enemy, Clock
from func import isCollision
from menus import start_menu, game_over


# Game loop
def main():

    # Random number generator
    rand = random.randint

    # Start time
    start = int(time.time())

    # Creates an player object
    ship = Player(370, 480, True)

    # Creates enemy objects
    en1 = [Enemy(0, 80, True), Enemy(80, 80, True), 
           Enemy(160, 80, True), Enemy(240, 80, True), 
           Enemy(320, 80, True), Enemy(400, 80, True), 
           Enemy(480, 80, True), Enemy(560, 80, True),
           Enemy(640, 80, True)
         ]
        
    # Creates a bullet object
    p1_bullet = Bullet(390, 460, True)

    # Creates a ammunition object
    ammo = Ammunation

    running = True
    while running:
        
        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Ship controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.playerX_change= -3.5
                if event.key == pygame.K_RIGHT:
                    ship.playerX_change = 3.5
                if event.key == pygame.K_SPACE and p1_bullet.ready is True:
                    p1_bullet.shoot(p1_bullet.bulletX, p1_bullet.bulletY)
                    p1_bullet.shots_fired += 1
                    print(p1_bullet.shots_fired)
                    ammo.ammo_left -= 1
                    print("Remaining ammunition: " + str(ammo.ammo_left))
                if ammo.ammo_left == 0:
                    print("Empty magazine! Reloading... ")
                    ammo.ammo_left = 5
                    

            # If key is realesed no movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ship.playerX_change = 0
                p1_bullet.bulletX_change = 0 

        # Bullet call
        if p1_bullet.ready is False:
            p1_bullet.shoot(p1_bullet.bulletX + 20, p1_bullet.bulletY)
            p1_bullet.bulletY -= p1_bullet.bulletY_change
            if p1_bullet.bulletY <= 0:
                p1_bullet.bulletY = 460
                p1_bullet.reload()
        if p1_bullet.ready is True:
            p1_bullet.bulletX = ship.playerX
            p1_bullet.bulletY = ship.playerY - 20

        # Enemy call
        for e in range(len(en1)):
            enemykill = isCollision(en1[e].enemyX, en1[e].enemyY, p1_bullet.bulletX, p1_bullet.bulletY)
            playerkill = isCollision(en1[e].enemyX, en1[e].enemyY, ship.playerX, ship.playerY)

            en1[e].enemy1(en1[e].enemyX, en1[e].enemyY)
            en1[e].enemyX += en1[e].enemyX_change

            if playerkill:
                # TODO Make player sprite flash when hit by enemy
                en1[e].enemyY = -100 
                ship.hits += 1
                ship.playerLife -= 1
                print("You got hit! Remaining lives left: " + str(ship.playerLife))
                
            if enemykill:
                # TODO Find a solution to delete enemy from array without the game crashing
                en1.append(Enemy(rand(0, 400), 80, True))
                ship.enemykilled += 1
                ship.playerScore += 10
                print(ship.enemykilled)
                en1[e].hit()
                # Enemy is hidden behind screen when killed.
                en1[e].enemyY = -100
                p1_bullet.bulletY = 600
                p1_bullet.reload()

            if en1[e].alive and en1[e].enemyX <=0:
                en1[e].enemyX_change = 3.5
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700:
                en1[e].enemyX_change = -3.5
                en1[e].enemyY += en1[e].enemyY_change


                   
        # Setting player movement boundaries
        if ship.playerX <= 0:
            ship.playerX = 0

        elif ship.playerX >= 735:
            ship.playerX= 735

        # Player call
        if ship.alive:
            ship.player1(ship.playerX, ship.playerY)
            ship.playerX += ship.playerX_change

        if not ship.alive:
            running = False
            del ship
        
        
        end = int(time.time())
        total = end - start

        # Live stats
        ship.show_life(10, 10)
        ship.show_score(270, 10)
        ship.show_level(720, 10)
        Clock.show_time(450, 10, end, start)

        if ship.playerLife == 0:
                quit = game_over(ship.enemykilled, ship.playerScore, total, ship.hits, p1_bullet.shots_fired, ship.playerLevel)
                if quit is False:
                    main()
                elif quit is True:
                    start_menu()
                    main()

start_menu()
main()
