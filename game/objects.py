import pygame, random
from setup import *
rand = random

# Player class
class Player:
    playerScore = 0
    playerLife = 5
    playerLevel = 1
    enemykilled = 0
    hits = 0
    playerImg = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\player.png")

    def __init__(self, playerX, playerY, alive: bool):
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = 0
        self.alive = alive
    
    def player1(self, x, y):
        screen.blit(Player.playerImg, (x, y))
    
    def show_score(self, x, y):
        score = font.render("Score: " + str(self.playerScore), True, (255, 255, 255))
        screen.blit(score, (x,y))

    def show_life(self, x, y):
        life = font.render("Lives: " + str(self.playerLife), True, (255, 255, 255))
        screen.blit(life, (x, y))

    def show_level(self, x, y):
        level = font.render("Level: " + str(self.playerLevel), True, (255, 255, 255))
        screen.blit(level, (x, y))
    
    def __del__(self):
        print('Gamer over.')

# Enemy class
class Enemy:
    enemyImg1 = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\enemy.png")

    def __init__(self, enemyX, enemyY, enemyX_change, alive: bool):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change
        self.enemyY_change = 50
        self.alive = alive

    def enemy1(self, x, y):
        screen.blit(Enemy.enemyImg1, (x, y))
    
    def hit(self):
        self.alive = False
    
    def __del__(self):
        print('Enemy killed.')

# Bullet class
class Bullet:
    bulletImg1 = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\bullet.png")
    bulletstate = "ready"
    shots_fired = 0

    def __init__(self, bulletX, bulletY, ready: bool):
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletX_change = 0
        self.bulletY_change = 5
        self.ready = ready

    def shoot(self, x ,y):
        screen.blit(Bullet.bulletImg1, (x, y))
        self.ready = False

    def reload(self):
        self.ready = True

    def __del__(self):
        ("Enemy hit!")

# Ammunition class
class Ammunation:
    ammo_left = 5
    magazines_left = 2
    
# Game clock
class Clock:
    def show_time(x, y, end, start):
        time = font.render("Time: " + str(end - start), True, (255, 255, 255))
        screen.blit(time, (x, y))

