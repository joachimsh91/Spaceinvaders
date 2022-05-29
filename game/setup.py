import pygame

# Initialize the game
init = pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Get screen width and height
width = screen.get_width()
height = screen.get_height()

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\ufo.png")
pygame.display.set_icon(icon)

# Background image
bg = pygame.image.load(r"C:\Users\joachh\Documents\spaceinvaders-20220528T210043Z-001\spaceinvaders\sprites\bg.png")

# Fonts 
font = pygame.font.Font('freesansbold.ttf', 16)
big_font_header = pygame.font.Font('freesansbold.ttf', 48)
font_header = pygame.font.Font('freesansbold.ttf', 32)
font_header2 = pygame.font.Font('freesansbold.ttf', 24)

# Text
level1 = big_font_header.render("Level 1", True, (255, 255, 255))
level2 = big_font_header.render("Level 2", True, (255, 255, 255))
level3 = big_font_header.render("Level 3", True, (255, 255, 255))
level4 = big_font_header.render("Level 4", True, (255, 255, 255))
level5 = big_font_header.render("Level 5", True, (255, 255, 255))
