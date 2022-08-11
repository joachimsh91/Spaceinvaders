import pygame, sys
from setup import *
from objects import Player

def start_menu():
    welcome_text = big_font_header.render("Space Invaders", True, (255, 255, 255))
    press_play = font_header2.render("Press 'Enter' to Play or 'Esc' to exit", True, (255, 255, 255))
    made_by = font.render("Made by Joachim Smørdal Haug", True, (255, 255, 255))
    ship = Player(370, 300, True)
    menu = True
    while menu:
        screen.blit(welcome_text, (width/2 - (welcome_text.get_width()/2), (height/2 + welcome_text.get_height() * -2.5)))
        screen.blit(press_play, (width/2 - (press_play.get_width()/2), (height/2 + press_play.get_height() * 5.5)))
        screen.blit(made_by, (width/2 - (made_by.get_width()/2), (height/2 + made_by.get_height() * 12)))
        ship.player1(ship.playerX, ship.playerY)

        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit
                    sys.exit()

def game_over(kills, pts, t, hits, shots, lev):
    # Text rendering for game over menu
    game_over_text = font_header.render("GAME OVER", True, (255, 255, 255))
    results_text = font_header2.render("Results: ", True, (255, 255, 255))
    retry_text = font_header2.render("Retry? (y/n) ", True, (255, 255, 255))
    enemies_killed = font.render("Enemies killed: " + str(kills), True, (255, 255, 255))
    score_text = font.render("Score: " + str(pts) + " pts", True, (255, 255, 255))
    time_elapsed = font.render("Time elapsed: " + str(t) + " sec", True, (255, 255, 255))
    hits_taken = font.render("Hits taken: " + str(hits) , True, (255, 255, 255))
    shots_fired = font.render("Shots fired: " + str(shots), True, (255, 255, 255))
    #level_reached = font.render("Level reached: " + str(lev), True, (255, 255, 255))
    game_over = True
    quit = True
    while game_over:
        

        # Displays text on screen
        screen.blit(game_over_text, (width/2 - (game_over_text.get_width()/2), (height/2 + game_over_text.get_height() * -2.5)))
        screen.blit(results_text, (width/2 - (results_text.get_width()/2), (height/2 + results_text.get_height() * 0)))
        screen.blit(time_elapsed, (width/2 - (time_elapsed.get_width()/2), (height/2 + time_elapsed.get_height() * 2.5)))
        #screen.blit(level_reached, (width/2 - (level_reached.get_width()/2), (height/2 + level_reached.get_height() * 3.5)))
        screen.blit(score_text, (width/2 - (score_text.get_width()/2), (height/2 + score_text.get_height() * 3.5)))
        screen.blit(enemies_killed, (width/2 - (enemies_killed.get_width()/2), (height/2 + enemies_killed.get_height() * 4.5)))
        screen.blit(shots_fired, (width/2 - (shots_fired.get_width()/2), (height/2 + shots_fired.get_height() * 5.5)))
        screen.blit(hits_taken, (width/2 - (hits_taken.get_width()/2), (height/2 + hits_taken.get_height() * 6.5)))

        screen.blit(retry_text, (width/2 - (retry_text.get_width()/2), (height/2 + retry_text.get_height() * 7)))
        
        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    quit = False
                    return quit
                    
                if event.key == pygame.K_n:
                    #start_menu()
                    return quit
                    