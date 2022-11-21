import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_grav = 0

# Intro screen
player_stand = pygame.image.load('player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))
title_surf = text_font.render("Pixel Runner", False, (64, 64, 64))
title_rect = title_surf.get_rect(center=(410, 50))
inst_surf = text_font.render('Press SPACE to start', False, (64, 64, 64))
inst_rect = inst_surf.get_rect(center=(400, 350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_grav = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_grav = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:

        # loops snail position
        snail_rect.x -= 6
        if snail_rect.right <= 0:
            snail_rect.left = 800

        # places surfaces
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(snail_surface, snail_rect)
        score = display_score()

        # Player
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

    # Game State
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = text_font.render(
            f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = rect = score_message.get_rect(center=(400, 330))
        screen.blit(title_surf, title_rect)

        if score == 0:
            screen.blit(inst_surf, inst_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # 60 fps setting
    pygame.display.update()
    clock.tick(60)
