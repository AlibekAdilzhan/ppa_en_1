import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()


def create_font(text):
    font = pygame.font.SysFont("comicsansms", 22)
    text_surface = font.render(text, True, (255, 255, 0))
    return text_surface

# music = pygame.mixer.music.load("lesson_11_music_1.mp3")
sound_coin = pygame.mixer.Sound("sound_coin.wav")

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = coin_image
        self.rect = pygame.Rect(self.x, self.y, block_size // 2, block_size // 2)


fps = 60
clock = pygame.time.Clock()

# game settings
width = 640
height = 480
block_size = 64
screen = pygame.display.set_mode((width, height))
game_map = [
    "................................................",
    "................................................",
    "................................................",
    "................................................",
    ".....$$$.......$$$$.............................",
    "...$.bbbb$$$$$$$$$$$$$$$$$$$$$$...............................",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
]

def get_image(image_path, size_x, size_y):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (size_x, size_y))
    return image


snowman_right = get_image("SnowMan1_right.png", block_size, block_size)
snowman_left = get_image("SnowMan1_left.png", block_size, block_size)
zombie = get_image("stay_right.png", block_size, block_size)
block = get_image("mario_block.png", block_size, block_size)
coin_image = get_image("coin1.png", block_size // 2, block_size // 2)
jump_counter = 2

hero_x = 50
hero_y = 50
hero_x_old = hero_x
hero_y_old = hero_y
enemy_x = 400
enemy_y = 50

hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
enemy_rect = pygame.Rect(enemy_x, enemy_y, block_size, block_size)

rects = []
coins = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)
        if game_map[i][j] == "$":
            coin = Coin(j * block_size + block_size // 4, i * block_size + block_size // 4)
            coins.append(coin)


h_speed = 5
v_speed = 0
h_speed_enemy = 1
v_speed_enemy = 0
g = 2
can_jump = False
camera_x = 0

coins_counter = 0

run = True
snowman = snowman_right
# 
pygame.mixer.music.play(-1)
#game loop
while run:
    screen.fill((50, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump_counter < 2:
                if jump_counter == 1:
                    v_speed = -25
                else:
                    v_speed = -20
                jump_counter = jump_counter + 1
    
    keystate = pygame.key.get_pressed()

    hero_x_old = hero_x
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + h_speed
        snowman = snowman_right
    elif keystate[pygame.K_LEFT] == True:
        snowman = snowman_left
        hero_x = hero_x - h_speed
    # if hero_x >= width:
    #     hero_x = -block_size
    # if hero_x < -block_size:
    #     hero_x = width
    
    if hero_x - camera_x >= 0.7 * width:
        camera_x = camera_x + h_speed
    elif hero_x - camera_x <= 0.3 * width:
        camera_x = camera_x - h_speed
    hero_y_old = hero_y

    if hero_x < enemy_x:
        enemy_x = enemy_x - h_speed_enemy
    else:
        enemy_x = enemy_x + h_speed_enemy
    v_speed = v_speed + g
    v_speed_enemy = v_speed_enemy + g
    hero_y = hero_y + v_speed
    enemy_y = enemy_y + v_speed_enemy

    hero_rect.x = hero_x
    hero_rect.y = hero_y
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y

    if enemy_y >= 400:
        enemy_y = 400
        v_speed_enemy = 0


    for rect in rects:
        if hero_rect.colliderect(rect) == True and abs(hero_rect.y - rect.y) < block_size * 0.5:
            hero_x = hero_x_old
        elif hero_rect.colliderect(rect) == True:
            hero_y = hero_y_old
            v_speed = 0
            can_jump = True
            jump_counter = 0

        if enemy_rect.colliderect(rect) == True:
            enemy_y = rect.y - block_size
            v_speed_enemy = 0

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "b":
                screen.blit(block, (block_size * j - camera_x, block_size * i))

    for coin in coins:
        screen.blit(coin.image, (coin.x - camera_x, coin.y))
        if hero_rect.colliderect(coin.rect) == True:
            coins_counter = coins_counter + 1
            coins.remove(coin)
            del coin
            pygame.mixer.Sound.play(sound_coin)

    coins_text = create_font("COINS: " + str(coins_counter))
    screen.blit(snowman, (hero_x - camera_x, hero_y))
    screen.blit(zombie, (enemy_x - camera_x, enemy_y))
    screen.blit(coin_image, (10, 15))
    screen.blit(coins_text, (60, 10))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit() 