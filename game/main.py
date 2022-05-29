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
    en1 = [Enemy(rand(0, 80), 80, 1.0, True), Enemy(rand(100, 180), 80, 1.0, True), 
          Enemy(rand(200, 280), 80, 1.0, True), Enemy(rand(300, 380), 80, 1.0, True), 
           Enemy(rand(400, 480), 80, 1.0, True), Enemy(rand(500, 580), 80, 1.0, True)
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
                if event.key == pygame.K_SPACE and p1_bullet.ready is True and ammo.magazines_left > 0:
                    p1_bullet.shoot(p1_bullet.bulletX, p1_bullet.bulletY)
                    p1_bullet.shots_fired += 1
                    print(p1_bullet.shots_fired)
                    ammo.ammo_left -= 1
                    print("Remaining ammunition: " + str(ammo.ammo_left))
                if ammo.ammo_left == 0 and ammo.magazines_left > 0:
                    print("Empty magazine! Reloading... ")
                    ammo.ammo_left = 5
                    ammo.magazines_left -= 1
                    print("Remaining magazines: " + str(ammo.magazines_left))
                if ammo.magazines_left == 0:
                    print("No more ammo!")
                    ammo.magazines_left = 2

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
                en1[e].enemyY = 700 
                ship.hits += 1
                ship.playerLife -= 1
                print("You got hit! Remaining lives left: " + str(ship.playerLife))
                
            if enemykill:
                en1.append(Enemy(rand(0, 400), 80, en1[e].enemyX_change, True))
                ship.enemykilled += 1
                ship.playerScore += 10
                print(ship.enemykilled)
                en1[e].hit()
                en1[e].enemyY = -100
                p1_bullet.bulletY = 600
                p1_bullet.reload()

            # Level 1
            if en1[e].alive and en1[e].enemyX <= 0 and ship.playerScore <= 100:
                en1[e].enemyX_change = 1.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and ship.playerScore <= 100:
                en1[e].enemyX_change = - 1.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 2
            if en1[e].alive and en1[e].enemyX <= 0 and 100 <= ship.playerScore <= 200:
                ship.playerLevel = 2
                en1[e].enemyX_change = 2.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 100 <= ship.playerScore <= 200:
                en1[e].enemyX_change = - 2.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 3
            if en1[e].alive and en1[e].enemyX <= 0 and 200 <= ship.playerScore <= 300:
                ship.playerLevel = 3
                en1[e].enemyX_change = 3.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 200 <= ship.playerScore <= 300:
                ship.playerLevel = 3
                en1[e].enemyX_change = - 3.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 4
            if en1[e].alive and en1[e].enemyX <= 0 and 300 <= ship.playerScore <= 400:
                ship.playerLevel = 4
                en1[e].enemyX_change = 4.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 300 <= ship.playerScore <= 400:
                ship.playerLevel = 4
                en1[e].enemyX_change = - 4.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 5
            if en1[e].alive and en1[e].enemyX <= 0 and 400 <= ship.playerScore <= 500:
                ship.playerLevel = 5
                en1[e].enemyX_change = 5.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 400 <= ship.playerScore <= 500:
                ship.playerLevel = 5
                en1[e].enemyX_change = - 5.0
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

        # Level popup
        if ship.playerLevel == 1:
            if total < 3:
                screen.blit(level1, (width/2 - (level1.get_width()/2), (height/2 + level1.get_height() * 0)))

        if ship.playerScore != 100:
            t1 = int(time.time())

        if ship.playerScore == 100:
            t2 = int(time.time())
            if t2 - t1 < 3:
                screen.blit(level2, (width/2 - (level2.get_width()/2), (height/2 + level2.get_height() * 0)))
        
        if ship.playerScore != 200:
            t1 = int(time.time())
            
        if ship.playerScore == 200:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level3, (width/2 - (level3.get_width()/2), (height/2 + level3.get_height() * 0)))

        if ship.playerScore != 300:
            t1 = int(time.time())
            
        if ship.playerScore == 300:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level4, (width/2 - (level4.get_width()/2), (height/2 + level4.get_height() * 0)))
        
        if ship.playerScore != 400:
            t1 = int(time.time())
            
        if ship.playerScore == 400:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level5, (width/2 - (level5.get_width()/2), (height/2 + level5.get_height() * 0)))
                
              



        if ship.playerLife == 0:
                quit = game_over(ship.enemykilled, ship.playerScore, total, ship.hits, p1_bullet.shots_fired, ship.playerLevel)
                if quit is False:
                    main()
                elif quit is True:
                    start_menu()
                    main()

start_menu()
main()
