import pygame
from sys import exit
import random

#initiate
pygame.init()
#screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Five Nights at Freddy's")
clock = pygame.time.Clock() 

test_surface = pygame.image.load('remake/Images/Cam 01.png')
#test_surface.fill((255,0,0))
#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface, (200,100))



    pygame.display.update()
    clock.tick(60)
