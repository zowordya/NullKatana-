import pygame, time
pygame.init()
window_size = [800, 600]
fps = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("My Game")
last_time = time.time()
x1, y1 = 20, 400
x2, y2 = 200, 390
x3, y3 = 400, 390
bg = pygame.image.load('BackGround.png')
player = pygame.image.load('right/1.png')
walk_right = [
    pygame.image.load('right/1.png'),
    pygame.image.load('right/2.png'),
    pygame.image.load('right/3.png'),
    pygame.image.load('right/4.png'),
    pygame.image.load('right/5.png'),
    pygame.image.load('right/6.png')
]
player_anim_count = 0
while True:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    dt = time.time() - last_time
    dt *= fps
    last_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()


    if keys[pygame.K_a]:
        x1 -= 2.5 * dt
    if keys[pygame.K_d]:
        x1 += 2.5 * dt


    screen.blit(walk_right[player_anim_count], (x1, y1))

    if player_anim_count == 5:
        player_anim_count = 0
    else:
        player_anim_count += 1
    clock.tick(15)
    pygame.display.update()
    '''
    player_rect = player.get_rect(topleft=(x1, y1))
    point_rect = point.get_rect(topleft=(x2, y2))
    point1_rect = point1.get_rect(topleft=(x3, y3))
'''


