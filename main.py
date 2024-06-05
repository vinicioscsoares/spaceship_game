import pygame
from random import randint
from os.path import join

#setup geral
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x= 100

#importando imagens

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = ( WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))

meteor_surf = pygame.image.load(join('images', 'meteor.png'))
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png'))
laser_rect = laser_surf.get_frect(bottomleft=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
#background estrelas
star_surf = pygame.image.load(join('images','star.png'))

moving_right = True

star_positions = [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range(20)]


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)   

    if moving_right:
        print(player_rect.left)
        player_rect.left += 1
        if player_rect.left >= WINDOW_WIDTH - 110:
            moving_right = False
    else:
        print(player_rect.left)
        player_rect.left -= 1
        if player_rect.left <= 0:
            moving_right = True
    
        

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    pygame.display.update()

pygame.quit()