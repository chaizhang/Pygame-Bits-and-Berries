# Bits & Berries TO-DO:
# 2) Wall and border collision
# 3) Randomize berry movement
# 5) Health bar
# 6) Refactor code
# 7) Make berry generation more rare? (e.g. eat 3 coins for 1 berry)
# 10) Needs to account for players who don't have the 'Berlin Sans FB Demi' font
# 11) Implement restart mechanics


import pygame
import sys
import random


class Player:
    def __init__(self, x, y, width, height, velocity):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = velocity


def load_graphic(file_name):
    graphic = pygame.image.load(str(file_name))
    return graphic


def resize(graphic, length, width):
    resized_graphic = pygame.transform.scale(graphic, (length, width))
    return resized_graphic


# LOAD GRAPHIC
bg = load_graphic("Blue_Background.png")
border = load_graphic("Blue_Border.png")
top_bar = load_graphic("Blue_Top_Bar.png")
berries = load_graphic("Red_Berries.png")
small_berries = load_graphic("Small_Red_Berries.png")
brick_wall = load_graphic("Red_Brick_Wall.png")
health = load_graphic("Health.png")
heart = load_graphic("Red_Heart.png")
starting_screen = load_graphic("Starting_Screen.png")
game_over_screen = load_graphic("Game_Over_Screen.png")
# =====
coin1 = load_graphic("Coin_Frame1.png")
coin2 = load_graphic("Coin_Frame2.png")
coin3 = load_graphic("Coin_Frame3.png")
coin4 = load_graphic("Coin_Frame4.png")
coin5 = load_graphic("Coin_Frame5.png")
coin6 = load_graphic("Coin_Frame6.png")
coin7 = load_graphic("Coin_Frame7.png")
coin8 = load_graphic("Coin_Frame8.png")
coin9 = load_graphic("Coin_Frame9.png")
coin10 = load_graphic("Coin_Frame10.png")
coin11 = load_graphic("Coin_Frame11.png")
coin12 = load_graphic("Coin_Frame12.png")
coin13 = load_graphic("Coin_Frame13.png")
coin14 = load_graphic("Coin_Frame14.png")
coin15 = load_graphic("Coin_Frame15.png")
coin16 = load_graphic("Coin_Frame16.png")
# =====
player_r1 = resize(load_graphic('Player_R1.png'), 35, 35)
player_r2 = resize(load_graphic('Player_R2.png'), 35, 35)
player_l1 = resize(load_graphic('Player_L1.png'), 35, 35)
player_l2 = resize(load_graphic('Player_L2.png'), 35, 35)
player_u1 = resize(load_graphic('Player_U1.png'), 35, 35)
player_u2 = resize(load_graphic('Player_U2.png'), 35, 35)
player_d1 = resize(load_graphic('Player_D1.png'), 35, 35)
player_d2 = resize(load_graphic('Player_D2.png'), 35, 35)
# =====

pygame.init()

# GAME WINDOW
SCREEN_WIDTH = 595  # pixels
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bits and Berries")

# PLAYER INITIALIZATION
player = Player(280, 385, 35, 35, 35)
player_images = {  # player images for animation
    'right': [player_r1, player_r2],
    'left': [player_l1, player_l2],
    'up': [player_u1, player_u2],
    'down': [player_d1, player_d2]
}

# WALL
wallX = (random.randint(1, 15)) * 35  # range 35-560
wallY = (random.randint(4, 18)) * 35  # range 140-665

# BERRY IMAGES FOR ANIMATION
berryX = (random.randint(1, 15)) * 35  # range 35-560
berryY = (random.randint(4, 18)) * 35  # range 140-665
berries_images = [berries, small_berries]
berry = pygame.Rect((berryX, berryY, 35, 35))

# COIN IMAGES FOR ANIMATION
coinX = (random.randint(1, 15)) * 35  # range 35-560
coinY = (random.randint(4, 18)) * 35  # range 140-665
coin_images = [
    coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8,
    coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16
]
# coin_images_index = 0
coin = pygame.Rect((coinX, coinY, 35, 35))

coin_counter_font = pygame.font.SysFont('Berlin Sans FB Demi', 25)
heart_counter = 3

# GAME INTRO SCREEN
intro_font = pygame.font.SysFont('Berlin Sans FB Demi', 20)
intro_screen = True
while intro_screen:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event1.type == pygame.KEYDOWN and event1.key == pygame.K_SPACE:
            intro_screen = False
    screen.blit(starting_screen, (0, 0))
    pygame.display.update()


# MAIN GAME LOOP
def game_loop():
    game_over = False
    initial_keypress = False
    player.rect.x = 280
    player.rect.y = 385
    direction = 'right'  # set initial direction
    clock = pygame.time.Clock()

    # For player/berry/coin animation
    image_index = 0  # set initial image index
    image_counter = 0  # keeps track of how many times an image has been displayed
    berries_image_index = 0
    coin_images_index = 0

    # ???
    wall_counter = 0
    berry_counter = 0
    coin_counter = 0

    walls = []
    # wall = pygame.Rect((wallX, wallY, 35, 35))

    while not game_over:
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and \
                    (event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or pygame.K_UP):
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

        # Render the counter
        coin_counter_text = coin_counter_font.render(str(coin_counter), True, (255, 255, 255))

        screen.fill((0, 0, 0))  # fill screen before drawing player

        # DRAWING
        screen.blit(bg, (35, 140))
        screen.blit(border, (0, 105))
        screen.blit(top_bar, (0, 0))
        screen.blit(berries_images[berries_image_index], berry)
        screen.blit(coin_images[coin_images_index], coin)
        screen.blit(player_images[direction][image_index], player.rect)  # draw player based on curr dir and image index
        screen.blit(coin_counter_text, (525, 35))
        screen.blit(health, (35, 35))
        screen.blit(health, (70, 35))
        screen.blit(health, (105, 35))

        # ANIMATION SPEED
        image_counter += 1
        if image_counter >= 2:  # image_index only updates after same image has been displayed 2 times
            image_index = (image_index + 1) % len(player_images[direction])
            berries_image_index = (berries_image_index + 1) % len(berries_images)
            coin_images_index = (coin_images_index + 1) % len(coin_images)
            image_counter = 0

        # Berry Collision
        if player.rect.colliderect(berry):
            berry.x = (random.randint(1, 15)) * 35  # range 35-560
            berry.y = (random.randint(4, 18)) * 35  # range 140-665
            berry_counter += 1
            while any(wall.colliderect(berry) for wall in walls) or player.rect.colliderect(
                    berry) or coin.colliderect(berry):
                berry.x = (random.randint(1, 15)) * 35
                berry.y = (random.randint(4, 18)) * 35

            if walls:
                removed_wall = random.choice(walls)
                walls.remove(removed_wall)
                wall_counter -= 1

        # Coin Collision
        if player.rect.colliderect(coin):
            # Generate new wall
            def generate_new_wall():
                new_wallX = (random.randint(1, 15)) * 35
                new_wallY = (random.randint(4, 18)) * 35
                return pygame.Rect((new_wallX, new_wallY, 35, 35))

            valid_position_found = False
            attempts = 0
            max_attempts = 255

            while not valid_position_found and attempts < max_attempts:
                new_wall = generate_new_wall()
                if not any(wall.colliderect(new_wall) for wall in walls) \
                        and not new_wall.colliderect(coin) \
                        and not new_wall.colliderect(berry) \
                        and not player.rect.colliderect(new_wall):
                    adjacent_collision = False
                    for dx in [-35, 0, 35]:
                        for dy in [-35, 0, 35]:
                            if dx == 0 and dy == 0:
                                continue
                            if any(new_wall.move(dx, dy).colliderect(wall) for wall in walls):
                                adjacent_collision = True
                                break
                        if adjacent_collision:
                            break
                    if not adjacent_collision:
                        valid_position_found = True
                attempts += 1

                if valid_position_found:
                    walls.append(new_wall)
                    wall_counter += 1

            # Generate new coin
            coin.x = (random.randint(1, 15)) * 35  # range 35-560
            coin.y = (random.randint(4, 18)) * 35  # range 140-665
            coin_counter += 1
            while any(wall.colliderect(coin) for wall in walls) or berry.colliderect(
                    coin) or player.rect.colliderect(coin):
                coin.x = (random.randint(1, 15)) * 35
                coin.y = (random.randint(4, 18)) * 35

        for wall in walls:
            screen.blit(brick_wall, wall)

        # Game ending logic
        if coin_counter > 3:
            game_over = True

        pygame.display.update()  # to refresh display
        clock.tick(7)  # adjusts frames per second for the animation


def ending_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                return

        screen.blit(game_over_screen, (0, 0))
        pygame.display.update()


while True:
    game_loop()
    ending_screen()
