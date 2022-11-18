import pygame

pygame.init()

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
    "................................................",
    ".....bbbb........................................",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
]



snowman = pygame.image.load("SnowMan1_right.png")
snowman = pygame.transform.scale(snowman, (block_size, block_size))
zombie = pygame.image.load("stay_right.png")
zombie = pygame.transform.scale(zombie, (block_size, block_size))
block = pygame.image.load("mario_block.png")
block = pygame.transform.scale(block, (block_size, block_size))


hero_x = 50
hero_y = 50
hero_x_old = hero_x
hero_y_old = hero_y
enemy_x = 400
enemy_y = 50

hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
enemy_rect = pygame.Rect(enemy_x, enemy_y, block_size, block_size)

rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)



h_speed = 3
v_speed = 0
h_speed_enemy = 1
v_speed_enemy = 0
g = 2
can_jump = False

run = True

#game loop
while run:
    screen.fill((50, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and can_jump == True:
                v_speed = v_speed - 20
                can_jump = False
    
    keystate = pygame.key.get_pressed()

    hero_x_old = hero_x
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + 3
    elif keystate[pygame.K_LEFT] == True:
        hero_x = hero_x - 3
    if hero_x >= width:
        hero_x = -block_size
    if hero_x < -block_size:
        hero_x = width
    
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

        if enemy_rect.colliderect(rect) == True:
            enemy_y = rect.y - block_size
            v_speed_enemy = 0

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "b":
                screen.blit(block, (block_size * j, block_size * i))

    screen.blit(snowman, (hero_x, hero_y))
    screen.blit(zombie, (enemy_x, enemy_y))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit() 