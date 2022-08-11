# In this file I store unfinished features in the making

#Feature to make enemies faster by level reached

""" # Level 1
            if en1[e].alive and en1[e].enemyX <= 0 and 10 <= ship.playerScore <= 10:
                ship.playerLevel = 1
                en1[e].enemyX_change = 1.0
                en1[e].enemyY += en1[e].enemyY_change
    
            # Level 2
            if en1[e].alive and en1[e].enemyX <= 0 and 10 <= ship.playerScore <= 20:
                ship.playerLevel = 2
                en1[e].enemyX_change = 2.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 10 <= ship.playerScore <= 20:
                en1[e].enemyX_change = - 2.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 3
            if en1[e].alive and en1[e].enemyX <= 0 and 20 <= ship.playerScore <= 30:
                ship.playerLevel = 3
                en1[e].enemyX_change = 3.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 20 <= ship.playerScore <= 30:
                ship.playerLevel = 3
                en1[e].enemyX_change = - 3.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 4
            if en1[e].alive and en1[e].enemyX <= 0 and 30 <= ship.playerScore <= 40:
                ship.playerLevel = 4
                en1[e].enemyX_change = 4.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 30 <= ship.playerScore <= 40:
                ship.playerLevel = 4
                en1[e].enemyX_change = - 4.0
                en1[e].enemyY += en1[e].enemyY_change

            # Level 5
            if en1[e].alive and en1[e].enemyX <= 0 and 40 <= ship.playerScore <= 50:
                ship.playerLevel = 5
                en1[e].enemyX_change = 5.0
                en1[e].enemyY += en1[e].enemyY_change

            if en1[e].alive and en1[e].enemyX >= 700 and 40 <= ship.playerScore <= 50:
                ship.playerLevel = 5
                en1[e].enemyX_change = - 5.0
                en1[e].enemyY += en1[e].enemyY_change"""

 # Feature to make text popup on screen when new level is reached
 # TODO Find a way to make the popup message dissappear after x amount of time               

""" # Level popup
        if ship.playerLevel == 1:
            if total < 3:
                screen.blit(level1, (width/2 - (level1.get_width()/2), (height/2 + level1.get_height() * 0)))

        if ship.playerScore != 10:
            t1 = int(time.time())

        if ship.playerScore == 10:
            t2 = int(time.time())
            print(t2-t1)
            if t2 - t1 < 3:
                screen.blit(level2, (width/2 - (level2.get_width()/2), (height/2 + level2.get_height() * 0)))
        
        if ship.playerScore != 20:
            t1 = int(time.time())
            
        if ship.playerScore == 20:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level3, (width/2 - (level3.get_width()/2), (height/2 + level3.get_height() * 0)))

        if ship.playerScore != 30:
            t1 = int(time.time())
            
        if ship.playerScore == 30:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level4, (width/2 - (level4.get_width()/2), (height/2 + level4.get_height() * 0)))
        
        if ship.playerScore != 40:
            t1 = int(time.time())
            
        if ship.playerScore == 40:
            t2 = int(time.time())
            if t2 - t1 < 4:
                screen.blit(level5, (width/2 - (level5.get_width()/2), (height/2 + level5.get_height() * 0)))
                
        """