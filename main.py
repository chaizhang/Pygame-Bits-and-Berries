import pygame
import random


class Player:
    def __init__(self, x, y, width, height, velocity):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = velocity


# Bits & Berries TO-DO:
# 1) Wall generation issues
# 2) Wall and border collision
# 3) Randomize berry movement
# 4) Coin and berry counter
# 5) Health bar
# 6) Refactor code
# 7) Make berry generation more rare? (eat 3 coins for 1 berry)
# 8) Starting screen
# 9) Start over screen

pygame.init()

SCREEN_WIDTH = 595  # pixels
SCREEN_HEIGHT = 700

# GAME WINDOW
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bits and Berries")

# GAME DESIGN / LOADING GRAPHICS
bg = pygame.image.load("Blue_Background.png")
border = pygame.image.load("Blue_Border.png")
top_bar = pygame.image.load("Blue_Top_Bar.png")
berries = pygame.image.load("Red_Berries.png")
small_berries = pygame.image.load("Small_Red_Berries.png")
brick_wall = pygame.image.load("Red_Brick_Wall.png")
# =====
coin1 = pygame.image.load("Coin_Frame1.png")
coin2 = pygame.image.load("Coin_Frame2.png")
coin3 = pygame.image.load("Coin_Frame3.png")
coin4 = pygame.image.load("Coin_Frame4.png")
coin5 = pygame.image.load("Coin_Frame5.png")
coin6 = pygame.image.load("Coin_Frame6.png")
coin7 = pygame.image.load("Coin_Frame7.png")
coin8 = pygame.image.load("Coin_Frame8.png")
coin9 = pygame.image.load("Coin_Frame9.png")
coin10 = pygame.image.load("Coin_Frame10.png")
coin11 = pygame.image.load("Coin_Frame11.png")
coin12 = pygame.image.load("Coin_Frame12.png")
coin13 = pygame.image.load("Coin_Frame13.png")
coin14 = pygame.image.load("Coin_Frame14.png")
coin15 = pygame.image.load("Coin_Frame15.png")
coin16 = pygame.image.load("Coin_Frame16.png")
# =====
player_r1 = pygame.transform.scale(pygame.image.load('Player_R1.png'), (35, 35))
player_r2 = pygame.transform.scale(pygame.image.load('Player_R2.png'), (35, 35))
player_l1 = pygame.transform.scale(pygame.image.load('Player_L1.png'), (35, 35))
player_l2 = pygame.transform.scale(pygame.image.load('Player_L2.png'), (35, 35))
player_u1 = pygame.transform.scale(pygame.image.load('Player_U1.png'), (35, 35))
player_u2 = pygame.transform.scale(pygame.image.load('Player_U2.png'), (35, 35))
player_d1 = pygame.transform.scale(pygame.image.load('Player_D1.png'), (35, 35))
player_d2 = pygame.transform.scale(pygame.image.load('Player_D2.png'), (35, 35))

# PLAYER INITIALIZATION
player = Player(280, 385, 35, 35, 35)

# PLAYER IMAGES FOR ANIMATION
player_images = {
    'right': [player_r1, player_r2],
    'left': [player_l1, player_l2],
    'up': [player_u1, player_u2],
    'down': [player_d1, player_d2]
}
direction = 'right'  # set initial direction and image index
image_index = 0
image_counter = 0  # keeps track of how many times an image has been displayed

# WALL
wallX = (random.randint(1, 15)) * 35  # range 35-560
wallY = (random.randint(4, 18)) * 35  # range 140-665
wall = pygame.Rect((wallX, wallY, 35, 35))
walls = []

# BERRY IMAGES FOR ANIMATION
berryX = (random.randint(1, 15)) * 35  # range 35-560
berryY = (random.randint(4, 18)) * 35  # range 140-665
berries_images = [berries, small_berries]
berries_image_index = 0
berry = pygame.Rect((berryX, berryY, 35, 35))

# COIN IMAGES FOR ANIMATION
coinX = (random.randint(1, 15)) * 35  # range 35-560
coinY = (random.randint(4, 18)) * 35  # range 140-665
coin_images = [
    coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8,
    coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16
]
coin_images_index = 0
coin = pygame.Rect((coinX, coinY, 35, 35))

pygame.key.set_repeat(1, 1)

# HOUSE KEEPING
berry_counter = 0
coin_counter = 0
wall_counter = 0
heart_counter = 3

# GAME INTRO SCREEN
intro_font = pygame.font.Font(None, 36)
intro_text = intro_font.render("Press SPACE to begin", True, (255, 255, 255))

intro_screen = True
while intro_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            intro_screen = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            intro_screen = False
    screen.fill((0, 0, 0))
    screen.blit(intro_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    pygame.display.update()

initial_keypress = False
player.rect.x = 280
player.rect.y = 385

# GAME LOOP
run = True
clock = pygame.time.Clock()

while run:

    pygame.event.pump()
    key = pygame.key.get_pressed()

    # EVENT HANDLER
    for event in pygame.event.get():  # iterates through all events that pygame picks up
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==
                                               pygame.K_DOWN or event.key == pygame.K_UP):
            initial_keypress = True
            if event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'

    if initial_keypress:
        if direction == 'left' and player.rect.left > 35:
            player.rect.x -= player.velocity
        elif direction == 'right' and player.rect.right < (SCREEN_WIDTH - 35):
            player.rect.x += player.velocity
        elif direction == 'up' and player.rect.top > 140:
            player.rect.y -= player.velocity
        elif direction == 'down' and player.rect.bottom < (SCREEN_HEIGHT - 35):
            player.rect.y += player.velocity

    screen.fill((0, 0, 0))  # fill screen before drawing player

    # DRAWING
    screen.blit(bg, (35, 140))
    screen.blit(border, (0, 105))
    screen.blit(top_bar, (0, 0))
    screen.blit(berries_images[berries_image_index], berry)
    screen.blit(coin_images[coin_images_index], coin)
    screen.blit(player_images[direction][image_index], player.rect)  # draw player based on cur dir and image index

    # ANIMATION SPEED
    image_counter += 1
    if image_counter >= 2:  # image_index only updates after same image has been displayed 2 times
        image_index = (image_index + 1) % len(player_images[direction])
        berries_image_index = (berries_image_index + 1) % len(berries_images)
        coin_images_index = (coin_images_index + 1) % len(coin_images)
        image_counter = 0

    # COLLISION

    # Berry Collision
    if player.rect.colliderect(berry):
        berry.x = (random.randint(1, 15)) * 35  # range 35-560
        berry.y = (random.randint(4, 18)) * 35  # range 140-665
        berry_counter += 1
        while any(wall.colliderect(berry) for wall in walls) or player.rect.colliderect(berry):
            berry.x = (random.randint(1, 15)) * 35
            berry.y = (random.randint(4, 18)) * 35

        if walls:
            removed_wall = random.choice(walls)
            walls.remove(removed_wall)
            wall_counter -= 1

    # Coin Collision
    if player.rect.colliderect(coin):
        # ONLY GENERATE NEW WALLS WHEN THERE IS SPACE?
        # Generate new wall
        new_wallX = (random.randint(1, 15)) * 35
        new_wallY = (random.randint(4, 18)) * 35
        new_wall = pygame.Rect((new_wallX, new_wallY, 35, 35))

        while any(wall.colliderect(new_wall) for wall in walls) \
                or any(wall.colliderect(coin) for wall in walls) \
                or player.rect.colliderect(new_wall):
            new_wall.x = (random.randint(1, 15)) * 35
            new_wall.y = (random.randint(4, 18)) * 35

        # FOR LOOP?
        for i in range(0, 225):
            if any(new_wall.move(dx, dy).colliderect(wall) for dx in [-35, 0, 35] for dy in [-35, 0, 35] for wall in walls):
                new_wall.x = (random.randint(1, 15)) * 35
                new_wall.y = (random.randint(4, 18)) * 35

        walls.append(new_wall)
        wall_counter += 1

        # Generate new coin
        coin.x = (random.randint(1, 15)) * 35  # range 35-560
        coin.y = (random.randint(4, 18)) * 35  # range 140-665
        coin_counter += 1
        while any(wall.colliderect(coin) for wall in walls) or berry.colliderect(coin) or player.rect.colliderect(coin):
            coin.x = (random.randint(1, 15)) * 35
            coin.y = (random.randint(4, 18)) * 35

    for wall in walls:
        screen.blit(brick_wall, wall)

    pygame.display.update()  # to refresh display
    clock.tick(7)  # adjusts frames per second for the animation

pygame.quit()
