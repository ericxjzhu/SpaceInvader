from math import sqrt
from random import randint
import pygame

# Initialise the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/background.png")

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load("images/enemy.png")
enemyX = randint(0, 800)
enemyY = randint(50, 150)
enemyX_change = 2
enemyY_change = 30

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Bullet
# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
bullet_img = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 3
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))   # x + 16 to make it appear in the centre of spaceship, y + 10 to make it appear in front of spaceship

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # RGB - Red Green Blue
    # Player is ontop of screen
    screen.fill((0, 0, 204))
    # Background Image
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x-coordinate of the spaceship.
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Checking for boundaries of spaceship so it doesn't go out of bounds.
    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX > 736: # 800 - 64
        playerX = 736

    # Enemy movement.
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # Bullet movement.
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
