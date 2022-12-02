import pygame
import time
 
pygame.init()
 
class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        global start_time
        if time.time() - start_time >= 0.3:
            start_time = time.time()
            self.y += bs


fps = 60
clock = pygame.time.Clock()
 
width, height = 352, 480
screen = pygame.display.set_mode((width, height))

#game_settings
bs = 32

run = True
figure = Figure(3 * bs, 0)

shape = [(0, 0), (1, 0), (1, 1), (2, 1)]
busy_cells = []

for i in range(width // bs + 1):
    busy_cells.append((i * bs, height))
# Game loop.
start_time = time.time()
while run:
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                figure.x += bs
            elif event.key == pygame.K_LEFT:
                figure.x -= bs
    figure.update()
    # print(busy_cells)
    for t in shape:
        for b in busy_cells:
            if figure.x + t[0] * bs == b[0] and figure.y + t[1] * bs == b[1] - bs:
                # print('sdfsdf')
                new_busy_cells = [(figure.x + c[0] * bs, figure.y + c[1] * bs) for c in shape]
                busy_cells.extend(new_busy_cells)
                figure = Figure(3 * bs, 0)
                break

    for t in shape:
        pygame.draw.rect(screen, (255, 255, 255), (figure.x + t[0] * bs, figure.y + t[1] * bs, bs, bs))
    for i in range(height // bs):
        pygame.draw.line(screen, (255, 255, 255), (0, i * bs), (width, i * bs))
    for i in range(width // bs):
        pygame.draw.line(screen, (255, 255, 255), (i * bs, 0), (i * bs, height))
    for c in busy_cells:
        pygame.draw.rect(screen, (255, 255, 255), (c[0], c[1], bs, bs))




    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()