import time, math, pygame, random, sys
rand = random.randint

# Player class
class Player:
    playerScore = 0
    playerLife = 5
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

    def hit(self):
        self.alive = False
        game_over()
    
    def showScore(self):
        print("Your current score: " + str(self.playerScore))
    
    def __del__(self):
        print('Gamer over.')

# Enemy class
class Enemy:
    enemyImg1 = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\enemy.png")

    def __init__(self, enemyX, enemyY, alive: bool):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = 3.5
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
    
class Ammunation:
    ammo_left = 5
    magazines_left = 2

class Stats:
    
    def show_score(x, y):
        score = font.render("Score: " + str(ship.playerScore), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def show_life(x, y):
        life = font.render("Lives: " + str(ship.playerLife), True, (255, 255, 255))
        screen.blit(life, (x, y))

    def show_time(x, y):
        time = font.render("Time: " + str(end - start), True, (255, 255, 255))
        screen.blit(time, (x, y))

    def show_enemies_killed(x, y):
        stats = font.render("Enemies killed " + str(ship.enemykilled), True, (255, 255, 255))
        screen.blit(stats, (x, y))


def isCollision(object1X, object1Y, object2X, object2Y):
    distance = math.sqrt((math.pow(object1X-object2X,2)) + (math.pow(object1Y-object2Y,2)))
    if distance < 27:
        return True
    else: 
        return False

def enemySpawn():
    enemies = [Enemy(rand(0, 80), 80, True),   Enemy(rand(100, 180), 80, True), 
               Enemy(rand(200, 280), 80, True), Enemy(rand(300, 380), 80, True), 
               Enemy(rand(400, 480), 80, True), Enemy(rand(500, 580), 80, True), 
              ]
    return enemies

def start_menu():
    welcome_text = big_font_header.render("Space Invaders", True, (255, 255, 255))
    press_play = font_header2.render("Press 'Enter' to Play or 'Esc' to exit", True, (255, 255, 255))
    made_by = font.render("Made by Joachim Smørdal Haug", True, (255, 255, 255))
    global ship
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
                    main()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit
                    sys.exit()


def game_over():
    # Text rendering
    game_over_text = font_header.render("GAME OVER", True, (255, 255, 255))
    results_text = font_header2.render("Results: ", True, (255, 255, 255))
    enemies_killed = font.render("Enemies killed: " + str(ship.enemykilled), True, (255, 255, 255))
    score_text = font.render("Score: " + str(ship.playerScore) + " pts", True, (255, 255, 255))
    time_elapsed = font.render("Time elapsed: " + str(end - start) + " sec", True, (255, 255, 255))
    hits_taken = font.render("Hits taken: " + str(ship.hits) , True, (255, 255, 255))
    shots_fired = font.render("Shots fired: " + str(p1_bullet.shots_fired), True, (255, 255, 255))
    retry_text = font_header2.render("Retry? (y/n) ", True, (255, 255, 255))
    
    game_over = True
    while game_over:

        # Displays text on screen
        screen.blit(game_over_text, (width/2 - (game_over_text.get_width()/2), (height/2 + game_over_text.get_height() * -2.5)))
        screen.blit(results_text, (width/2 - (results_text.get_width()/2), (height/2 + results_text.get_height() * 0)))
        screen.blit(time_elapsed, (width/2 - (time_elapsed.get_width()/2), (height/2 + time_elapsed.get_height() * 2.5)))
        screen.blit(score_text, (width/2 - (score_text.get_width()/2), (height/2 + score_text.get_height() * 3.5)))
        screen.blit(enemies_killed, (width/2 - (enemies_killed.get_width()/2), (height/2 + enemies_killed.get_height() * 4.5)))
        screen.blit(shots_fired, (width/2 - (shots_fired.get_width()/2), (height/2 + shots_fired.get_height() * 5.5)))
        screen.blit(hits_taken, (width/2 - (hits_taken.get_width()/2), (height/2 + hits_taken.get_height() * 6.5)))
        screen.blit(retry_text, (width/2 - (retry_text.get_width()/2), (height/2 + hits_taken.get_height() * 11)))
        
        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_over is False
                    main()
                if event.key == pygame.K_n:
                    start_menu()
                    #pygame.quit
                    #sys.exit()

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
width = screen.get_width()
height = screen.get_height()

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\ufo.png")
pygame.display.set_icon(icon)

# Background image
bg = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\bg.png")

# Creates ammunition
ammo = Ammunation

# Fonts 
font = pygame.font.Font('freesansbold.ttf', 16)
big_font_header = pygame.font.Font('freesansbold.ttf', 48)
font_header = pygame.font.Font('freesansbold.ttf', 32)
font_header2 = pygame.font.Font('freesansbold.ttf', 24)

# Stat tracking
s1 = Stats

# Game loop
def main():

    # Sets start time
    global start
    start = int(time.time())

    # Creates an player object
    global ship 
    ship = Player(370, 480, True)

    # Creates enemy objects
    global en1
    en1 = enemySpawn()

    # Creates a bullet object
    global p1_bullet
    p1_bullet = Bullet(390, 460, True)

    running = True
    while running:
        
        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Ship control
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
            p1_bullet.bulletY = ship.playerY

    # Enemy call
        for e in range(len(en1)):
            enemykill = isCollision(en1[e].enemyX, en1[e].enemyY, p1_bullet.bulletX, p1_bullet.bulletY)
            playerkill = isCollision(en1[e].enemyX, en1[e].enemyY, ship.playerX, ship.playerY)

            en1[e].enemy1(en1[e].enemyX, en1[e].enemyY)
            en1[e].enemyX += en1[e].enemyX_change

            if playerkill:
                en1[e].hit()
                en1[e].enemyY = 700 
                ship.hits += 1
                ship.playerLife -= 1
                ship.playerScore -= 10
                print("You got hit! Remaining lives left: " + str(ship.playerLife))

            if ship.playerLife == 0:
                running = False
                ship.hit()
                
            if enemykill:
                en1.append(Enemy(rand(0,400), 80, True))
                ship.enemykilled += 1
                ship.playerScore += 10
                print(ship.enemykilled)
                en1[e].hit()
                en1[e].enemyY = -100
                p1_bullet.bulletY = 600
                ship.showScore()
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
            ship.showScore()
            running = False
            del ship
        
        global end
        end = int(time.time())

        # Stat displays
        s1.show_life(10, 10)
        s1.show_score(10, 30)
        s1.show_time(10, 50)

start_menu()
main()
