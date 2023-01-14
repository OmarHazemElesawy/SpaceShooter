import pygame
import random
import math
from pygame import mixer
# initialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("hiclipart.com.png")

# music
mixer.music.load("background_music.ogg")
mixer.music.play(-1)
# title and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load("spaceship_icon.png")
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load("our_spaceship.png")
# playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480


playerX_change = 0
# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
sum_of_enemies = 5
for i in range ( sum_of_enemies):
    enemyImg.append(pygame.image.load("alien2.png"))
    # playerImg = pygame.image.load("player.png")
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

missileImg = pygame.image.load("missile.png")
# playerImg = pygame.image.load("player.png")
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 5
missile_state = "ready"
# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    over_game = over_font.render("GAME OVER", True, (212, 175, 55))
    screen.blit(over_game, (200, 250))


def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x+16, y+20))


def made_collision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(missileX-enemyX, 2)) + (math.pow(missileY-enemyY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if missile_state =="ready":
                    missile_sound = mixer.Sound("shoot.wav")
                    missile_sound.play()
                    missileX = playerX
                    fire_missile(missileX, missileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(sum_of_enemies):
        if enemyY[i] > 440:
            for j in range(sum_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        collision = made_collision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            hit_sound = mixer.Sound("hit.wav")
            hit_sound.play()
            missileY = 480
            missile_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    # missile
    if missile_state == "fire":
        fire_missile(missileX, missileY)
        missileY -= missileY_change
    if missileY <= 0:
        missileY = 480
        missile_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()


