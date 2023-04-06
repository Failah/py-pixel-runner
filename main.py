# video: The ultimate introduction to Pygame, by Clear Code
# link: https://www.youtube.com/watch?v=AY9MnQ4x3zk&ab_channel=ClearCode
# resume video from: 02:06:00

from sys import exit

import pygame


def display_score():
    current_time = (pygame.time.get_ticks() / 1000).__floor__() - start_time.__floor__()
    score_surface = test_font.render(f'Score:  {current_time}', False, score_color)
    score_rect = score_surface.get_rect(center=(width / 2, 50))
    screen.blit(score_surface, score_rect)


game_active = True
start_time = 0

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()
FPS = 60
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_color = (64, 64, 64)
score_bg = '#c0e8ec'
# score_surface = test_font.render("My Game", False, score_color)
# score_rect = score_surface.get_rect(center=(width / 2, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_y_pos = 300
snail_rect = snail_surface.get_rect(midbottom=(snail_x_pos, snail_y_pos))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    print('jump')
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = width
                start_time = (pygame.time.get_ticks() / 1000).__floor__()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # SCORE
        display_score()

        # SNAIL
        snail_rect.left -= 4
        if snail_rect.right < 0:
            snail_rect.left = width
        screen.blit(snail_surface, snail_rect)

        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # COLLISIONS
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')

    # KEYBOARD INPUTS
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(snail_rect):
    #     print('collision happening')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(FPS)
