import pygame
from settings import *
#from enemy import *
from player import *

moving_sprites = pygame.sprite.Group()
player = Player(300,200)
moving_sprites.add(player)

while Running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            Running = False   
    screen.fill("red")
    #player_group.update()
    moving_sprites.draw(screen)
    moving_sprites.update()
   #kamion_group.draw(screen)  
    #kamion_group.update() 
    #if pygame.sprite.spritecollide(player, kamion_group, False):
       # print("COLLISION!")


    pygame.display.flip()
    clock.tick(60)