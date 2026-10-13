"""""
import pygame

# Initialize Pygame
pygame.init()

# Game window setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Epic Adventure Game")

# Setup a game clock to control the frame rate (FPS)
clock = pygame.time.Clock()

# PLAYER STUFF
# X and Y represent the top-left corner coordinates of our player square
player_x = 400
player_y = 300
player_size = 40  # The width and height of our square in pixels
player_speed = 5  # How many pixels the player moves per frame

#Obstacle stuff
obstacle_x = 250
obstacle_y = 200
obstacle_width = 150
obstacle_height = 100

# Game loop flag
running = True

# THE CORE GAME LOOP
while running:
    # 1. HANDLE INPUTS (Events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys
    keys = pygame.key.get_pressed()

#Save player's previous position for collision detection
    old_player_x = player_x
    oldplayer_y = player_y

#Movement and boundary checks
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if player_x < 0:
        player_x = 0
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if player_y < 0:
        player_y = 0
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

#Obstacle collision detection
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_size > obstacle_y):
        # Collision detected, revert to previous position
        player_x = old_player_x
        player_y = oldplayer_y

    # 2. DRAW GRAPHICS
    #Screen
    screen.fill((100, 149, 237))  

#Obstacle Box
    pygame.draw.rect(screen, (139, 69, 19), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Draw the player square (Screen, Color (RGB), [X, Y, Width, Height])
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_size, player_size))

    # REFRESH & TICK
    pygame.display.flip()
    clock.tick(60)  # Lock the game to a smooth 60 frames per second


# Clean up and close
pygame.quit()


"""""